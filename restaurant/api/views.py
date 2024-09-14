from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer

class MenuItemViewSet(ModelViewSet):
    """
    ViewSet for viewing and editing MenuItem instances.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
    """
    ViewSet for viewing and editing Booking instances.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  # Ensures that only authenticated users can access this viewset
