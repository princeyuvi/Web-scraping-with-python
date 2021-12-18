import requests as rq
from bs4 import BeautifulSoup
response= rq.get('https://timesofindia.indiatimes.com/')
soup = BeautifulSoup(response.text, 'html5lib')  
results = soup.find_all('figcaption')
records = []

for record in results:
    headline = record.text
    records.append(headline)
for i in range(len(records)):
    print(records[i],'\n')
