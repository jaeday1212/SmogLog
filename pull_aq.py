import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv() # Checks 

key = os.getenv("aq")

header = {"X-API-Key":key}

data = requests.get("https://api.openaq.org/v3/locations",headers=header)

data.raise_for_status()

locations = data.json()

print("Successful response!!")

pprint(locations)
