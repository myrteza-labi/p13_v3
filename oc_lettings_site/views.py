"""Views for the oc_lettings_site app."""

from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque
# molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
# eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna
# nisi, pellentesque iaculis enim cursus in. Praesent volutpat
# porttitor magna, non finibus neque cursus id.
def index(request):
    """View to display the home page."""
    return render(request, 'index.html')


def custom_404(request, exception):
    """Custom handler for 404 errors."""
    logger.warning(f"404 error encountered: {request.path} - {exception}")
    return render(request, '404.html', status=404)
