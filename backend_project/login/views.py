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


def service(request,pk):
    userdetail=Login_detail.objects.all()
    userid=Login_detail.objects.get(id=pk)
    posts=Post.objects.all()
    auth = Author.objects.all()
    context={'userdetail':userdetail,'user':userid,'posts':posts,'authors':auth}
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
            author = Author.objects.create(creater=pk, requests=0, status='none')
            post=Post.objects.create(titles=titles,description=description,wskill=wskill,datetime=datetime,price=price,location=location,creater=userid.id,authors=author)
            post.save()
        #button for accept and reject
        if 'acceptorrejectbutton' in request.POST:
            req=request.POST['requestid']
            stat=request.POST['acceptorrejectbutton']
            spost=Post.objects.get(creater=userid.id)
            reqid=int(req)
            # statid=int(stat)
            if stat=='accept':
                author1=Author.objects.get(requests=reqid)
                author1.status='accepted'
                spost.accepter=reqid
                author1.save()
            elif stat=='reject':
                author1=Author.objects.get(requests=reqid)
                author1.status='rejected'
                spost.authors.add(author1)
            spost.save()
        if 'userName' in request.POST:
            newname=request.POST['userName']
            newpassword=request.POST['userPassword']
            newlocation=request.POST['userLocation']
            if newname!='':
                userid.name=newname
            if newpassword!='':
                userid.password=newpassword
            if newlocation!='':
                userid.location=newlocation
            userid.save()    
    return render(request,'servicerPG.html',context)


def task(request,pk):
    userdetail=Login_detail.objects.all()
    userid=Login_detail.objects.get(id=pk)
    posts = Post.objects.all()
    auth = Author.objects.all()
    context={'userdetail':userdetail,'user':userid,'posts':posts,'authors':auth}
    print(request.POST)
    if request.method=='POST':
        if 'req' in request.POST:
            servicerid=request.POST['req']
            createrid=request.POST['createrid']
            poster=Post.objects.get(id=servicerid)
            author = Author.objects.create(creater=createrid,requests=pk,status='request sended')
            poster.authors=author
            poster.save()
        if 'userName' in request.POST:
            newname=request.POST['userName']
            newpassword=request.POST['userPassword']
            newlocation=request.POST['userLocation']
            if newname!='':
                userid.name=newname
            if newpassword!='':
                userid.password=newpassword
            if newlocation!='':
                userid.location=newlocation
            userid.save() 
       
        
    
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