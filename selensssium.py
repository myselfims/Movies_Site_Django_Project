import requests
from bs4 import BeautifulSoup

url  = 'https://www.1377x.to/search/bahubali/1/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.2840.71 Safari/539.36'}
# headers={"User-Agent": "Mozilla/5.0"}
r = requests.get(url,headers=headers,timeout=15)
soup = BeautifulSoup(r.content,'html.parser')
anchors = soup.find_all('a',class_='torrentdown1')
print(anchors)
# for a in anchors:
#     if 'bahubali' in str(a.get('href')).lower():
#         r = requests.get(f'https://www.1377x.to/{a.get("href")}',headers=headers)
#         print(r.content)
        # break
