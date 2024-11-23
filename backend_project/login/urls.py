from django.urls import path
from . import views



urlpatterns = [
    path('',views.indexpage,name='index'),
    path('login/',views.login,name='login'),
    path('login/signup/',views.signuppage,name='signup'),
    path('service/<str:pk>',views.service,name='service'),
    path('task/<str:pk>',views.task,name='task'),
]