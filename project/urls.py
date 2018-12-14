"""inventaire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from materials.views import HardwareList, HardwareUpdateComplete, HardwareUpdateLight, HardwareDelete, HardwareCreate
from accounts.views import UserList, UserUpdate, UserDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', HardwareList.as_view()),
    path('create/', HardwareCreate.as_view(), name="hardware-create"),
    path('edit/<int:pk>', HardwareUpdateLight.as_view()),
    path('edit/complete/<int:pk>', HardwareUpdateComplete.as_view()),
    path('delete/<int:pk>', HardwareDelete.as_view()),

    path('users/', UserList.as_view()),
    path('users/edit/<int:pk>', UserUpdate.as_view()),
    path('users/delete/<int:pk>', UserDelete.as_view())

]
