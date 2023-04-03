import requests
import json
import os
from dotenv import load_dotenv

def query_place(latitude, longitude):
    load_dotenv()

    url = os.environ['FOURSQUARE_API_URL']
    headers = {'Authorization': os.environ['FOURSQUARE_API_KEY']}
    params = {
        "ll": f"{latitude},{longitude}",
        "radius": 500,
        "categories": "13003", # BARS
        "sort": "DISTANCE",
        "open_now": True,
        "exclude_chains": True
    }

    response = requests.get(url, headers=headers, params=params)
    response_json = json.loads(response.text)
    results = format_results(response_json['results'])
    return results
    
def format_results(results):
    places = []
    for result in results:
        places.append((result['name'], result['location']['address']))

    return places