import os
import json
from .models import TblCian, TblAddresses


def values_for_cian(TblAddresses, TblCian):
    dir = os.path.abspath(__file__).replace("ProjectXMain\pa\\record_to_db.py", "cache\\cian\\", 1)
    #for i in range(4):
    arrayAddresses = []
    arrayCian = []
    with open(f"{dir}json_{0}.json", 'r') as file:
        values = json.load(file)
        for record in values:
            Address = TblAddresses
            len_adr = len(record['address'])
            Address.adr_region = record['address']['region']
            Address.adr_city = record['address']['city']
            if len_adr == 4:
                Address.adr_city = record['address']['city']
                Address.adr_city = record['address']['city']
            elif len_adr == 5:
                Address.adr_city = record['address']['city']
                Address.adr_city = record['address']['city']
                Address.adr_city = record['address']['city']
            else:
                Address.adr_city = record['address']['city']
                Address.adr_city = record['address']['city']
                Address.adr_city = record['address']['city']
                Address.adr_city = record['address']['city']


if __name__ == "__main__":
    values_for_cian(TblAddresses, TblCian)