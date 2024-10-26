from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserLoginForm, RegistrationForm

# Create your views here.
def user_registration(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('user_login')
    else:
        register_form = RegistrationForm()

    return render(request, 'user_account/user_registration.html', {'register_form': register_form, 'type': 'Register'})
    

def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, request.POST)
        if form.is_valid():
        # get the form data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print('The USER is:', user)
            # check if the user is valid
            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                return redirect('user_login')
    else:
        form = CustomUserLoginForm()
        return render(request, 'user_account/user_login.html', {'form': form, 'type': 'Login'})
    
def user_logout(request):
    logout(request)
    return redirect('homepage')
