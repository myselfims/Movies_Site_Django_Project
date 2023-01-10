import requests 
from bs4 import BeautifulSoup




def download_link(name):
    title = str(name).lower()
    t = title.replace(' ', '+')
    url = f'https://moviesmod.in/?s={t}'
    r = requests.get(url)
    html = r.content
    try:
        soup = BeautifulSoup(html, 'html.parser')
        links = ''
        anchors = soup.find_all('a',class_='post-image post-image-left')
        for link in anchors:
            links= link.get('href')
            break
        nr = requests.get(str(links))
        nhtml = nr.content
        nsoup = BeautifulSoup(nhtml, 'html.parser')
        down_link = []
        qualities = nsoup.find_all('h4')
        all_qualities = []
        nanchors = nsoup.find_all('a',class_='maxbutton-1 maxbutton maxbutton-download-links')
        for h in qualities:
            if 'download' in str(h.getText()).lower():
                all_qualities.append(h.getText())
        print(all_qualities)
        for l in nanchors:
            down_link.append(l.get('href'))
            
        print(down_link)
        
        return down_link
    except:
        return None
    

link = download_link('Avatar: The Way of Water')
print(link)