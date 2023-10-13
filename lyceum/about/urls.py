from django.urls import path
from . import about_views

urlpatterns = [
    path('', about_views.description)
]
