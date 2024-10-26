from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserLoginForm, RegistrationForm
from .models import UserProfile

# Create your views here.


def user_registration(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            # Create a new user profile for the user
            user_profile = UserProfile(user=user)
            user_profile.username = request.POST.get('username')
            user_profile.first_name = request.POST.get('first_name')
            user_profile.middle_name = request.POST.get('middle_name')
            user_profile.last_name = request.POST.get('last_name')
            user_profile.email_address = request.POST.get('email')
            user_profile.mailing_address = request.POST.get('mailing_address')
            if register_form.cleaned_data.get('image'):
                user_profile.image = register_form.cleaned_data.get('image')
            user_profile.save()
            return redirect('user_login')
    else:
        register_form = RegistrationForm()
    return render(request, 'user_account/user_registration.html', {'register_form': register_form, 'type': 'Register'})


# def user_registration(request):
#     if request.method == 'POST':
#         register_form = RegistrationForm(request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             return redirect('user_login')
#     else:
#         register_form = RegistrationForm()

#     return render(request, 'user_account/user_registration.html', {'register_form': register_form, 'type': 'Register'})


def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, request.POST)
        if form.is_valid():
            # get the form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            # check if the user is valid
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                return render(request, 'user_account/user_login.html', {'form': form, 'error': 'Invalid username or password', 'type': 'Login'})
        else:
            form = CustomUserLoginForm()
            return render(request, 'user_account/user_login.html', {'form': form, 'type': 'Login'})
    else:
        form = CustomUserLoginForm()
        return render(request, 'user_account/user_login.html', {'form': form, 'type': 'Login'})


def user_logout(request):
    logout(request)
    return redirect('homepage')
