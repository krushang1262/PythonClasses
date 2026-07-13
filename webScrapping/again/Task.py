import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
web = requests.get(url)

soup = BeautifulSoup(web.text,"html.parser")

img = soup.find_all("a", href=True)
for i in img:
    link = "https://books.toscrape.com/"+i['href']
    if ("category" not in link):
        data = requests.get(link)
        dd = BeautifulSoup(data.text,"html.parser")
        desc = dd.find("div",id="product_description")
        if desc:    
            print(desc.find_next("p").text, "\n" )