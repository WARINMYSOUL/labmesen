from rest_framework import serializers
from DjangoDB.models import Staff, Statuses, Rooms


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'