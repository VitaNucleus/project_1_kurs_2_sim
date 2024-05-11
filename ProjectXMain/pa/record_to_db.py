import os
import json

from django.http import JsonResponse, HttpResponse
from .models import *


def set_cians(record, url, adr, i):
    print(record)
    if "floor" in list(record):
        floor = record['floor']
    else:
        floor = None
    if "flors" in list(record):
        floors = record['floors']
    else:
        floors = None
    if "additional_info" in list(record):
        additional_info = record['additional_info']
    else:
        additional_info = None

    if "areas" not in list(record):
        cost = record['cost']
        area = record['area']
        if i % 2 == 0:
            Cian = TblCianSale.objects.get_or_create(tcs_url=url, tcs_cost=cost, tcs_area=area, tcs_address=adr,
                                                     tcs_floor=floor, tcs_floors=floors,
                                                     tcs_additional_info=additional_info)
        else:
            Cian = TblCianRent.objects.get_or_create(tcr_url=url, tcr_cost=cost, tcr_area=area, tcr_address=adr,
                                                     tcr_floor=floor, tcr_floors=floors,
                                                     tcr_additional_info=additional_info)
    else:
        for i in range(len(record['areas'])):
            cost = record['costs'][i]
            area = record['areas'][i]
            if i % 2 == 0:
                Cian = TblCianSale.objects.get_or_create(tcs_url=url, tcs_cost=cost, tcs_area=area, tcs_address=adr,
                                                         tcs_floor=floor, tcs_floors=floors,
                                                         tcs_additional_info=additional_info)
            else:
                Cian = TblCianRent.objects.get_or_create(tcr_url=url, tcr_cost=cost, tcr_area=area, tcr_address=adr,
                                                         tcr_floor=floor, tcr_floors=floors,
                                                         tcr_additional_info=additional_info)


def set_address_and_cian(record, url, i):
    region = record['address']['region']
    city = record['address']['city']
    street = record['address']['street']
    house = record['address']['house']
    if 'district' in list(record['address']):
        district = record['address']['district']
    else:
        district = None
    if 'sub_district' in list(record['address']):
        sub_district = record['address']['sub_district']
    else:
        sub_district = None
    Adr = TblAddresses.objects.get_or_create(adr_region=region, adr_city=city, adr_district=district, adr_street=street,
                                             adr_sub_district=sub_district, adr_house=house)
    set_cians(record, url, Adr[0], i)


def values_for_cian(request):
    dir = os.path.abspath(__file__).replace("ProjectXMain/pa/record_to_db.py", "cache/cian/", 1)
    for i in range(4):
        with open(f"{dir}json_{i}.json", 'r') as file:
            values = json.load(file)
            for record in values:
                set_address_and_cian(values[record], record, i)

    return HttpResponse("Ok")