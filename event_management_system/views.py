from django.shortcuts import render
from events.models import Event, Booking

# def homepage(request):
#     # Retrieve all events
#     events = list(Event.objects.all())  # Convert QuerySet to a list of Event instances

#     # Get a set of event IDs that the user has booked
#     user_booked_events = set(Booking.objects.filter(user=request.user).values_list('event_id', flat=True))
    
#     # Annotate each event with a flag if the user has already booked it
#     for event in events:
#         event.user_has_booked = event.id in user_booked_events

#     return render(request, 'index.html', {'events': events})

def homepage(request):
    # Retrieve all events
    events = list(Event.objects.all())  # Convert QuerySet to a list of Event instances

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Get a set of event IDs that the user has booked
        user_booked_events = set(Booking.objects.filter(user=request.user).values_list('event_id', flat=True))
        
        # Annotate each event with a flag if the user has already booked it
        for event in events:
            event.user_has_booked = event.id in user_booked_events
    else:
        # For unauthenticated users, set `user_has_booked` to False for all events
        for event in events:
            event.user_has_booked = False

    return render(request, 'index.html', {'events': events})