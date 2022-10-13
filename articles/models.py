from email.mime import image
from email.policy import default
from email.quoprimime import body_check
from django.db import models
from django.contrib.auth.models import User

#make migrations
#migrate - to database
class Article(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.png",blank=True)
    author  =  models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    
    #display the query
    def __str__(self):
        return self.title 

    def snippet(self):
        if (len(self.body)>50):
            return self.body[:50] + "..."
        else: return self.body
