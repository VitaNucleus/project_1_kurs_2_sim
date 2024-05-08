import os
import json

from django.http import JsonResponse, HttpResponse
from .models import TblCian, TblAddresses


def set_cians(record, url):
    print("a")
    queryset = TblAddresses.objects.all().last()
    for i in queryset:
        print(i)
    adr = queryset.id
    print(record)
    if "floor" in list(record):
        floor = record['floor']
    else:
        floor = None
    if "flors" in list(record):
        floors = record['floors']
    else:
        floors = None
    rent_sale = "sale"
    print(list(record))
    if "areas" not in list(record):
        cost = record['cost']
        area = record['area']
        Cian = TblCian(tc_url=url, tc_cost=cost, tc_area=area, tc_address=adr)
        Cian.save()
    else:
        for i in range(len(record['areas'])):
            cost = record['costs'][i]
            area = record['areas'][i]
            Cian = TblCian(tc_url=url, tc_cost=cost, tc_area=area, tc_address=adr)
            Cian.save()


def set_address(record):
    len_adr = len(record['address'])
    region = record['address']['region']
    city = record['address']['city']
    street = record['address']['street']
    house = record['address']['house']
    if len_adr == 4:
        Adr = TblAddresses(adr_region=region, adr_city=city, adr_street=street, adr_house=house)
    elif len_adr == 5:
        district = record['address']['district']
        Adr = TblAddresses(adr_region=region, adr_city=city, adr_district=district, adr_street=street,
                               adr_house=house)
    else:
        district = record['address']['district']
        sub_district = record['address']['sub_district']
        Adr = TblAddresses(adr_region=region, adr_city=city, adr_district=district, adr_street=street,
                               adr_house=house)
    Adr.save()
    print(Adr.adr_id)

def values_for_cian(request):
    dir = os.path.abspath(__file__).replace("ProjectXMain/pa/record_to_db.py", "cache/cian/", 1)
    #for i in range(4):
    arrayAddresses = []
    arrayCian = []
    with open(f"{dir}json_{0}.json", 'r') as file:
        values = json.load(file)
        for record in values:
            set_address(values[record])
            set_cians(values[record], record)

        return HttpResponse("Ok")