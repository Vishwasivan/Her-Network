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
    
    
from django.db import models
from django.utils.timezone import now, timedelta
import uuid

class AadhaarVerification(models.Model):
    aadhaar_number = models.CharField(max_length=12)
    mobile_number = models.CharField(max_length=10)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_sent_at = models.DateTimeField(blank=True, null=True)
    verified = models.BooleanField(default=False)
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(default=now)
    file = models.FileField(upload_to='uploads/')
    
   
    otp_expiry_time = models.DateTimeField(blank=True, null=True)
    
    def set_otp_expiry(self):
        # Set the expiry time to 5 minutes from now
        self.otp_expiry_time = now() + timedelta(minutes=5)
        self.save()