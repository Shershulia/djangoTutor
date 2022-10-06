from email.mime import image
from email.quoprimime import body_check
from django.db import models
#make migrations
#migrate - to database
class Article(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.png",blank=True)

    #display the query
    def __str__(self):
        return self.title 

    def snippet(self):
        if (len(self.body)>50):
            return self.body[:50] + "..."
        else: return self.body
