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
# Create your views here.


# url = "https://imdb-top-100-movies.p.rapidapi.com/"

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
    return r.json()
    




def download_movie(name,year):
    name = str(name).lower()
    final = name.replace(' ','+')
    url = f"https://moviesmod.in/?s={final}'+'{year}"
    return url


def download_link(name,year):
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
        down_link = ''
        nanchors = nsoup.find_all('a',class_='maxbutton-1 maxbutton maxbutton-download-links')
        for l in nanchors:
            down_link= l.get('href')
            break
        return down_link
    except:
        return None
    

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
    for t in trailor['results']:
        if t['type'] == 'Trailer':
            trailor = t
            break
    print(cast)
    url = download_link(details['title'],str(details['release_date'])[:4])
    if request.user.is_authenticated:
        
        user = User.objects.get(username=request.user.username)
        liked_movies = Liked_Movies.objects.filter(user = user)
        liked_list = []
        for m in liked_movies:
            liked_list.append(int(m.movie_id))
        return render(request, 'movie detail.html',{'movie':details,'cast':cast['cast'],'crew':cast['crew'],'production':details['production_companies'],'liked_movies':liked_list,'downloadlink':url,'trailor':trailor})
    
    return render(request, 'movie detail.html',{'movie':details,'cast':cast['cast'],'crew':cast['crew'],'production':details['production_companies'],'downloadlink':url,'trailor':trailor})

    
    


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
        
        user = User.objects.create_user(username = username,email = email, password = password )
        user.save()

        return JsonResponse({'msg':'User created'})
    
    elif action == 'login':
        print(action)
        username = request.POST.get('username')
        password = request.POST.get('password')
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
        
    elif action == 'logout':
        print(action)
        logout(request)
        return JsonResponse({'msg':'logged out'})
    
    elif action == 'check_login':
        if request.user.is_authenticated:
            return JsonResponse({'msg':'true','username':request.user.username})
        return JsonResponse({'msg':'false'})