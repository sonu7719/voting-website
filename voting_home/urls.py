from django.contrib import admin
from django.urls import include, path
from  voting_home import views

app_name='voting_home'

urlpatterns = [
    path('', views.home, name='home'),
    path('index.html', views.home, name='home'),
    path('feedback.html',views.feed, name='feed')
    # path('register.html', views.register, name='register'),    
    # path('poll.html', views.poll, name='poll'), 
    # path('login.html',views.login,name='login')
]