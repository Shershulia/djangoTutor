from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login 

# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)  #data that will be posted
        if form.is_valid():
            user = form.save() #save in database 
            login(request,user)
            return redirect("articles:list") #redirect to url
    else :
        form = UserCreationForm() 
    return render(request,'accounts/signup.html',{"form":form})

def login_view(request):
    if request.method == "POST":
        form= AuthenticationForm(data = request.POST)
        if form.is_valid():
            #log in user
            user = form.get_user()
            login(request,user)
            return redirect("articles:list") #redirect to url
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{"form":form})    
