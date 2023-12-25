from rest_framework import serializers
from DjangoDB import models

from django.contrib.auth.models import User

owner = serializers.ReadOnlyField(source='owner.username')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Statuses
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = '__all__'


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rooms
        fields = '__all__'


class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clients
        fields = ('first_name', 'last_name', 'email')


class ReservationDetailsSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='get_client_name', read_only=True)
    room_number = serializers.IntegerField(source='room__room_number')  # Update this line
    room_type = serializers.CharField(source='room__room_type')  # Update this line
    rate = serializers.DecimalField(max_digits=10, decimal_places=2, source='room__rate')  # Update this line
    staff_name = serializers.CharField(source='get_staff_name', read_only=True)

    class Meta:
        model = models.Reservations
        fields = ('reservation_id', 'client_name', 'room_number', 'room_type', 'rate', 'staff_name')