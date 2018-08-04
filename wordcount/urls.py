

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='home'),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about')
]
