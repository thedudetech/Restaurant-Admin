from django.shortcuts import render
from django.http import HttpResponse
from users.models import Users
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from foodadmin import templates

# Create your views here.
def login(request):
    msg ='invalid'
    if request.method == 'POST':
        print("Inside login  Post")
        email = request.POST['email']
        password = request.POST['password']
        m = Users.objects.get(email=request.POST['email'])
        request.session['user_id'] = m.id
        checkuser = Users.objects.filter(email=email)
        if checkuser:
            pswd = Users.objects.filter(email=email,password=password)    
            if pswd:
                request.session['user_id'] = m.id
                request.session['email'] = m.email
                return render(request, 'index.html')
            else:

                return render(request, 'page-login.html',{'name' : email} )
        else:
            return render(request, 'page-login.html',msg)

    return render(request, 'page-login.html')

def register(request):
    if request.method == 'POST':
        print("Inside Register Post")
        user_name = request.POST['user_name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        dob = request.POST['dob']
        photo = request.POST['pic']
        password = request.POST['password']     

        print(user_name)
        print(email)
        print(mobile)
        print(dob)
        print(photo)
        print(password)
        b = Users(user_name=user_name, email=email,mobile=mobile, dob=dob, photo=photo, password=password)
        b.save()
        return render(request, 'page-login.html')
    return render(request, 'page-register.html')