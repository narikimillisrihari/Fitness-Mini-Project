from rest_framework import serializers
from booking.models import Fitness,Book

class FitnessSerializers(serializers.ModelSerializer):
    class Meta:
        model=Fitness
        fields="__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"