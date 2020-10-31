from django.shortcuts import render
from django.views.generic import TemplateView
import requests
# Create your views here.

def location_search(request):
    output = ""
    if request.method == "POST":
        location = request.POST.get('title')
        PARAMS = {'q':location}
        URL = "https://geodata.gov.hk/gs/api/v1.0.0/locationSearch"
        response = requests.get(
            url=URL,params=PARAMS).json()
        output = response[0]["nameEN"]
    context = {
        "info": output
    }
    return render(request, "locations.html", context)
