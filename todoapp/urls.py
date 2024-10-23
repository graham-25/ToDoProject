from django.urls import path
from . import views

urlpatterns = [
    #declareing all our urls and urlpattens
    path('', views.home, name='home-page'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
]