from rest_framework import generics
from DjangoDB.models import Staff, Statuses, Rooms
from .serializers import RoomsSerializer, StatusSerializer, StaffSerializer


class StatusesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Statuses.objects.all()
    serializer_class = StatusSerializer


class StaffList(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class RoomsList(generics.ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer

