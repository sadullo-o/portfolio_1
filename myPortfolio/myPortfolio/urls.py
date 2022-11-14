"""myPortfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from main.views import *
from .settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/', About.as_view(), name='about'),
    path('myworks/', MyWorks.as_view(), name='myworks_url'),
    path('contact/', contact, name='contact'),
    path('login/', login_page, name='login'),
    path('register/', register, name='register'),
    path('logout', logout_users, name='logout'),
    path('blog', blog, name='blog'),
    path('search', search, name='search'),
    # path('search2', Search.as_view(), name='search'),
    path('profile', profile, name='profile'),
    path('edit', edit, name='edit'),

]


if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)