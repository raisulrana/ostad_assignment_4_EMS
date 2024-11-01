from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile



input_class = "bg-gray-50 border border-black-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'mailing_address', 'image']
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class': input_class, 'id':'required', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': input_class, 'id':'required', 'placeholder': 'First Name'}))
    middle_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': input_class, 'id':'required', 'placeholder': 'Middle Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': input_class, 'id':'required', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': input_class, 'id':'required', 'placeholder': 'Email Address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': input_class, 'id':'required', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': input_class, 'id':'required', 'placeholder': 'Confirm Password'}))
    mailing_address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': input_class, 'id':'required', 'placeholder': 'Address'}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': input_class, 'id':'required', 'placeholder': 'Upload Profile Picture'}))


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()

            # Check if the user already has a UserProfile
            try:
                profile = UserProfile.objects.get(user=user)
            except UserProfile.DoesNotExist:
                # If no profile exists, create a new one
                profile = UserProfile.objects.create(
                    user=user,
                    username=user.username,
                    first_name=user.first_name,
                    middle_name=user.middle_name,
                    last_name=user.last_name,
                    email_address=user.email,
                    phone_number=user.phone_number,
                    mailing_address=self.cleaned_data['mailing_address'],
                    image=self.cleaned_data['image'] if 'image' in self.cleaned_data else None
                )
            else:
                # If profile exists, update the fields
                profile.username = user.username
                profile.first_name = user.first_name
                profile.last_name = user.last_name
                profile.email_address = user.email
                profile.mailing_address = self.cleaned_data['mailing_address']
                if 'image' in self.cleaned_data and self.cleaned_data['image']:
                    profile.image = self.cleaned_data['image']
            profile.save()
        
        return user



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'middle_name', 'last_name', 'email_address', 'phone_number', 'mailing_address', 'image']



class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField( widget=forms.TextInput(attrs={'class': input_class, 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': input_class, 'placeholder': 'Password'}))