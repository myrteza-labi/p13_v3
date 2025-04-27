"""Tests for the lettings app."""

from django.test import TestCase
from django.urls import reverse, resolve
from lettings.models import Address, Letting
from lettings.views import index, letting


class AddressModelTest(TestCase):
    """Test the Address model."""

    def test_address_str(self):
        """Test the string representation of Address."""
        address = Address.objects.create(
            number=123,
            street="Baker Street",
            city="London",
            state="LD",
            zip_code=12345,
            country_iso_code="GBR"
        )
        self.assertEqual(str(address), "123 Baker Street")


class LettingModelTest(TestCase):
    """Test the Letting model."""

    def test_letting_str(self):
        """Test the string representation of Letting."""
        address = Address.objects.create(
            number=221,
            street="Baker Street",
            city="London",
            state="LD",
            zip_code=12345,
            country_iso_code="GBR"
        )
        letting = Letting.objects.create(
            title="Sherlock Holmes Apartment",
            address=address
        )
        self.assertEqual(str(letting), "Sherlock Holmes Apartment")


class LettingsViewsTest(TestCase):
    """Tests for lettings views (index and detail)."""

    @classmethod
    def setUpTestData(cls):
        # Crée un address et un letting valides pour les tests
        cls.address = Address.objects.create(
            number=10,
            street="Downing Street",
            city="London",
            state="LD",
            zip_code=12345,
            country_iso_code="GBR"
        )
        cls.letting = Letting.objects.create(
            title="Prime Minister's Residence",
            address=cls.address
        )

    def test_index_view_status_and_template(self):
        """Index view returns 200 and uses the correct template."""
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        # On vérifie que notre letting apparaît dans le contexte
        self.assertIn(self.letting, response.context['lettings_list'])

    def test_detail_view_existing_letting(self):
        """Detail view for an existing letting returns 200 and correct template."""
        url = reverse('lettings:detail', args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')
        self.assertEqual(response.context['title'], self.letting.title)

    def test_detail_view_nonexistent_letting(self):
        """Detail view for a non-existent letting returns custom 404."""
        url = reverse('lettings:detail', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'lettings/letting_404.html')


class LettingsURLsTest(TestCase):
    """Tests for lettings URL routing."""

    def test_index_url_resolves_to_index_view(self):
        """The URL for lettings:index should resolve to lettings.views.index."""
        url = reverse('lettings:index')
        resolver = resolve(url)
        self.assertEqual(resolver.func, index)

    def test_detail_url_resolves_to_letting_view(self):
        """The URL for lettings:detail should resolve to lettings.views.letting."""
        # On donne un ID factice (l'existence n'est pas vérifiée ici)
        url = reverse('lettings:detail', args=[123])
        resolver = resolve(url)
        self.assertEqual(resolver.func, letting)
