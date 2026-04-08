import requests

data = requests.get("https://api.escuelajs.co/api/v1/products/")
result = data.json()

for d in result:
    print(d.get("title"),d.get("price"), sep=" ")