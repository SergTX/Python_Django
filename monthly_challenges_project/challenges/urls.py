from django.urls import path
from . import views


urlpatterns = [
    path("", views.months_index),   # Empty , will be pointing to challenges
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenges, name="month-challenge")  # adding a name to use dynamically
]
