from . import views
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    url(r'^artists/', views.ArtistList.as_view())
]