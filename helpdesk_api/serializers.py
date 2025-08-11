from rest_framework import serializers
from .models import Ticket  # Adjust if model is elsewhere
from .models import InventoryItem

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'  # or specify fields explicitly

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'location', 'bin', 'bbl', 'description']