from django.contrib import admin
from django.urls import include, path
from  Parties import views

app_name='Parties'

urlpatterns = [
    # path('', views.parties, name='parties'),
     path('poll.html', views.poll, name='poll'), 
    
]
