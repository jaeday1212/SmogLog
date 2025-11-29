import requests

data = requests.get("https://api.openaq.org/v2/locations")
data.raise_for_status()
locations = data.json()
print("Successful response!!")

