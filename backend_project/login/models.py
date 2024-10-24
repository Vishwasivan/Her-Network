from django.db import models
from django.core.validators import MaxValueValidator

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
    requests = models.CharField(default='post',max_length=50,null=True,blank=True)
    
    

class Post(models.Model):
    titles = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    wskill = models.CharField(max_length=30)
    datetime = models.DateTimeField()
    price = models.FloatField()
    location = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    accepter = models.CharField(max_length=50,default='unknown')
    creater = models.CharField(max_length=50,default='unknown')
    
