import requests
from bs4 import BeautifulSoup


def download_link(name,year):
    title = str(name).lower()
    t = title.replace(' ', '+')
    t = t.replace('.', '')
    t = t.replace(':', '')
    t = title.replace('_',' ')
    
    print(t,year)
    try:
        # Bolly4u.com code
        url = f'https://bolly4u.team/?s={t}+{year}'
        r = requests.get(url)
        print(url)
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        links = ''
        anchors = soup.find_all('a',class_='cursor-pointer overflow-hidden group block shadow-sm')
        if anchors:
            print('tryings..')
            try:
                for link in anchors:
                    title = soup.find_all('div',class_='mt-2 transition-all block px-2 py-3 shadow-inner text-gray-500 group-hover:text-indigo-500 tracking-wide text-sm')
                    if 'Movie Download' or 'Clean Movie' or '480p 720p' in str(title):
                        links= link.get('href')
                        break
                    
                nr = requests.get(str(links))
                nhtml = nr.content
                nsoup = BeautifulSoup(nhtml, 'html.parser')
                down_links = []
                qualities = nsoup.find_all('h4')
                all_qualities = []
                nanchors = nsoup.find_all('a',class_='buttn no')
                for h in qualities:
                    if 'links' in str(h.getText()).lower():
                        all_qualities.append(h.getText())
                        
                for l in nanchors:
                    if 'DIRECT [ G-DRIVE ]'.lower() in str(l.getText()).lower():
                        down_links.append(l.get('href'))
                print(down_links,all_qualities)
                if len(down_links) and len(all_qualities) > 0:
                    print('yes')
                    return down_links,all_qualities
            except:
                pass
        # Bolly4u.com code
  
        url = f'https://worldfree4u.gold/?s={t}+{year}'
        print(url)
        r = requests.get(url)
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        links = ''
        anchors = soup.find_all('a',class_='cursor-pointer overflow-hidden group block shadow-sm')
        if anchors:
            try:
                for link in anchors:
                    if '1080p' or '720p' in str(link.getText()):
                        links= link.get('href')
                        break
                nr = requests.get(str(links))
                nhtml = nr.content
                nsoup = BeautifulSoup(nhtml, 'html.parser')
                down_links = []
                qualities = nsoup.find_all('h4')
                all_qualities = []
                nanchors = nsoup.find_all('a',class_='dl2')
                for h in qualities:
                    if 'download' in str(h.getText()).lower():
                        all_qualities.append(h.getText())

                for l in nanchors:
                    down_links.append(l.get('href'))
                    
                
                if len(down_links) and len(all_qualities) > 0:
                    print('yes')
                    return down_links,all_qualities
            except: 
                pass
        
        url = f'https://topgmovies.xyz/?s={t}+{year}'
        print(url)
        r = requests.get(url)
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        links = ''
        anchors = soup.find_all('a',class_='post-image post-image-left')
        if anchors:
            try:
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
                    if 'download' in str(h.getText()).lower() and 'full hindi movie' not in str(h.getText()).lower():
                        all_qualities.append(h.getText())
                        
                for l in nanchors:
                    down_links.append(l.get('href'))
                    
                if len(down_links) and len(all_qualities) > 0:
                    print('yes')
                    return down_links,all_qualities
            except:
                pass
        
        # Vega Movies Code
        
        print('vega movies')
        url = f'https://vegamovies.loan/?s={t}+{year}'
        print(url)
        r = requests.get(url)
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        links = ''
        anchors = soup.find_all('a',class_='post-image post-image-left')
        if anchors:
            
            for link in anchors:
                print(link.get('href'))
                links= link.get('href')
                break
            nr = requests.get(str(links))
            nhtml = nr.content
            nsoup = BeautifulSoup(nhtml, 'html.parser')
            down_links = []
            qualities = nsoup.find_all('h5')
            all_qualities = []
            nanchors = nsoup.find_all('a',class_='buttons btn_green center')
            print('vega working..')
            for h in qualities:
                all_qualities.append(h.getText())
            print(nanchors)       
            for l in nanchors:
                print(l.get('href'))
                down_links.append(l.get('href'))
                
            if len(down_links) and len(all_qualities) > 0:
                    print('yes')
                    return down_links,all_qualities
        
    except:
        return None,None
    
    
links,q = download_link("Jung_e",2023)