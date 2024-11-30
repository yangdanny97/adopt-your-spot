import json
import requests

# Use Google Maps geocoding API to get location for each address

API_KEY = "YOUR API KEY HERE"

with open("adopt_your_spot.json", "r") as f:
    entries = json.load(f)
    for entry in entries:
        address = entry["address"].replace(" ", "+")
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        results = data["results"]
        if len(results) == 0:
            print(address.replace("+", " "))
            entry["location"] = results
        else:
            entry["location"] = results[0]
    with open("adopt_your_spot_geocoded.json", "w") as f2:
        json.dump(entries, f2)
