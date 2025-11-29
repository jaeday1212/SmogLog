import requests
from requests.exceptions import RequestException
from dotenv import load_dotenv
import os
from pprint import pprint
import sys
import time

load_dotenv() # Checks 

key = os.getenv("aq")

if not key:
    raise ValueError("API key not found!!")

header = {"X-API-Key":key}

endpoints = ['locations','sensors']

try:
    data_1 = requests.get(f"https://api.openaq.org/v3/{endpoints[0]}",headers=header)
    data_1.raise_for_status()
    
    locations = data_1.json()

    locs_id = [i["id"] for i in locations["results"]][:3]

except RequestException as e:
    raise 

except Exception as e:
    print(f"logic error {e}")
    sys.exit(1)

print("Successful response!! and extraction")

print(locs_id)

for specific_ids in locs_id:
    sensors = requests.get(f"https://api.openaq.org/v3/{endpoints[0]}/{specific_ids}",headers=header) # Successful response object needs to be unpacked
    pprint(sensors)