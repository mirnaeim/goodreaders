from django.urls import path
from .views import get_title

urlpatterns = [
    path('search/', get_title),
]
