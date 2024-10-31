from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    event_author = models.ForeignKey(User, on_delete=models.CASCADE)
    event_created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    event_updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    event_ended_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title