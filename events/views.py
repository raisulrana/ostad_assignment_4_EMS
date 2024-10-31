from django.shortcuts import render, redirect
from .models import Event, Category
from .forms import EventForm

# Create your views here.
def add_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return redirect('add_event')
        
    else:
        event_form = EventForm()
        
    return render(request, 'events/add_event.html',{'form': event_form})


def edit_event(request, id):
    edit_event = Event.objects.get(pk=id)
    event_form = EventForm(instance=edit_event)
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return redirect('add_event')
        
    else:
        event_form = EventForm()
        
    return render(request, 'add_event.html',{'form': event_form})


def delete_event(request, id):
    delete_event = Event.objects.get(pk=id)
    delete_event.delete()
    
    return redirect ('homepage')