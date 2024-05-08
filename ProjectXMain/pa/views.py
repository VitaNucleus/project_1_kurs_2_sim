import os
import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def test(request):
    return render(request, "Lk.html")

def json_test(request):
    dir = os.path.abspath(__file__).replace("ProjectXMain/pa/views.py", "cache/cian/", 1)
    with open(f"{dir}json_0.json", 'r') as file:
        object = json.load(file)
        return JsonResponse(object)