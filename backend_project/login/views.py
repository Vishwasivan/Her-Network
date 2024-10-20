from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Login_detail


# Create your views here.
def signuppage(request):
    print("data")
    print(request.POST)
    print(request.POST.getlist('skills'))
    if (request.method=='POST'):
        name=request.POST['Uname']
        email=request.POST['Uemail']
        number=request.POST['Uphone']
        role=request.POST['role']
        skill=request.POST.getlist('skills')
        password=request.POST['Upsw']
        password2=request.POST['UCpsw']
        
        if Login_detail.objects.filter(email=email).exists():
            messages.info(request,"email already exist")
            return render(request,'signup.html')
        
        if Login_detail.objects.filter(number=number).exists():
            messages.info(request,"number already exist")
            return render(request,'signup.html')
            
        elif password!=password2:
            messages.info(request,"password does not match")
            return render(request,'signup.html')
        else:
            login = Login_detail.objects.create(name=name,email=email,number=number,role=role,skill=skill,password=password)
            login.save()
            return redirect('login')

    else:    
        return render(request,'signup.html')



def login(request):
    if request.method=='POST':
        email=request.POST['Uemail']
        password=request.POST['Upsw']
        login= authenticate(request,email=email,password=password)
        if Login_detail.objects.filter(email=email,password=password).exists():
            return redirect('index')
        else:
            messages.info(request,"cannot login") 
    return render(request,'login.html')




def indexpage(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def service(request):
    return render(request,'servicerPG.html')

def s3(request):
    return render(request,'taskerPG.html')