from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    capacity = models.PositiveBigIntegerField(default=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, null=True, blank=True)
    event_created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    event_updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    event_ended_at = models.DateTimeField(null=True, blank=True)

    def is_fully_booked(self):
        return self.bookings.count() >= self.capacity
    
    def seats_left(self):
        return self.capacity - self.bookings.count()
    
    def __str__(self):
        return self.title
    

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    booked_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username} booked {self.event.title}"
    
    class Meta:
        unique_together = ('event', 'user')  # Prevents duplicate bookings for the same event by the same user