import requests

cn = input("Enter city name: ")

headers = {
    "User-Agent": "my-app"   
}

data = requests.get(f"https://nominatim.openstreetmap.org/search?city={cn}&format=json&limit=1", headers=headers).json()

print("Latitude",data[0]["lat"], "and", "Longititude", data[0]["lon"])