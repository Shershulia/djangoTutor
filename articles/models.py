from email.quoprimime import body_check
from django.db import models
#make migrations
class Article(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    #display the query
    def __str__(self):
        return self.title 

