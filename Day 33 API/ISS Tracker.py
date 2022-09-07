""" This program tracks position of the ISS satellite and sends me an email when it is within my vicinity. """

import requests
from datetime import datetime
import smtplib
import time

# these are my longitude and latitude
LATITUDE = 53.544388
LONGITUDE = -113.490929

#  this returns true if it is close to me
def ISS_Overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if LATITUDE-5 <= iss_latitude <= LATITUDE+5 and LONGITUDE-5 <= iss_longitude <= LONGITUDE+5:
        return True

#  this returns true if it is night time
def is_night():
    parameters = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

#  this is where i send myself an email to go outside and look. 
while True:
    time.sleep(60)
    if ISS_Overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login("akpanusohanietie@gmail.com", "######")
            connection.sendmail(
                from_addr="akpanusohanietie@gmail.com",
                to_addrs="aniusoh@gmail.com",
                msg="Subject:ISS Tracker\n\nLook Up!"
            )
