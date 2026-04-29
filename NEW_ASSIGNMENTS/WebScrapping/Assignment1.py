import requests 
import pandas as pd 
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
respone = requests.get(url)

soup = BeautifulSoup(respone.text,'html.parser')

jt = soup.find_all("h2", class_="title is-5")
cn = soup.find_all("h3", class_="subtitle is-6 company")
lc = soup.find_all("p", class_="location")

jobName = [jb.text for jb in jt]
companyName = [c.text for c in cn]
companyLocation = [l.text for l in lc]

contentFile = pd.DataFrame({'Job-Name':jobName, 'Company-Name':companyName, 'Location':companyLocation})
contentFile.to_excel('~/Desktop/webscrapping/webScrappingAssignments.xlsx', index=False)