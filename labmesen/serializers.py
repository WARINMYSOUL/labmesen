from rest_framework import serializers
from DjangoDB import models


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
