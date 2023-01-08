import requests

search_url = 'https://www.omdbapi.com/?s=dhoom&apikey=189f9712'


def searchmovie(query):
    url = f'https://www.omdbapi.com/?s={query}&apikey=189f9712'
    r = requests.request('GET', url=url)
    return r.json()

res = searchmovie('ek tha tiger')
print(res)