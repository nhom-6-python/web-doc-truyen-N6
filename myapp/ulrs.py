from django.contrib import admin
from django.urls import path
from . import views, views1, views2, views3
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views1.home, name='home'),
    path('truyen_id=<int:id>/', views1.doctruyen, name='doctruyen')
]