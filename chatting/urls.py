from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.hello, name='hello_world'),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name='home'),
    path('chat',views.chat,name="chat"),
    path('signin',views.handlelogin,name='login'),
    path('logout',views.handlelogout,name='logout'),
    path('chatbot',views.chatbot,name='chatbot'),
   #path('home',views.home,name='home'),
]