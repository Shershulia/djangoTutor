from http.client import HTTPResponse
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

def article_list(request):
    article = Article.objects.all().order_by("date")
    return render(request, 'articles/article_list.html',{'articles':article})

def article_detail(request,slug):
    return HttpResponse(slug)

