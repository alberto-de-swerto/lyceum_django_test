from django.urls import path
from . import cat_views

urlpatterns = [
    path('', cat_views.item_list),
    path('<int:pk>/', cat_views.item_detail)
]
