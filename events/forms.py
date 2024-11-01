from django import forms
from .models import Event


common_css_class = "bg-gray-50 border border-black-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        # fields = '__all__'
        fields = ['title', 'description', 'category', 'author_event', 'location']

    title = forms.CharField(widget=forms.TextInput(attrs={'class': common_css_class}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': common_css_class}))
    category = forms.CharField(widget=forms.TextInput(attrs={'class': common_css_class}))
    author_event = forms.CharField(widget=forms.TextInput(attrs={'class': common_css_class}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': common_css_class}))