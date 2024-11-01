from django.shortcuts import render
from events.models import Event

def homepage(request):
    context = {
        'title': 'Home',
        'page_heading': 'Welcome to Event Management System',
        'events': Event.objects.all(),
    }
    return render(request, 'index.html', context)