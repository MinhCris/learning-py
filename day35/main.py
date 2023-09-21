import requests
Endpoint ="https://api.openweathermap.org/data/2.5/onecall"
api_key ="7ed61b18de273a65d87066ba5d90ac08"
weather_params={
    "lat":21.027763,
    "lon":105.834160,
    "appid": api_key,
}
response=requests.get(Endpoint,params=weather_params)
print(response.json())