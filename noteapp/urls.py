"""noteapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

import os
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.urls import path, include, re_path
from django.conf import settings
from django.views.generic import TemplateView
from django.views.static import serve
# serving media files in DEBUG=FALSE mode, not appropriate for production
# from django.views.static import serve
# from django.conf.urls import url

urlpatterns = [
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', user_views.logout_view, name='logout'), # using a custom logout function
    path('logout/', auth_views.LogoutView.as_view(template_name='users/login.html'), name='logout'),
    path('', TemplateView.as_view(template_name='home/base.html')),
    # re_path(r'^oauth/', serve,{'document_root': settings.MEDIA_ROOT}),
    # path('', include('home.urls')),
    # url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), # serving media files in DEBUG=FALSE mode
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    re_path(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'
        ),
]

    # Change to ads.urls
    # path('admin/', admin.site.urls),  # Keep
    # path('accounts/', include('django.contrib.auth.urls')),  # Keep
    # path('ads/', include('ads.urls')),
    # path('menu/', include('menu.urls')),
    # path('', TemplateView.as_view(template_name='home/main.html')),