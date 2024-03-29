"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.shortcuts import render

def home(request):
    # your view logic here
    return render(request, 'home.html')  # adjust the template name as needed


def home(request):

    return render(request, 'base.html')  # adjust the template name as needed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/',home ,name = 'home'),
    path('', include('Post.urls', namespace="post")),
    path('profile/', include('allauth.urls')),
    path('ads/', include('advert.urls', namespace="advert")),
    path('comment/', include('Comment.urls', namespace="comment")),
]
