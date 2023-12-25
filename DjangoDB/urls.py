from django.urls import path
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from DjangoDB import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('statuses/<int:pk>', views.StatusesDetail.as_view()),
    path('staff/', views.StaffList.as_view()),
    path('staff/<int:pk>/', views.StaffDetail.as_view()),
    path('rooms/', views.RoomsList.as_view()),
    path('rooms/<int:pk>/', views.RoomDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('client/', views.ClientReservationListView.as_view()),
    path('resrvation/', views.ReservationListView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
