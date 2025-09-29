"""
URL configuration for {{cookiecutter.project_name}}.
"""

from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def health_check(request):
    """Health check endpoint."""
    return JsonResponse(
        {"status": "healthy", "service": "{{cookiecutter.project_name}}"}
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health_check, name="health"),
    path("api/", include("{{cookiecutter.project_slug}}.adapters.driving.api.urls")),
]
