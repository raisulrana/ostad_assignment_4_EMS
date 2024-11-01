from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserLoginForm, RegistrationForm
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_registration(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return redirect('user_login')
    else:
        register_form = RegistrationForm()

    return render(request, 'user_account/user_registration.html', {'register_form': register_form, 'type': 'Register'})


def user_profile(request, username):
    try:
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(user=user)
        return render(request, 'user_account/user_profile.html', {'user_profile': user_profile, 'person': user})
    except User.DoesNotExist:
        logout(request)
        return render(request, 'user_account/not_found.html')


@login_required
def update_user_profile(request, username):
    try:
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(user=user)

        if request.method == 'POST':
            update_profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            context = {'update_profile_form': update_profile_form, 'user_profile': user_profile, 'person': user}
            if update_profile_form.is_valid():
                update_profile_form.save()
                return redirect('user_profile', username=user.username)
            else:
                return render(request, 'user_account/update_user_profile.html', context)
        else:
            update_profile_form = UserProfileForm(instance=user_profile)
            context = {'update_profile_form': update_profile_form, 'user_profile': user_profile, 'person': user}
            return render(request, 'user_account/update_user_profile.html', context)
    except User.DoesNotExist:
        logout(request)
        return render(request, 'user_account/not_found.html')


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
