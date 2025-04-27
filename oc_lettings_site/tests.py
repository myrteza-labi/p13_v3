"""Tests for the oc_lettings_site app."""


from django.test import TestCase
from django.urls import reverse, resolve
from oc_lettings_site import views

class SiteViewsTest(TestCase):
    """Tests for oc_lettings_site views."""

    def test_index_view(self):
        """Index view returns 200 and uses the correct template."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_custom_404_view(self):
        """Custom 404 view returns 404 and uses the 404 template."""
        # On simule une URL inconnue
        response = self.client.get('/nonexistent-page/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')


class SiteURLsTest(TestCase):
    """Tests for oc_lettings_site URL routing."""

    def test_index_url_resolves_to_index_view(self):
        """The root URL should resolve to oc_lettings_site.views.index."""
        resolver = resolve('/')
        self.assertEqual(resolver.func, views.index)

    def test_404_handler_is_custom(self):
        """handler404 must be set to custom_404."""
        import oc_lettings_site.urls as urls_mod
        self.assertEqual(urls_mod.handler404, 'oc_lettings_site.views.custom_404')
