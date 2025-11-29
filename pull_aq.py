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

    data_2 = requests.get(f"https://api.openaq.org/v3/{endpoints[1]}",headers=header)
    data_2.raise_for_status()

except RequestException as e:
    print(f"Something went wrong with request exception {e}")



locations = data_1.json()

print("Successful response!!")

pprint(locations["results"][0])

