from rest_framework import serializers
from .models import Ticket  # Adjust if model is elsewhere

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'  # or specify fields explicitly