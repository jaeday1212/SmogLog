import requests
from requests.exceptions import RequestException
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv() # Checks 

key = os.getenv("aq")

if not key:
    raise ValueError("API key not found!!")

header = {"X-API-Key":key}

endpoints = ['locations','sensors']

try:
    data_1 = requests.get(f"https://api.openaq.org/v3/{endpoints[0]}",headers=header)
    data_1.raise_for_status()



    print("Successful response!!")

except RequestException as e:
    raise
    

locations = data_1.json()

pprint(locations)

locs_id = [i["id"] for i in locations["results"]]

print(locs_id)