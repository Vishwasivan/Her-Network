from django.urls import path
from . import views



urlpatterns = [
    path('',views.indexpage,name='index'),
    path('login/',views.login,name='login'),
    path('login/signup/',views.signuppage,name='signup'),
    path('service/<str:pk>',views.service,name='service'),
    path('task/<str:pk>',views.task,name='task'),
    path("verify-aadhaar-mobile/", views.verify_aadhaar_mobile, name="verify_aadhaar_mobile"),
    path("verify-otp/", views.verify_otp, name="verify_otp"),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
