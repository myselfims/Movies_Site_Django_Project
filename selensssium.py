import requests
from bs4 import BeautifulSoup

url  = 'https://www.1377x.to/search/bahubali/1/'
headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.content,'html.parser')
anchors = soup.find_all('a',class_='torrentdown1')
print(anchors)
for a in anchors:
    if 'bahubali' in str(a.get('href')).lower():
        r = requests.get(f'https://www.1377x.to/{a.get("href")}',headers=headers)
        print(r.content)
        break
