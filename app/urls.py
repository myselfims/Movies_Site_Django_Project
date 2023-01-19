from django.urls import path,include
from app import views

urlpatterns = [
    path('', views.home),
    path('signin/',include('allauth.urls')),
    path('site_actions/',views.ajax_actions, name = 'ajax_actions'),
    path('favorite/', views.favorite , name = 'favorite'),
    path('search/',views.search, name = 'search'),
    path('popular/',views.popular, name = 'popular'),
    path('upcoming/',views.upcoming, name = 'upcoming'),
    path('top_rated/',views.top_rated, name = 'top_rated'),
    path('movie_detail/<str:id>',views.movie_detail, name = 'movie_detail'),
    path('contact/',views.contact, name = 'contact'),
    path('disclaimer/',views.disclaimer, name='disclaimer'),
]
