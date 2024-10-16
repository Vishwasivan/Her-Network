from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.loginhome,name='login'),
    path('login/index/',views.indexpage,name='index'),
]
