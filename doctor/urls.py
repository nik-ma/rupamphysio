#created by nikhil
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='homepage'),
    path('appointment',views.appointment,name='appointment'),
    path('help',views.help,name='help'),
    
]