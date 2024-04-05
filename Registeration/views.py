from django.http import HttpResponse
from django.shortcuts import render, redirect
from Registeration import views
from Registeration.models import Register
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# def Register (request):
#     return HttpResponse("this is Registeration  page")

def register (request):
    if request.method=='POST':
             register_user = Register()
             user = User()
             name = request.POST.get('First_Name')
             email = request.POST.get('Email')
             con_pass=request.POST.get('Confirm_Password')
             Password= request.POST.get('Password')
             ad_no=request.POST.get('Adhar_no')

             user.username = email
             user.first_name = name
             user.email = email
             user.set_password(Password)
             user.save()
             register_user.First_Name=name
             register_user.Email=email
             register_user.Confirm_Password=con_pass
             register_user.Password=Password
             register_user.Adhar_no=ad_no
             register_user.save()
             return redirect('login.html')
            #  return HttpResponse("Data Inserted Succesfully")
    # return HttpResponse("this is my voting home page")
    return render(request,'register.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        print(email, password)
        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            print('*******successfully login*******')  # Redirect to the dashboard page after successful login
            return render(request, 'index.html')
            # return HttpResponse('User login')
        else:
             return HttpResponse('Login Failed')
    else:
        return render(request, 'login.html')
#     from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from django.contrib import messages

def logout_user(request):
    logout(request)
    return render(request, 'index.html')
    

