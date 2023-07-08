from django.contrib import admin
from django.urls import path, include
from connections import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index.html', views.index, name='index'),
    path('connection', views.connection, name='connection'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
