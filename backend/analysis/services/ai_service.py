"""
AI summary service for Carbon Watch.

Responsibilities:
- Gemini API configuration
- Prompt generation
- AI summary generation
- Graceful fallback if API is unavailable
"""

import logging

import google.generativeai as genai
from django.conf import settings

logger = logging.getLogger(__name__)

GEMINI_MODEL = "gemini-1.5-flash"


def _build_prompt(district_name, carbon_2020, carbon_2021, carbon_change, percentages):
    """
    Build the Gemini prompt from analysis results.

    Args:
        district_name: Name of the Nepal district.
        carbon_2020: Estimated carbon stock for 2020 (tonnes C).
        carbon_2021: Estimated carbon stock for 2021 (tonnes C).
        carbon_change: Net change in carbon stock (tonnes C).
        percentages: dict with forest/cropland/built_up/other percentages.

    Returns:
        Formatted prompt string.
    """
    direction = "decreased" if carbon_change < 0 else "increased"
    concern = "concerning" if carbon_change < -100000 else "relatively stable"

    return f"""
You are an environmental analyst. Write a 2-3 sentence plain-language summary
of this carbon monitoring data for {district_name} district in Nepal.

Satellite data (ESA WorldCover 2020 vs 2021):
- Carbon stock 2020: {carbon_2020:,.0f} tonnes C
- Carbon stock 2021: {carbon_2021:,.0f} tonnes C
- Net change: {carbon_change:+,.0f} tonnes C ({direction})
- Forest cover: {percentages['forest_area_pct']}%
- Cropland: {percentages['cropland_area_pct']}%
- Built-up area: {percentages['built_up_area_pct']}%

The trend is {concern}. Be factual and concise. Do not use bullet points.
""".strip()


def _build_fallback_summary(district_name, carbon_change, percentages):
    """
    Generate a rule-based fallback summary when Gemini is unavailable.

    Args:
        district_name: Name of the Nepal district.
        carbon_change: Net change in carbon stock (tonnes C).
        percentages: dict with forest/cropland/built_up/other percentages.

    Returns:
        Plain-text fallback summary string.
    """
    direction = "decreased" if carbon_change < 0 else "increased"
    return (
        f"{district_name} district shows {percentages['forest_area_pct']}% forest cover "
        f"based on ESA WorldCover satellite data. "
        f"Estimated carbon stock {direction} by {abs(carbon_change):,.0f} tonnes C "
        f"between 2020 and 2021."
    )


def generate_summary(district_name, carbon_2020, carbon_2021, carbon_change, percentages):
    """
    Generate a plain-language AI summary of carbon analysis results.

    Uses Gemini 1.5 Flash. Falls back to a rule-based summary
    if the API key is missing or the request fails.

    Args:
        district_name: Name of the Nepal district.
        carbon_2020: Estimated carbon stock for 2020 (tonnes C).
        carbon_2021: Estimated carbon stock for 2021 (tonnes C).
        carbon_change: Net change in carbon stock (tonnes C).
        percentages: dict with forest/cropland/built_up/other percentages.

    Returns:
        Summary string (AI-generated or fallback).
    """
    if not settings.GEMINI_API_KEY:
        logger.warning("GEMINI_API_KEY not set. Using fallback summary.")
        return _build_fallback_summary(district_name, carbon_change, percentages)

    try:
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel(GEMINI_MODEL)
        prompt = _build_prompt(
            district_name, carbon_2020, carbon_2021, carbon_change, percentages
        )
        response = model.generate_content(prompt)
        summary = response.text.strip()

        logger.info("AI summary generated for district=%s", district_name)
        return summary

    except Exception:
        logger.exception(
            "Gemini API failed for district=%s. Using fallback summary.",
            district_name
        )
        return _build_fallback_summary(district_name, carbon_change, percentages)
