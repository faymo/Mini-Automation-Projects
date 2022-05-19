import requests

API_KEY = "674f934af58c9eb0bfdc059948ee6b12"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]["description"]

    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather: ", weather)
    print("Temperature: ", temperature, "celsius")
else:
    print("An error occured.")
