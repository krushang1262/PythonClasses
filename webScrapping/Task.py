import requests 
import pandas as pd
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')

jobName = soup.find_all("h2", class_="title is-5")
jobCompany = soup.find_all("h3", class_="subtitle is-6 company")
jobLocation = soup.find_all("p", class_="location")

Name = [N.text for N in jobName]
Company = [C.text for C in jobCompany]
locations = [L.text for L in jobLocation]

df = pd.DataFrame({'Job-Title':Name, 'Company-name':Company, 'Locations':locations})
df.to_excel('~/Desktop/webscrapping/output.xlsx', index=False)