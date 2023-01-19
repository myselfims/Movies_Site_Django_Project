from django.shortcuts import render
import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Liked_Movies
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
import requests
from django.shortcuts import redirect
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# Create your views here.


headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
# selenium function 

def direct_download(url):
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    op.add_argument("USER AGENT")
    driver = webdriver.Chrome(executable_path= ChromeDriverManager().install(),options=op)
    d_link = ''
    while d_link == '':
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content,'html.parser')
            anchors = soup.find_all('a')
            link = ''
            for a in anchors:
                if str(a.getText()) == '✅ Fast Server (G-Drive)':
                    link = a.get('href')
                    break


            driver.get(link)
            driver.get_screenshot_as_file("screenshot.png")

            btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="landing"]/span/a')))

            btn.click()

            btn2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/article/span[2]")))

            btn2.click()
            sleep(10)

            btn3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/article/span[1]")))

            btn3.click()

            sleep(10)

            btn4 = driver.find_element(By.ID,'two_steps_btn')
            l = btn4.get_attribute('href')

            driver.get(l)

            btn5 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/button")))

            btn5.click()

            sleep(10)

            input = driver.find_element(By.XPATH,'//*[@id="wi"]/div/input')
            d_link = str(input.get_attribute('value'))
        except:
            print('Trying again!')
    
    return str(input.get_attribute('value'))

# selenium function 

def movies_types(type):
    url = f'https://api.themoviedb.org/3/movie/{type}?api_key=65b4c60e268ed91234cd5991cb97f273'
    r = requests.request('GET', url=url)
    return r.json()
    

def movie_details(id):
    url = f'https://api.themoviedb.org/3/movie/{id}?api_key=65b4c60e268ed91234cd5991cb97f273'
    r = requests.request('GET', url=url)
    return r.json()

def cast_details(id):
    url = f'https://api.themoviedb.org/3/movie/{id}/credits?api_key=65b4c60e268ed91234cd5991cb97f273&language=en-US'
    r = requests.request('GET', url=url)
    return r.json()


def get_trailor(id):
    url = f"https://api.themoviedb.org/3/movie/{id}/videos?api_key=65b4c60e268ed91234cd5991cb97f273&language=en-US"
    r = requests.request('GET', url=url)
    trailor = r.json()
    try:
        for t in trailor['results']:
            if t['type'] == 'Trailer':
                trailor = t
                break
        return trailor
    except:
        return None
    




def download_movie(name,year):
    name = str(name).lower()
    final = name.replace(' ','+')
    url = f"https://moviesmod.in/?s={final}'+'{year}"
    return url


# headers = {
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
#     }


# proxies = [
#     'http://3.111.208.135:80',
#     'http://103.242.119.88:80',
#     'http://115.242.198.158:8080',
#     'http://103.146.170.252:83',
#     'http://183.88.223.17:8081',
#     'http://97.76.251.138:8080',
#     'http://151.64.222.230:3128',
#     'http://152.32.202.108:80',
#     'http://23.142.200.190:80',
#     'http://155.254.192.162:80	',
# ]




def download_link(name,year):
    title = str(name).lower()
    t = title.replace(' ', '+')
    
    try:
        url = f'https://moviesmod.com/?s={t}+{year}'
        r = requests.get(url, headers=headers)
        # for p in proxies:
        #     try:
        #         print(f'trying : {p}')
        #         req = requests.get(url,proxies={'http':p,'https':p},timeout=7)
        #         r = req
        #         break
        #     except:
        #         print('Trying again...')
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
        
        url = f'https://topgmovies.xyz/?s={t}+{year}'
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
                if 'download' in str(h.getText()).lower() and 'full hindi movie' not in str(h.getText()).lower():
                    all_qualities.append(h.getText())
                    
            for l in nanchors:
                down_links.append(l.get('href'))
                
            return down_links,all_qualities
        
        # Vega Movies Code
        
        url = f'https://vegamovies.loan/?s={t}+{year}'
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
            qualities = nsoup.find_all('h5')
            all_qualities = []
            nanchors = nsoup.find_all('a',class_='buttons btn_green')
            for h in qualities:
                all_qualities.append(h.getText())
                    
            for l in nanchors:
                down_links.append(l.get('href'))
                
            return down_links,all_qualities
        
    except:
        return None,None
    

search_url = 'https://www.omdbapi.com/?t=tt3896198&apikey=189f9712'

def searchmovie(query):
    url = f'https://api.themoviedb.org/3/search/movie?api_key=65b4c60e268ed91234cd5991cb97f273&language=en-US&query={query}&page=1&include_adult=false'
    r = requests.request('GET', url=url)
    print(type(r.json()))
    return r.json()

headers = {
    "X-RapidAPI-Key": "92a745b94emsh0cb338c535b85eap183d4ajsn2e683d429da5",
    "X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}

# response = requests.request("GET", url, headers=headers)

def home(request):
    try:
        url = f'https://api.themoviedb.org/3/trending/all/week?api_key=65b4c60e268ed91234cd5991cb97f273'
        r = requests.request('GET', url=url)
    except:
        return HttpResponse('Please check your internet connection!')
     
    response = r.json()
    
    if request.user.is_authenticated:

        user = User.objects.get(username = request.user.username)
        liked_movies = Liked_Movies.objects.filter(user=user)
        liked = []
        for movie in liked_movies:
            liked.append(int(movie.movie_id))
        print('movies',liked)
        return render(request, 'home.html',{'movies':response['results'],'user':user,'liked_movies': liked})
    
    
    return render(request, 'home.html',{'movies':response['results'],'user':'none'})

def popular(request):
    response = movies_types('popular')
        # user = User.objects.get(username = request.user.username)
        # for movie in liked_movies:
        #     liked.append(movie.movie_id)
        # print('movies',liked)
        # return render(request, 'home.html',{'movies':response['results'],'user':user,'liked_movies': liked})
    return render(request, 'popular.html',{'movies':response['results']})

def upcoming(request):
    response = movies_types('upcoming')
        # user = User.objects.get(username = request.user.username)
        # for movie in liked_movies:
        #     liked.append(movie.movie_id)
        # print('movies',liked)
        # return render(request, 'home.html',{'movies':response['results'],'user':user,'liked_movies': liked})
    return render(request, 'upcoming.html',{'movies':response['results']})

def top_rated(request):
    response = movies_types('top_rated')
        # user = User.objects.get(username = request.user.username)
        # for movie in liked_movies:
        #     liked.append(movie.movie_id)
        # print('movies',liked)
        # return render(request, 'home.html',{'movies':response['results'],'user':user,'liked_movies': liked})
    return render(request, 'top rated.html',{'movies':response['results']})
    


def favorite(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        liked_movies = Liked_Movies.objects.filter(user = user)
        liked = []
        liked_list = []
        if liked_movies:
            for movie in liked_movies:
                liked_list.append(int(movie.movie_id))
                movie = movie_details(movie.movie_id)
                liked.append(movie)
                    
        print(liked_list)
        print('movies',liked)
        return render(request, 'favorite.html',{'movies':liked,'user':user,'liked_movies': liked_list})
    return redirect('/')


def search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        result = searchmovie(query)
        print(result)
        liked_list = []
     
        if request.user.is_authenticated:
            user = User.objects.get(username=request.user.username)
            liked_movies = Liked_Movies.objects.filter(user = user)
            for m in liked_movies:
                liked_list.append(m.movie_id)
        return render(request, 'search.html',{'movies':result['results'],'liked_movies': liked_list})
    
    
def movie_detail(request,id):
    details = movie_details(id)
    cast = cast_details(id)
    trailor = get_trailor(id)
   
    
    try:
        links,qualities = download_link(details['title'],str(details['release_date'])[:4])
    except:
        links = None
        qualities = None
        
    if request.user.is_authenticated:
        
        user = User.objects.get(username=request.user.username)
        liked_movies = Liked_Movies.objects.filter(user = user)
        liked_list = []
        for m in liked_movies:
            liked_list.append(int(m.movie_id))
        return render(request, 'movie detail.html',{'movie':details,'cast':cast['cast'],'crew':cast['crew'],'production':details['production_companies'],'liked_movies':liked_list,'downloadlinks':links,'qualities':qualities,'trailor':trailor})
    
    return render(request, 'movie detail.html',{'movie':details,'cast':cast['cast'],'crew':cast['crew'],'production':details['production_companies'],'downloadlinks':links,'qualities':qualities,'trailor':trailor})

    
    


@csrf_exempt
def ajax_actions(request):
    action = request.POST.get('action')
    if action == 'like_movie':
        if request.user.is_authenticated:
            id = request.POST.get('movie_id')
            user = User.objects.get(username=request.user.username)
            check = Liked_Movies.objects.filter(user=user , movie_id = id)
            print(len(check))
            if len(check) == 0:
                liked_model = Liked_Movies(user=user, movie_id = id)
                liked_model.save()
                return JsonResponse({'msg':'liked'})
            for m in check:
                m.delete()
            print('deleted')
            return JsonResponse({'msg':'unliked'})
        return JsonResponse({'msg':'logged out'})
        
    elif action == 'signup':
        print('signup')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        check = User.objects.filter(username=username)
        if len(check) > 0:
            return JsonResponse({'msg':'User already exist!'})
        else:
            if len(password) >= 8:
                user = User.objects.create_user(username = username,email = email, password = password )
                user.save()
                login(request,user=user)
                return JsonResponse({'msg':'User created'})
            return JsonResponse({'msg':'Password should be minimum 8 characters'})
    
    elif action == 'login':
        print(action)
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(username=username, password=password)
            if user.is_authenticated:
                login(request,user=user)
                user = User.objects.get(username = request.user.username)
                liked_movies = Liked_Movies.objects.filter(user=user)
                liked_json = []
                for l in liked_movies:
                    liked_json.append({'id':l.movie_id})

                print(liked_json)
                return JsonResponse({'msg':'logged in','username':request.user.username, 'liked':liked_json})
            else:
                return JsonResponse({'msg':'usernot found'})
       
        except:
            return JsonResponse({'msg':'usernot found'})
        
    elif action == 'logout':
        print(action)
        logout(request)
        return JsonResponse({'msg':'logged out'})
    
    elif action == 'check_login':
        if request.user.is_authenticated:
            return JsonResponse({'msg':'true','username':request.user.username})
        return JsonResponse({'msg':'false'})