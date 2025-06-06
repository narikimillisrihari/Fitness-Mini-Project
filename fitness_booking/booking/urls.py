from django.urls import path
from booking.views import BookingAPIView,BookingListbyEmailAPIView,FitnessAPIView
urlpatterns = [
    path('classes/', FitnessAPIView.as_view(),name="class_list"),
    path('book/', BookingAPIView.as_view(), name='book-class'),
    path('bookings/',BookingListbyEmailAPIView.as_view(),name="booking-by-email"),
]