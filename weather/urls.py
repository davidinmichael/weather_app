from django.urls import path
from .views import *

app_name = "weather"

urlpatterns = [
    path("", weather_home, name="home")
]
