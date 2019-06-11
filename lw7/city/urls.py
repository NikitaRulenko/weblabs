from django.urls import path

from .views import CityView
from . import views


app_name = "cities"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('cities/', CityView.as_view()),
    path('cities/<int:pk>', CityView.as_view())
]