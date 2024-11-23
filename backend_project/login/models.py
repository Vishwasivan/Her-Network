from django.db import models
from django.core.validators import MaxValueValidator
from datetime import datetime

# Create your models here.
class Login_detail(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    number = models.IntegerField(default=False,validators=[MaxValueValidator(10)])
    role = models.CharField(max_length=10)
    skill = models.CharField(max_length=10)
    password = models.CharField( max_length=50,)
    location = models.CharField( max_length=50,default='none',null=True,blank=True)
    

class Author(models.Model):
    creater = models.IntegerField(default=0,blank=True)
    requests = models.IntegerField(default=0,blank=True)
    status = models.CharField(default='null',max_length=50,blank=True)
    

class Post(models.Model):
    titles = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    wskill = models.CharField(max_length=30)
    datetime = models.DateTimeField()
    price = models.FloatField()
    location = models.CharField(max_length=50)
    authors = models.ForeignKey(Author,on_delete=models.CASCADE)
    accepter = models.IntegerField(default=0,blank=True)
    creater = models.IntegerField(default=0,blank=True)
    
    
