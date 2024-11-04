from django.shortcuts import render, redirect
from .models import Event, Category
from .forms import EventForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event = event_form.save(commit=False)  # Use a different variable for the instance
            event.created_by = request.user
            event.save()
            event_form.save_m2m()  # This works because `event_form` is still the form instance
            print("Redirecting to homepage...")
            return redirect('homepage')
        else:
            print('Error in form submission:', event_form.errors)
    else:
        event_form = EventForm()
    
    return render(request, 'events/add_event.html', {'form': event_form})
        

@login_required
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
    else:
        event_form = EventForm()
        
    return render(request, 'add_event.html',{'form': event_form})

@login_required
def delete_event(request, id):
    delete_event = Event.objects.get(pk=id)
    delete_event.delete()
    
    return redirect ('homepage')