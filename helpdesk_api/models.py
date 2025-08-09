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