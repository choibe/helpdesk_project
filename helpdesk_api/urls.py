from django.urls import path
from .views import TicketListCreateAPIView
from .views import InventoryItemListAPIView

urlpatterns = [
    path('tickets/', TicketListCreateAPIView.as_view(), name='ticket-list-create'),
    path('inventory/', InventoryItemListAPIView.as_view(), name='inventory-list'),
]