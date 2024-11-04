from django import forms
from .models import Event
from categories.models import Category


common_css_class = "bg-gray-50 border border-black-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'category', 'location']

    title = forms.CharField(widget=forms.TextInput(attrs={'class': common_css_class}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': common_css_class}))
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': common_css_class}),
        required=True
    )
    # event_user = forms.CharField(widget=forms.TextInput(attrs={'class': common_css_class}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': common_css_class}))