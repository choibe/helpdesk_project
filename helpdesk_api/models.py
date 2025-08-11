from django.db import models

# Example Ticket model
class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('open', 'Open'), ('closed', 'Closed'), ('pending', 'Pending')],
        default='open'
    )

    def __str__(self):
        return f"{self.title} ({self.status})"
    
class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    bin = models.CharField(max_length=50, blank=True, null=True)
    bbl = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name