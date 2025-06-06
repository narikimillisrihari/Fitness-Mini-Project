from django.shortcuts import render
from rest_framework import generics,status
from booking.models import Fitness,Book
from rest_framework.response import Response
from booking.serializers import FitnessSerializers,BookSerializer
from django.utils.timezone import now
import pytz
# Create your views here.
class FitnessAPIView(generics.ListAPIView):
    serializer_class=FitnessSerializers
    def get_queryset(self):
        return Fitness.objects.filter(date_time__gte=now()).order_by('date_time')

class BookingAPIView(generics.CreateAPIView):
    serializer_class=BookSerializer

    def create(self, request, *args, **kwargs):
        class_id = request.data.get('class_id')
        client_name=request.data.get('client_name')
        client_email=request.data.get('client_email')
        # if class_id or not client_name or not client_email:
        #     return Response({'error':'missing the field values'},status=status.HTTP_400_BAD_REQUEST)
        if not all([class_id, client_name, client_email]):
            return Response({"error": "All fields are required"}, status=400)

        try:
            fitness_class = Fitness.objects.get(id=class_id)
        except Fitness.DoesNotExist:
            return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)

        if fitness_class.available_slots<0:
            return Response({'error':'No avaliable slots'},status=status.HTTP_400_BAD_REQUEST)
        
        booking = Book.objects.create(
            fitness_class=fitness_class,
            client_name=client_name,
            client_email=client_email
        )

        # Reduce available slots
        fitness_class.available_slots -= 1
        fitness_class.save()

        return Response(BookSerializer(booking).data, status=status.HTTP_201_CREATED)
    
class BookingListbyEmailAPIView(generics.ListAPIView):
    serializer_class=BookSerializer
    def get_queryset(self):
        email=self.request.query_params.get('email')
        if email:
            return Book.objects.filter(client_email=email)
        return Book.objects.none()
