"""
URL configuration.
"""
from django.contrib import admin
from django.urls import path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)

from core import views as core_views

urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        'api/health-check/',
        core_views.health_check,
        name='health-check'
    ),
    path(
        'api/schema/',
        SpectacularAPIView.as_view(),
        name='api-schema'
    ),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs'
    ),
]
