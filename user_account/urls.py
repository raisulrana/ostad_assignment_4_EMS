from . import views
from django.urls import path


urlpatterns = [
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("user-registration/", views.user_registration, name="user_registration"),
    path("profile/<str:username>", views.user_profile, name="user_profile"),
    path("update-profile/<str:username>", views.update_user_profile, name="update_user_profile"),
]
