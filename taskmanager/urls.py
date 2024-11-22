from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('taskmanagermain.urls')),
    path('accounts/',include('allauth.urls')),
]
