from django.contrib import admin
from django.urls import include, path
from  result import views
app_name='result'


urlpatterns = [
    path('', views.result, name='result'),
    path('vote.html', views.voting, name='vote'),
    
    
]
