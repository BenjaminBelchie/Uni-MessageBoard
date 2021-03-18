"""AtlanticProject URL Configuration

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
#Importing all the views which contain the functions which are called on in the URLS list
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include 
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
#from users.views import UserListAll

#This is where URL handling occurs, if a user clicks on a button or link it will be for one of these URLS, this list contains the names of the URL extension, where it goes and what function it calls. 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    #path('user/all', UserListAll.as_view(), name='users-list'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('MessageBoard/', include('MessageBoard.urls')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
