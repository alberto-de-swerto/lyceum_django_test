from django.urls import path
from . import hp_views

urlpatterns = [
    path('', hp_views.home)
]
