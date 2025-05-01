"""URL configuration for the oc_lettings_site app."""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


def trigger_error(request):
    """View to trigger a division by zero error for Sentry test."""
    1 / 0  # Force an intentional error


handler404 = 'oc_lettings_site.views.custom_404'

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('sentry-debug/', trigger_error),
]

# Serve static files only when DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
