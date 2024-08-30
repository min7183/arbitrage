from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# Create your views here.
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
    
sports = get(stem + f"/v4/sports/?apiKey={apikey}")
success = 1
for sport in sports:
    if sport['title'] == 'MLB':
        key = sport['key']
        break
else:
    success = 0
if success:
    print(get_odds(key))

def index(request):
    return HttpResponse("Hello you are at the home of the arbitrage site")

def query_result(request, params : dict):
    try:
        results = get_odds(*params)
    except :
        raise Http404("the call could not be completed")
    return HttpResponse(results)