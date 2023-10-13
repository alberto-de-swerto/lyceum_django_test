from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# from catalog import cat_views
# from homepage import hp_views
# from about import about_views

urlpatterns = [
    path('', include('homepage.urls')),
    path('catalog/', include('catalog.urls')),
    path('catalog/<int:pk>/', include('catalog.urls')),
    path('about/', include('about.urls')),
]
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
