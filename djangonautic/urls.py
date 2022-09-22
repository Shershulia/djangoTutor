from django.contrib import admin
from django.urls import path
from djangonautic import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.about), # ^ beginning of the address space, $ is the finish of the line
    path('',views.homepage), #whenever .com url for the home page
]
