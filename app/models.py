from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Liked_Movies(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    movie_id = models.CharField(max_length=50)
    
class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    
    def __str__(self):
        return self.name