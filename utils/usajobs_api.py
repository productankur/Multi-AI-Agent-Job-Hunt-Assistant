import requests
import os

def fetch_usajobs(keyword, location="remote", results_per_page=5):
    # Works on both Colab and Streamlit Cloud
    try:
        import streamlit as st
        USAJOBS_API_KEY = st.secrets["USAJOBS_API_KEY"]
    except:
        from config import USAJOBS_API_KEY

    headers = {
        "Authorization-Key": USAJOBS_API_KEY,
        "User-Agent": "ankur.product.champ@gmail.com",
        "Host": "data.usajobs.gov"
    }
    params = {
        "Keyword": keyword,
        "LocationName": location,
        "ResultsPerPage": results_per_page
    }
    url = "https://data.usajobs.gov/api/search"
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return []
    data = response.json()
    jobs = data.get("SearchResult", {}).get("SearchResultItems", [])
    return jobs
