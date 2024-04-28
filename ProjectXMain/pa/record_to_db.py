import sys
sys.path.append("..")  # Add the parent directory to the path

from .models import *
import os
import json



def values_for_cian():
    dir = os.path.abspath(__file__).replace("ProjectX\PA\\record_to_db.py", "cache\\cian\\", 1)
    print(dir)
    #for i in range(4):
    # with open(f"{dir}json_{0}.json", 'r') as file:
    #     values = json.load(file)
    #     print(values)

if __name__ == "__main__":
    values_for_cian()