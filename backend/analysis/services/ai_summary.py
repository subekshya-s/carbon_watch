import google.generativeai as genai
from django.conf import settings

def generate_carbon_summary(district_name, carbon_stock, carbon_change, forest_pct, cropland_pct):
    try:
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')

        prompt = f"""
You are an environmental analyst. Write a 2-3 sentence plain-language summary of this carbon monitoring data for {district_name} district in Nepal.

Data (2020 vs 2021 comparison using ESA WorldCover satellite data):
- Estimated carbon stock: {carbon_stock:,.0f} tonnes C
- Carbon change: {carbon_change:+,.0f} tonnes C
- Forest cover: {forest_pct}%
- Cropland: {cropland_pct}%

Be factual, concise, and mention whether the trend is concerning or stable. Do not use bullet points.
"""
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"Analysis complete for {district_name}. Carbon stock estimated at {carbon_stock:,.0f} tonnes C with a change of {carbon_change:+,.0f} tonnes C between 2020 and 2021."
