import requests 
from bs4 import BeautifulSoup




# def download_link(name):
#     title = str(name).lower()
#     t = title.replace(' ', '+')
    
#     try:
#         url = f'https://moviesmod.in/?s={t}'
#         r = requests.get(url)
#         html = r.content
#         soup = BeautifulSoup(html, 'html.parser')
#         links = ''
#         anchors = soup.find_all('a',class_='post-image post-image-left')
#         if anchors:
#             for link in anchors:
#                 links= link.get('href')
#                 break
#             nr = requests.get(str(links))
#             nhtml = nr.content
#             nsoup = BeautifulSoup(nhtml, 'html.parser')
#             down_links = []
#             qualities = nsoup.find_all('h4')
#             all_qualities = []
#             nanchors = nsoup.find_all('a',class_='maxbutton-1 maxbutton maxbutton-download-links')
#             for h in qualities:
#                 if 'download' in str(h.getText()).lower():
#                     all_qualities.append(h.getText())

#             for l in nanchors:
#                 down_links.append(l.get('href'))
                
            
#             return down_links,all_qualities
        
#         url = f'https://topgmovies.xyz/?s={t}'
#         r = requests.get(url)
#         html = r.content
#         soup = BeautifulSoup(html, 'html.parser')
#         links = ''
#         anchors = soup.find_all('a',class_='post-image post-image-left')
#         if anchors:
#             for link in anchors:
#                 links= link.get('href')
#                 break
#             nr = requests.get(str(links))
#             nhtml = nr.content
#             nsoup = BeautifulSoup(nhtml, 'html.parser')
#             down_links = []
#             qualities = nsoup.find_all('h3')
#             all_qualities = []
#             nanchors = nsoup.find_all('a',class_='maxbutton-1 maxbutton maxbutton-download-links')
#             for h in qualities:
#                 if 'download' in str(h.getText()).lower():
#                     all_qualities.append(h.getText())
                    
#             for l in nanchors:
#                 down_links.append(l.get('href'))
                
#             return down_links,all_qualities
        
        
        
#     except:
#         return None
    

# link,qualities = download_link('dilwale 2015')
# print(qualities,link)

# def download(t,y):
url = f'https://bolly4u.team/?s={"kgf+chapter+2"}+{2022}'
print(url)
r = requests.get(url)
html = r.content
soup = BeautifulSoup(html, 'html.parser')
links = ''
anchors = soup.find_all('a',class_='cursor-pointer overflow-hidden group block shadow-sm')
if anchors:
    # print(anchors)
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
            
        print('down:',down_links,'q:',all_qualities)
    except:
        pass
    
# links,q = download('kgf chapter 2',2022)
# print(links,q)