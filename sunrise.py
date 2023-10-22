import requests
from datetime import datetime

MY_LAT = 28.669155
MY_LONG = 77.453758

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()
data = response.json()
sunrise = 5 + int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = 5 + int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(f"Sunset Time: {sunset}")
print(f"Sunrise Time: {sunrise}")
