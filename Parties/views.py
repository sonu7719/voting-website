from django.http import HttpResponse
from django.shortcuts import render
from Parties.models import parties
from Registeration import views
# Create your views here.
# def parties (request):
#     return HttpResponse("this is parties page")

def poll (request):
    if request.method=='POST':
            Partie_ino = parties()
            name = request.POST.get('Party_name')
            email = request.POST.get('Partie_Email')
            sponser=request.POST.get('sponser')
            Partie_no= request.POST.get('Partie_no')
            Leader=request.POST.get('Leader')
            Partie_ino.Party_name=name
            Partie_ino.Partie_Email=email
            Partie_ino.sponser=sponser
            Partie_ino.Partie_no=Partie_no
            Partie_ino.Leader=Leader
            Partie_ino.save()
            return HttpResponse("Partie Register Succesfully will be Displayed Soon")

    return render (request,'poll.html')
