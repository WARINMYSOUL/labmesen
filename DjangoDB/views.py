from django.db.models.functions import Concat
from rest_framework import generics

from DjangoDB import models
from DjangoDB.serializers import RoomsSerializer, StatusSerializer, StaffSerializer, UserSerializer, ClientSerializer, \
    ReservationDetailsSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from django.db.models import F, Value, CharField
from DjangoDB.models import Reservations, Clients, Rooms, Staff


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StatusesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Statuses.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StaffList(generics.ListCreateAPIView):
    queryset = models.Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RoomsList(generics.ListCreateAPIView):
    queryset = models.Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClientReservationListView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = models.Clients.objects.filter(reservations__isnull=False).distinct()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReservationListView(generics.ListAPIView):
    serializer_class = ReservationDetailsSerializer

    def get_queryset(self):
        # Здесь вставьте ваш запрос
        queryset = (
            models.Reservations.objects
            .select_related('client', 'room', 'staff')
            .annotate(
                client_name=Concat('client__first_name', Value(' '), 'client__last_name', output_field=CharField()),
                staff_name=Concat('staff__first_name', Value(' '), 'staff__last_name', output_field=CharField())
            )
            .values(
                'reservation_id',
                'client_name',
                'room__room_number',
                'room__room_type',
                'room__rate',
                'staff_name'
            )
        )
        return queryset
    permission_classes = [permissions.IsAuthenticated]

