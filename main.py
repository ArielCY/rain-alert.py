import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "e0c550f6b815d5b46084b6c6927b0f02"
account_sid = "AC7c357bb2c70d78979800071781270f39"
auth_token = "0549b71f9a1e07f77368c2e0bac53485"

#location is Chicago,IL
weather_params = {
    "lat": 41.878113,
    "lon": -87.629799,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.status_code) # 200 means OK
response.raise_for_status()

weather_data = response.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_weather in weather_slice:
    condition_code = hour_weather["weather"][0]["id"] # return string format
    if int(condition_code) < 700:
        # print("Bring an umbrella.")
        will_rain = True

if will_rain:
    #print("Bring an umbrella.") # only print out "Bring an umbrella" one time
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
    body="Remember to bring an umbrella, it's going to rain today.",
    from = "+12057362627", # trial number
    to= "+11234567890" # verified number
    )

    print(message.status)
