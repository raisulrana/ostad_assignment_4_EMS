from django.urls import path, include
from .import views

urlpatterns = [
    # path('', views.homepage, name='homepage'),
    path('add-event/', views.add_event, name='add_event'),
    path('edit-event/<int:id>', views.edit_event, name='edit_event'),
    path('delete-event/<int:id>', views.delete_event, name='delete_event'),
]