"""
URL configuration for labmesen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from labmesen.views import StaffList, StaffDetail, StatusesDetail, RoomDetail, RoomsList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('statuses/<int:pk>', StatusesDetail.as_view()),
    path('staff/', StaffList.as_view()),
    path('staff/<int:pk>/', StaffDetail.as_view()),
    path('rooms/', RoomsList.as_view()),
    path('rooms/<int:pk>/', RoomDetail.as_view()),
]