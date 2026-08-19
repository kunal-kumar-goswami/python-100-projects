import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api= "766622b67002134fcd92e73c036c7ecf"
account_sid = "AC2a90505ea61b147d539c236aa679dbc6"
auth_token = "30fad39e1ef225d3467ae4fd7cb77a46"
 
weather_params ={
    "lat": 20.593683,
    "lon": 78.962883,
    "appid": api ,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params= weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
 
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
         from_='whatsapp:+14155238886',
        body=  "It's going to rain today. Remember to bring an Umbrella☔",
        to='whatsapp:+917479643994'
)

print(message.status)


