from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Login_detail(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    number = models.IntegerField(default=False,validators=[MaxValueValidator(10)] )
    role = models.CharField(max_length=10)
    skill = models.CharField(max_length=10)
    password = models.CharField( max_length=50,)