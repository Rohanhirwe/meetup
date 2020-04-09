from django.contrib import admin
from django.urls import path,include
from . import views

app_name='home'
urlpatterns = [
    path('',views.index, name='index'),
    path('register/',views.register, name='register'),
    path('login/',views.user_login, name='login'),
    path(r'^logout/$', views.user_logout, name='logout'),
    path(r'^special/',views.special,name='special'),
]