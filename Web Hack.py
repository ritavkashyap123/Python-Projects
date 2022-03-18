import requests
from bs4 import BeautifulSoup

# Website link
url = ''

res = requests.get(url).content

soup = BeautifulSoup(res,'html.parser')

links = soup.find_all('a')

for link in links:
    print(link['href'])