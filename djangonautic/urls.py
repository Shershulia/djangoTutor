from django.contrib import admin
from django.urls import path , include
from djangonautic import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls') ),
    path('about/',views.about), # ^ beginning of the address space, $ is the finish of the line
    path('',views.homepage), #whenever .com url for the home page
]

urlpatterns+= staticfiles_urlpatterns()