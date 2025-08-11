from django.shortcuts import render
from rest_framework import generics
from .models import Ticket
from .serializers import TicketSerializer
from .models import InventoryItem
from .serializers import InventoryItemSerializer

# Create your views here.
class TicketListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class InventoryItemListAPIView(generics.ListAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer