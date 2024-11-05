from django.shortcuts import render
from events.models import Event, Booking
from django.db.models import Q
from events.models import Event, Category


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


def search_view(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', None)
    if query:
        events = Event.objects.filter(
            Q(title__icontains=query) |
            Q(category__name__icontains=query) |
            Q(event_created_at__icontains=query) |
            Q(location__icontains=query)
        ).distinct()
    elif category_id:
        events = Event.objects.filter(category_id=category_id)
    else:
        events = Event.objects.all()

    categories = Category.objects.all()  # Retrieve categories again for the template
    
    return render(request, 'index.html', {'events': events, 'categories': categories})