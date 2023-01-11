import requests 
from bs4 import BeautifulSoup




def download_link(name):
    title = str(name).lower()
    t = title.replace(' ', '+')
    
    try:
        url = f'https://moviesmod.in/?s={t}'
        r = requests.get(url)
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        links = ''
        anchors = soup.find_all('a',class_='post-image post-image-left')
        if anchors:
            for link in anchors:
                links= link.get('href')
                break
            nr = requests.get(str(links))
            nhtml = nr.content
            nsoup = BeautifulSoup(nhtml, 'html.parser')
            down_links = []
            qualities = nsoup.find_all('h4')
            all_qualities = []
            nanchors = nsoup.find_all('a',class_='maxbutton-1 maxbutton maxbutton-download-links')
            for h in qualities:
                if 'download' in str(h.getText()).lower():
                    all_qualities.append(h.getText())

            for l in nanchors:
                down_links.append(l.get('href'))
                
            
            return down_links,all_qualities
        
        url = f'https://topgmovies.xyz/?s={t}'
        r = requests.get(url)
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        links = ''
        anchors = soup.find_all('a',class_='post-image post-image-left')
        if anchors:
            for link in anchors:
                links= link.get('href')
                break
            nr = requests.get(str(links))
            nhtml = nr.content
            nsoup = BeautifulSoup(nhtml, 'html.parser')
            down_links = []
            qualities = nsoup.find_all('h3')
            all_qualities = []
            nanchors = nsoup.find_all('a',class_='maxbutton-1 maxbutton maxbutton-download-links')
            for h in qualities:
                if 'download' in str(h.getText()).lower():
                    all_qualities.append(h.getText())
                    
            for l in nanchors:
                down_links.append(l.get('href'))
                
        
            
            return down_links,all_qualities
        
    except:
        return None
    

link,qualities = download_link('dilwale 2015')
print(qualities,link)


// how to connect mysql?