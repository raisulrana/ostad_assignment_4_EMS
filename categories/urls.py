from django.urls import path, include
from .import views

urlpatterns = [
    path('add-category/', views.add_category, name='add_category'),
]