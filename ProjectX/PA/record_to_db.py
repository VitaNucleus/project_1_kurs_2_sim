from django.conf import settings
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectX.settings')
settings.configure()

import django
django.setup()

import json
from models import TblAddresses



def values_for_cian():
    dir = os.path.abspath(__file__)#.replace("mainrecord_to_db.py", "", 1)
    print(dir)
    # for i in range(4):
    # with open(f"{dir}/cache/cian/json_{0}.json", 'r') as file:
    #     values = json.load(file)
    #     print(values)

if __name__ == "__main__":
    values_for_cian()