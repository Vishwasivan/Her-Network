from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Login_detail, Post, Author
from django.contrib.auth.decorators import login_required


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
    print(request.POST)
    if request.method=='POST':
        email=request.POST['Uemail']
        password=request.POST['Upsw']
        if Login_detail.objects.filter(email=email,password=password).exists():
            login=Login_detail.objects.get(email=email)
            if login.role=='Housewife':
                return redirect(service,login.id)
            else:
                return redirect(task,login.id)
            
        else:
            messages.info(request,"cannot login") 
    return render(request,'login.html')


def indexpage(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

# @login_required(login_url='login')
def service(request,pk):
    userid=Login_detail.objects.get(id=pk)
    posts=Post.objects.all()
    context={'user':userid,'posts':posts}
    print(request.POST)
    if request.method=='POST':
        #creating the post
        if 'serviceTitle' in request.POST:
            titles=request.POST['serviceTitle']
            description=request.POST['serviceDescription']
            wskill=request.POST['skills']
            datetime=request.POST['availability']
            price=request.POST['servicePrice']
            location=request.POST['serviceLocation']
            post=Post.objects.create(titles=titles,description=description,wskill=wskill,datetime=datetime,price=price,location=location,creater=userid.id)
            post.save()
        #button for accept and reject
        if 'acceptorrejectbutton' in request.POST:
            status=request.POST['acceptorrejectbutton']
            cpost=Post.objects.get(creater=userid.id)
            if status=='accept':
                cpost.requests='accepted'
            elif status=='reject':
                cpost.requests='rejected'
            cpost.save()
    return render(request,'servicerPG.html',context)

# @login_required(login_url='login')
def task(request,pk):
    userid=Login_detail.objects.get(id=pk)
    posts = Post.objects.prefetch_related('authors').all()
    context={'user':userid,'posts':posts}
    print(request.POST)
    if request.method=='POST':
        servicerid=request.POST['req']
        poster=Post.objects.get(id=servicerid)
        author1=Author.objects.create(requests=pk)
        poster.authors.add(author1)

        poster.save()
        return render(request,'taskerPG.html',context)
    else:
        return render(request,'taskerPG.html',context)



# for change the name
# def proflic_change(request):
#     print(request.POST)
#     if request.method=='POST':
#         login = Login_detail.objects.get(id=17)
#         if request.POST['username']:
#             newname=request.POST['username']
#             login.name=newname
#             login.save()
#         return  render(request,'servicerPG.html')
            
    
#     return  render(request,'servicerPG.html')
            
#         password=request.POST['userPassword']