"""
URL configuration for webproject project.

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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', views.tranchu, name='trangchu'),
    path('vechungto/', views.vechungto, name='vechungto'),
    path('bosuutap/', views.bosuutap, name='bosuutap'),
    path('workshop/', views.workshop, name='workshop'),
    path('installation/', views.installation, name='installation'),
    path('thietke/', views.thietke, name='thietke'),
    path('giohang/', views.giohang, name='giohang'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('user/', include('user.urls')), 
]