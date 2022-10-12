import re
from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)  #data that will be posted
        if form.is_valid():
            form.save() #save in database 
            return redirect("articles:list") #redirect to url
    else :
        form = UserCreationForm() 
    return render(request,'accounts/signup.html',{"form":form})
