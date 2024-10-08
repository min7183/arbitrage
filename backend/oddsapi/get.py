import requests
from pprint import pprint
from dotenv import load_dotenv
import os

stem = "https://api.the-odds-api.com"
load_dotenv()
apikey = os.getenv("API_KEY")

def get(url):
    print(url)
    resp = requests.get(url)
    print(resp)
    return resp.json()

def get_odds(key, region="us", oddsFormat="american", markets=[]):
    url = stem + f"/v4/sports/{key}/odds?regions={region}&oddsFormat={oddsFormat}&markets={','.join(markets)}&apiKey={apikey}" 
    return get(url)
    
if __name__ == '__main__':
    sports = get(stem + f"/v4/sports/?apiKey={apikey}")
    success = 1
    for sport in sports:
        if sport['title'] == 'MLB':
            key = sport['key']
            break
    else:
        success = 0
    if success:
        pprint(get_odds(key))
