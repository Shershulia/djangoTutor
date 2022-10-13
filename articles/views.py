from http.client import HTTPResponse
from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(request):
    articles = Article.objects.all().order_by("date")
    return render(request, 'articles/article_list.html',{'articles':articles})

def article_detail(request,slug):
    #return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request,"articles/article_detail.html",{'article':article})

@login_required(login_url="/accounts/login/") #protection for login 
def article_create(request):
    if (request.method == "POST"):
        form=forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            #save to the database
            instance = form.save(commit=False)
            instance.author = request.user #initialise user who wrote the article
            instance.save()
            return redirect("articles:list")
    else:
        form=forms.CreateArticle()

    return render(request,"articles/create.html", {"form":form}) #3rd parameter - sending to html

