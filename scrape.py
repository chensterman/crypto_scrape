import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
SERP_API_KEY = os.getenv("SERP_API_KEY")
CMC_PRO_API_KEY = os.getenv("CMC_PRO_API_KEY")

def google_serper(query: str):
    """Helper function for searching results on Google."""
    url = "https://google.serper.dev/search"
    payload = json.dumps({
        "q": query
    })
    headers = {
        'X-API-KEY': SERP_API_KEY,
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload).json()
    results = [{"link": result["link"], "snippet": result["snippet"]} for result in response["organic"]]
    return results

def website_scrape(token: str, chain: str):
    """Helper function getting token official website URL from Google."""
    query = f"{token} {chain} website"
    try:
        # Take the first Google result
        result = google_serper(query)[0]
        return result
    except Exception as e:
        return {"error": str(e)}

def twitter_scrape(token: str, chain: str):
    """Helper function getting token Twitter URL from Google."""
    query = f"{token} {chain} twitter"
    try:
        results = google_serper(query)
        for result in results:
            link = result["link"]
            # Return the first result that has "twitter" in URL
            if "twitter" in link.lower():
                return result
        # Otherwise return null
        return None
    except Exception as e:
        return {"error": str(e)}
    
def discord_scrape(token: str, chain: str):
    """Helper function getting token Discord URL from Google."""
    query = f"{token} {chain} discord"
    try:
        results = google_serper(query)
        for result in results:
            link = result["link"]
            # Return the first result that has "twitter" in URL
            if "discord" in link.lower():
                return result
        # Otherwise return null
        return None
    except Exception as e:
        return {"error": str(e)}
    
def cmc_scrape(token: str):
    """
    Helper function to retrieve CMC info via CMC API.
    Documentation for the endpoint used: https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyQuotesLatest
    Also worth looking into (returns social media links): https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyInfo
    """
    # Get token name in lower case
    slug = token.lower()
    api_url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    parameters = {
        'slug': slug
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': CMC_PRO_API_KEY,
    }
    try:
        # GET request to CMC api token market data
        response = requests.request("GET", api_url, headers=headers, params=parameters).json()
        # Retrieve first token matching slug (API returns multiple, so just grab first)
        token_key = list(response["data"])[0]
        market_data = response["data"][token_key]["quote"]
        url = f"https://coinmarketcap.com/currencies/{slug}"
        return {"market_data": market_data, "link": url}
    except Exception as e:
        return {"error": str(e)}
    
def dextools_scrape(token: str):
    """Helper function getting token DexTools URL from Google."""
    query = f"{token} dextools"
    try:
        results = google_serper(query)
        for result in results:
            link = result["link"]
            # Return the first result that has "twitter" in URL
            if "dextools" in link.lower():
                return result
        # Otherwise return null
        return None
    except Exception as e:
        return {"error": str(e)}
    
def address_scrape(token: str):
    """Helper function getting first 3 Google results for token address."""
    query = f"{token} address"
    try:
        results = google_serper(query)
        return results[:3]
    except Exception as e:
        return {"error": str(e)}
    
def address_verbose_scrape(token: str, chain: str):
    """Helper function getting first 3 Google results for token + chain address."""
    query = f"{token} {chain} address"
    try:
        results = google_serper(query)
        return results[:3]
    except Exception as e:
        return {"error": str(e)}
    
def google_scrape(token: str):
    """Helper function getting first 5 Google results for token name."""
    query = f"{token} crypto"
    try:
        results = google_serper(query)
        return results[:5]
    except Exception as e:
        return {"error": str(e)}

def scrape(token: str, chain: str):
    website_data = website_scrape(token, chain)
    twitter_data = twitter_scrape(token, chain)
    discord_data = discord_scrape(token, chain)
    dextools_data = dextools_scrape(token)
    cmc_data = cmc_scrape(token)
    address_data = address_scrape(token)
    address_verbose_data = address_verbose_scrape(token, chain)
    google_data = google_scrape(token)
    return {
        "website": website_data,
        "twitter": twitter_data,
        "discord": discord_data,
        "dextools": dextools_data,
        "cmc": cmc_data,
        "address_results": address_data,
        "address_verbose_results": address_verbose_data,
        "google_results": google_data,
    }

if __name__ == "__main__":
    token = input("Enter token name here: ")
    chain = input("Enter blockchain name here: ")
    print(scrape(token, chain))