from django.shortcuts import render

def homepage(request):
    context = {
        'title': 'Home',
        'page_heading': 'Welcome to Event Management System',
    }
    return render(request, 'index.html', context)