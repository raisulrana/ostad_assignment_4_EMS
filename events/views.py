from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Category
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden
from .models import Event, Booking

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
            return redirect('homepage')
        else:
            print('Error in form submission:', event_form.errors)
    else:
        event_form = EventForm()
    
    return render(request, 'events/add_event.html', {'form': event_form})
        

@login_required
def edit_event(request, id):
    edit_event = Event.objects.get(pk=id)

    if request.method == 'POST':
        event_form = EventForm(request.POST, instance=edit_event)
        if event_form.is_valid():
            event_form.save()
            return redirect('homepage')
    else:
        event_form = EventForm(instance=edit_event)
        
    return render(request, 'events/edit_event.html',{'form': event_form})


@login_required
def delete_event(request, id):
    delete_event = Event.objects.get(pk=id)
    delete_event.delete()
    
    return redirect ('homepage')


@login_required
def book_event(request, id):
    event = get_object_or_404(Event, pk=id)
    
    # Check if the user is the event creator
    if request.user == event.created_by:
        return HttpResponseForbidden("You cannot book your own event.")
    
    # Check if the user has already booked this event
    if Booking.objects.filter(event=event, user=request.user).exists():
        return HttpResponse("You have already booked this event.")
    
    # Create a booking record
    Booking.objects.create(event=event, user=request.user)
    return redirect('homepage')  # Redirect to a confirmation page if needed


@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'events/user_bookings.html', {'bookings': bookings})
