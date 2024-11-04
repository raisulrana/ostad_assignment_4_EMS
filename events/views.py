from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Category
from django.http import HttpResponseForbidden
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

# @login_required
# def edit_event(request, id):
#     edit_event = get_object_or_404(Event, pk=id)
    
#     # Check if the user is the creator or an admin
#     if request.user != edit_event.created_by and not request.user.is_staff:
#         return HttpResponseForbidden("You do not have permission to edit this event.")

#     if request.method == 'POST':
#         event_form = EventForm(request.POST, instance=edit_event)
#         if event_form.is_valid():
#             event_form.save()
#             return redirect('homepage')
#     else:
#         event_form = EventForm(instance=edit_event)
    
#     return render(request, 'events/add_event.html', {'form': event_form})

@login_required
def delete_event(request, id):
    delete_event = Event.objects.get(pk=id)
    delete_event.delete()
    
    return redirect ('homepage')