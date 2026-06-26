# Carbon Watch - Project Plan

## AOI Source
Nepal's 77 districts, loaded from a static GeoJSON file (data/nepal_districts.geojson).

## Core User Flow
1. User selects a district (via map or list)
2. User triggers analysis for a date range
3. System fetches satellite data (Sentinel-2) for that district via Google Earth Engine
4. System calculates land cover change and estimated carbon stock/change
5. AI generates a plain-language summary of the results
6. User views calculated estimate + AI summary side by side

## Real vs Mocked for Demo
- Real: Earth Engine analysis for 3-5 pre-selected districts (cached for demo speed)
- Mocked initially, replaced later: analyze endpoint returns placeholder data until real pipeline is wired in
- AI summary: real API call, but with a fallback message if the API fails

## Out of Scope (for this version)
- Ground-truth validation
- Permanence/leakage accounting
- Carbon credit registry integration
