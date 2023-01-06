from django.urls import path,include
from app import views

urlpatterns = [
    path('', views.home),
    path('signin/',include('allauth.urls')),
    path('site_actions/',views.ajax_actions, name = 'ajax_actions')
]
