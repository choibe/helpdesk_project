from django.contrib import admin
from .models import Ticket
from .models import InventoryItem

# Register your models here.
@admin.register(Ticket)  # lets you manage tickets via the admin web interface
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'created_at')
    ordering = ('-created_at',)

admin.site.register(InventoryItem)