from tkinter import Menu
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('menu/', include('menu.urls')),
    path('', views.index),
]