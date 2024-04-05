from django.contrib import admin
from django.urls import include, path
from  Registeration import views

app_name='Registeration'

urlpatterns = [
    # path('', views.Register, name='Register'),
    path('register.html', views.register, name='register'),    
    path('login.html',views.user_login,name='user_login'),
     path('logout_user', views.logout_user, name='logout_user'),

    
    
]
