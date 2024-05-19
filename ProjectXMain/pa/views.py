import os
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.

def enter(request):
    return render(request, "login.html")

def Reg(request):
    return render(request, "registration.html")

def Lk(request):
    return render(request, "personal_area.html")

def json_test(request):
    dir = os.path.abspath(__file__).replace("ProjectXMain/pa/views.py", "cache/cian/", 1)
    with open(f"{dir}json_0.json", 'r') as file:
        object = json.load(file)
        return JsonResponse(object)


def river_segment(request):
    if request.method == 'POST':
        min_area = float(request.POST.get('min_area', 50))
        max_area = float(request.POST.get('max_area', 100))
        min_price = float(request.POST.get('min_price', 0))
        max_price = float(request.POST.get('max_price', 100000))
        rent = request.POST.get('rent', False)

        # selected_rivers = River.objects.filter(area__range=(min_area, max_area), price__range=(min_price, max_price))

        # if rent:
        #     selected_rivers = selected_rivers.filter(rent=True)
        #
        # average_price = selected_rivers.aggregate(avg_price=Avg('price'))['avg_price']

        return render(request, 'result.html',) #{'average_price': average_price})

    return render(request, 'river_segment.html')