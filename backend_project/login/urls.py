from django.urls import path
from . import views



urlpatterns = [
    path('index/login/',views.loginpage,name='login'),
    path('index/',views.indexpage,name='index'),
    path('ud/',views.userdashboard,name='ud'),
]