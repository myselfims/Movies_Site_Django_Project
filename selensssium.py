import requests


proxies = [
    'http://103.161.145.99:8080',
    'http://3.111.208.135:80',
    'http://103.242.119.88:80',
    'http://115.242.198.158:8080',
    'http://103.146.170.252:83',
    'http://183.88.223.17:8081',
    'http://97.76.251.138:8080',
    'http://151.64.222.230:3128',
    'http://152.32.202.108:80',
    'http://23.142.200.190:80',
    'http://155.254.192.162:80	',
]

name = 'avatar'
year = '2022'
url = f'https://moviesmod.in/?s={name}+{year}'

for p in proxies:
    try:
        print(f'trying : {p}')
        r = requests.get(url,proxies={'http':p,'https':p})
        print(r.content)
        break
    except:
        print('Trying again...')
    
