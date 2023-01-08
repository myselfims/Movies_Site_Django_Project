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
# Create your views here.


url = "https://imdb-top-100-movies.p.rapidapi.com/"

headers = {
    "X-RapidAPI-Key": "92a745b94emsh0cb338c535b85eap183d4ajsn2e683d429da5",
    "X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

def home(request):

    
    if request.user.is_authenticated:
        user = User.objects.get(username = request.user.username)
        user = User.objects.get(username = request.user.username)
        liked_movies = Liked_Movies.objects.filter(user=user)
        liked = []
        print(response.json())
        print(type(response.json()))
        for movie in liked_movies:
            liked.append(movie.movie_id)
        print('movies',liked)
        
        return render(request, 'home.html',{'movies':response.json(),'user':user,'liked_movies': liked})
    
    
    return render(request, 'home.html',{'movies':response.json(),'user':'none'})



def favorite(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        liked_movies = Liked_Movies.objects.filter(user = user)
        liked = []
        liked_list = []
        for movie in liked_movies:
            liked_list.append(movie.movie_id)
            for m in response.json():
                if m['id'] == movie.movie_id:
                    liked.append(m)
                    
        print(liked_list)
        print('movies',liked)
        return render(request, 'favorite.html',{'movies':liked,'user':user,'liked_movies': liked_list})
    return redirect('/')

    


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
        
        user = User(username = username,email = email, password = password )
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