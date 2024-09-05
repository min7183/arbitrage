from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from oddsapi import get_odds

# Create your views here.
def index(request):
    return HttpResponse("Hello you are at the home of the arbitrage site")

def query_result(request, params : dict):
    try:
        results = get_odds(*params)
    except Exception:
        raise Http404("the call could not be completed")
    return HttpResponse(results)
