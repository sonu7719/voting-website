from django.http import HttpResponse
from django.shortcuts import render
from voting_home import views
from voting_home.models import Feedback
# Create your views here.
def home (request):
    # return HttpResponse("this is my voting home page")
    return render(request,'index.html')

def feed(request):
    if request.method=='POST':
             feedback = Feedback()
             name = request.POST.get('First_name')
             email = request.POST.get('Email')
             Age= request.POST.get('Age')
             message= request.POST.get('Content')
             feedback.First_name=name
             feedback.Email=email
             feedback.Age=Age
             feedback.Content=message
             feedback.save()
             return HttpResponse("Response  Succesfully Recored")
    return render (request,'feedback.html') 

# def register (request):
#     # return HttpResponse("this is my voting home page")
#     return render(request,'register.html')

# def poll (request):
#     return render (request,'poll.html')

# def login(request):
#     return render(request,'login.html')


