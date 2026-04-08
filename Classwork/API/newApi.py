import requests

lat = 21.2094892
lng = 72.8317058

headers = {
      "User-Agent": "my-app"
}

data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid=f7e41ce7e70845cc2b06568cfc7cfb4c&units=metric", headers=headers).json()

print(data["main"]["temp"])