from django.contrib import admin
from django.urls import path
from articles import views


urlpatterns = [
    path('',views.article_list), #whenever .com url for the home page
]
