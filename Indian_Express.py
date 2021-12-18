import requests as rq
from bs4 import BeautifulSoup
response= rq.get('https://indianexpress.com/')
soup = BeautifulSoup(response.text, 'html5lib')  
results = soup.find_all('h3')
records = []

for record in results:
    headline = record.text
    records.append(headline)
for i in range(len(records)):
    print(records[i],'\n')
