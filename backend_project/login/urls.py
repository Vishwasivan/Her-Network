from django.urls import path
from . import views



urlpatterns = [
    path('index/',views.indexpage,name='index'),
    path('login/',views.login,name='login'),
    path('login/signup',views.signuppage,name='signup'),
    
    
    #
    path('home/',views.service,name='home'),
    path('inde/',views.s3,name='index3'),
]