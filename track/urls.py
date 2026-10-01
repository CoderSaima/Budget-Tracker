from django.urls import path
from track import views

urlpatterns = [
    path("", views.trackbudget, name="track")
]