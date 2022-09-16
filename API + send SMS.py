""" this program sends my phone number a textmessage when the weather is cloudy
    using twilio
"""

import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "af4708023930e4deda9ee5cedb4f8c59"
account_sid = "AC5969289310ed12873feddcc5667eb1ba"
auth_token = "b0e91b17cbff1d4c89f3368df05e2996"

weather_params = {
    "lat": 53.544388,
    "lon": -113.490929,
    "appid": api_key,

}
will_rain = False
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
condition_code = int(weather_data["weather"][0]["id"])
if condition_code > 700:
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="This is Anietie testing a code",
        from_="+18159575375",
        to="+16478774335"
    )
    print(message.status)

