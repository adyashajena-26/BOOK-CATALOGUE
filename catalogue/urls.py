from django.urls import path
from .views import profile_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', profile_view, name="profile"),
]