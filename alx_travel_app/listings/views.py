# listings/views.py
from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Listing instances.
    This provides 'list', 'create', 'retrieve', 'update', 'partial_update', and 'destroy' actions.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Booking instances.
    This provides 'list', 'create', 'retrieve', 'update', 'partial_update', and 'destroy' actions.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
