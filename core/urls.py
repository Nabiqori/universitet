"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mainapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('fanlar/', fanlar_view),
    path('yonalishlar/', yonalishlar_view),
    path('ustozlar/', ustozlar_view),
    path('yonalish_qoshish/', yonalishlar_qoshish_view),
    path('fan_qoshish/', fanlar_qoshish_view),
    path('ustoz_qoshish/', ustoz_qoshish_view, name='ustoz_qoshish'),
    path('fanlar/<int:pk>/tahrirlash/',fan_update_view),
    path('yonalishlar/<int:pk>/tahrirlash/',yonalish_update_view),
    path('ustozlar/<int:pk>/tahrirlash/',ustoz_update_view),
]
