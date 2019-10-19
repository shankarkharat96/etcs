from django.urls import path
from django.conf.urls import  url
from . import views

urlpatterns = [

				       path('',views.login,name='login'),  
               url(r'^SELECT.html$', views.SELECT, name='SELECT'),    
               url(r'^MAP.html$', views.MAP, name='MAP'),
               
               
               
               
                                          ]
