import os
import json

from django.db.models import Avg, Count, Min, Max
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from datetime import datetime

# Create your views here.
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
        context['values_chart_rent'] = {}
        context['values_chart_sale'] = {}
        context['update_time'] = datetime.now().strftime('%Y-%m-%d 5:00:00')

        min_area = float(request.POST.get('min_area'))
        max_area = float(request.POST.get('max_area'))

        if request.POST.get('min_price'):
            min_price = float(request.POST.get('min_price'))
        else:
            min_rent = TblCianRent.objects.aggregate(Min('tcr_cost'))['tcr_cost__min']
            min_sale = TblCianSale.objects.aggregate(Min('tcs_cost'))['tcs_cost__min']
            min_price = min(min_rent, min_sale)

        if request.POST.get('max_price'):
            max_price = float(request.POST.get('max_price'))
        else:
            max_rent = TblCianRent.objects.aggregate(Max('tcr_cost'))['tcr_cost__max']
            max_sale = TblCianSale.objects.aggregate(Max('tcs_cost'))['tcs_cost__max']
            max_price = max(max_rent, max_sale)

        if request.POST.get("area_step"):
            step_area = float(request.POST.get("area_step"))
        else:
            step_area = (max_area - min_area) / 10

        context["count_rent"] = TblCianRent.objects.filter(tcr_area__range=(min_area, max_area),
                                                           tcr_cost__range=(min_price, max_price),
                                                           ).aggregate(Count("tcr_id"))['tcr_id__count']
        context["count_sale"] = TblCianSale.objects.filter(tcs_area__range=(min_area, max_area),
                                                           tcs_cost__range=(min_price, max_price),
                                                           ).aggregate(Count("tcs_id"))['tcs_id__count']

        district = request.POST.get('district')

        while (min_area < max_area):
            temp_area = min_area + step_area
            if temp_area > max_area:
                temp_area = max_area

            if district == "Все районы":
                queryset_rent = TblCianRent.objects.filter(tcr_area__range=(min_area, temp_area),
                                                           tcr_cost__range=(min_price, max_price),
                                                           ).aggregate(avg_area=Avg('tcr_area'),
                                                                       avg_price=Avg('tcr_cost'),
                                                                       count=Count('tcr_id'))
                queryset_sale = TblCianSale.objects.filter(tcs_area__range=(min_area, temp_area),
                                                           tcs_cost__range=(min_price, max_price),
                                                           ).aggregate(avg_area=Avg('tcs_area'),
                                                                       avg_price=Avg('tcs_cost'),
                                                                       count=Count('tcs_id'))
            else:
                queryset_rent = TblCianRent.objects.filter(tcr_area__range=(min_area, temp_area),
                                                           tcr_cost__range=(min_price, max_price),
                                                           tcr_address__adr_district=district,
                                                           ).aggregate(avg_area=Avg('tcr_area'),
                                                                       avg_price=Avg('tcr_cost'),
                                                                       count=Count('tcr_id'))
                queryset_sale = TblCianSale.objects.filter(tcs_area__range=(min_area, temp_area),
                                                           tcs_cost__range=(min_price, max_price),
                                                           tcs_address__adr_district=district,
                                                           ).aggregate(avg_area=Avg('tcs_area'),
                                                                       avg_price=Avg('tcs_cost'),
                                                                       count=Count('tcs_id'))

            if queryset_rent['avg_price'] and queryset_rent['avg_area']:
                cost_m = queryset_rent['avg_price'] / queryset_rent['avg_area']
                count = queryset_rent['count']
                context['values_chart_rent'][f'{min_area}-{temp_area}'] = [round(cost_m, 2), count]
            else:
                context['values_chart_rent'][f'{min_area}-{temp_area}'] = ["Нет данных", 0]

            if queryset_sale['avg_price'] and queryset_sale['avg_area']:
                cost_m = queryset_sale['avg_price'] / queryset_sale['avg_area']
                count = queryset_sale['count']
                context['values_chart_sale'][f'{min_area}-{temp_area}'] = [round(cost_m, 2), count]
            else:
                context['values_chart_sale'][f'{min_area}-{temp_area}'] = ["Нет данных", 0]

            min_area += step_area

        return render(request, 'result.html', context=context)

    context = {}
    context['districts'] = []
    districts = TblAddresses.objects.order_by().values_list("adr_district").distinct()
    for item in districts:
        if item[0]:
            context['districts'].append(item[0])

    return render(request, 'recomendation_form.html', context=context)


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


def get_user_object(request):
    if request.method == "GET":
        return render(request, "get_object.html")
    elif request.method == "POST":
        cost = float(request.POST.get("price"))
        area = float(request.POST.get("area"))
        address = {"city": request.POST.get("city"),
                   "district": request.POST.get("district"),
                   "street": request.POST.get("street"),
                   "home": request.POST.get('building'),}
        if request.POST.get('floor'):
            floor = request.POST.get('floor')
        else:
            floor = None
        if request.POST.get('floors'):
            floors = request.POST.get('floors')
        else:
            floors = None
        return HttpResponseRedirect("/home/")