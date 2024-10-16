from django.db import models

# Create your models here.
class Login_detail(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    role = models.CharField(max_length=10)
    skill = models.CharField(max_length=10)
    password = models.CharField( max_length=50,)

#class Sign_in(models.Model):
    

