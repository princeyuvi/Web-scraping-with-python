import requests as rq
from bs4 import BeautifulSoup
response= rq.get('https://www.ndtv.com/')
soup = BeautifulSoup(response.text, 'html5lib')  
results = soup.select(".item-title")

records = []

for record in results:
    headline = record.text
    records.append(headline)
for i in range(len(records)):
    print(records[i],'\n')
