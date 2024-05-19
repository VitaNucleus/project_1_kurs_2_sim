import os
import json

from django.db.models import Avg
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def enter(request):
    return render(request, "login.html")

def Reg(request):
    return render(request, "registration.html")

def Lk(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        context["user_name"] = user.first_name
        context["email"] = user.email
        return render(request, "personal_area.html", context=context)
    else:
        return HttpResponseRedirect('/')

def json_test(request):
    dir = os.path.abspath(__file__).replace("ProjectXMain/pa/views.py", "cache/cian/", 1)
    with open(f"{dir}json_0.json", 'r') as file:
        object = json.load(file)
        return JsonResponse(object)


def recomendation_form(request):
    if request.method == 'POST':
        context = {}
        context['values_chart'] = {}
        min_area = float(request.POST.get('min_area'))
        max_area = float(request.POST.get('max_area'))
        min_price = float(request.POST.get('min_price'))
        max_price = float(request.POST.get('max_price'))
        step_area = float(request.POST.get("area_step"))
        rent = request.POST.get('rent')

        if not step_area:
            step_area = max_area - min_area / 10

        while (min_area < max_area):
            temp_area = min_area + step_area
            if temp_area > max_area:
                temp_area = max_area

            if rent:
                queryset = (TblCianRent.objects.filter(tcr_area__range=(min_area, temp_area),
                                                      tcr_cost__range=(min_price, max_price),
                                                      ).aggregate(avg_area=Avg(f'tcr_area'),
                                                                 avg_price=Avg(f'tcr_cost')))
            else:
                queryset = (TblCianSale.objects.filter(tcs_area__range=(min_area, temp_area),
                                                      tcs_cost__range=(min_price, max_price),
                                                      ).aggregate(avg_area=Avg('tcs_area'),
                                                                 avg_price=Avg('tcs_cost')))
            min_area += step_area
            context['values_chart'][f'{round(queryset["avg_area"], 2)}'] = round(queryset['avg_price'], 2)

        return render(request, 'result.html', context=context)

    return render(request, 'recomendation_form.html')


def set_params_delete_unnecessary(i, obj):
    result = {}
    if i == 0:
        result["cost"] = obj.tcr_cost
        result["area"] = obj.tcr_area
        result["floor"] = obj.tcr_floor
        result["address"] = obj.tcr_address
        result["floors"] = obj.tcr_floors
        result["additional_info"] = obj.tcr_additional_info
    else:
        result["cost"] = obj.tcs_cost
        result["area"] = obj.tcs_area
        result["floor"] = obj.tcs_floor
        result["address"] = obj.tcs_address
        result["floors"] = obj.tcs_floors
        result["additional_info"] = obj.tcs_additional_info
    return result


def delete_unnecessary(requset):
    for i in range(2):
        if i == 0:
            queryset = TblCianRent.objects.filter()
        else:
            queryset = TblCianSale.objects.filter()
        for record in queryset:
            if i == 0:
                url = record.tcr_url
                for_delete = TblCianRent.objects.filter(tcr_url=url)
            else:
                url = record.tcs_url
                for_delete = TblCianSale.objects.filter(tcs_url=url)
            for j in range(len(for_delete)):
                result = set_params_delete_unnecessary(i, for_delete[j])
                for k in range(j + 1, len(for_delete)):
                    next_result = set_params_delete_unnecessary(i, for_delete[k])
                    if ((result["cost"] == next_result["cost"]) and (result["area"] == next_result["area"]) and
                            (result["floor"] == next_result["floor"]) and (result["address"] == next_result["address"])
                            and (result["floors"] == next_result["floors"]) and
                            (result["additional_info"] == next_result["additional_info"])):
                        for_delete[k].delete()
    return HttpResponse("Ok")


def split_sale_and_rent(requset):
    for i in range(2):
        if i == 0:
            queryset = TblCianRent.objects.filter()
        else:
            queryset = TblCianSale.objects.filter()
        for record in queryset:
            if i == 0:
                url = record.tcr_url
                if "sale" in url.split('/'):
                    Cian, exist = TblCianSale.objects.get_or_create(tcs_url=url, tcs_cost=record.tcr_cost,
                                                                    tcs_area=record.tcr_area,
                                                                    tcs_address=record.tcr_address,
                                                                    tcs_floor=record.tcr_floor,
                                                                    tcs_floors=record.tcr_floors,
                                                                    tcs_additional_info=record.tcr_additional_info)
                    record.delete()
            else:
                url = record.tcs_url
                if "rent" in url.split('/'):
                    Cian, exist = TblCianRent.objects.get_or_create(tcr_url=url, tcr_cost=record.tcs_cost,
                                                                    tcr_area=record.tcs_area,
                                                                    tcr_address=record.tcs_address,
                                                                    tcr_floor=record.tcs_floor,
                                                                    tcr_floors=record.tcs_floors,
                                                                    tcr_additional_info=record.tcs_additional_info)
                    record.delete()
    return HttpResponse("Ok")