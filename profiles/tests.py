"""Tests for the profiles app."""

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from profiles.models import Profile
from profiles.views import index, profile


class ProfileModelTest(TestCase):
    """Test the Profile model."""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='jdoe', password='pass')
        cls.profile = Profile.objects.create(user=cls.user, favorite_city='Paris')

    def test_profile_str(self):
        """Profile.__str__() should return the username."""
        self.assertEqual(str(self.profile), 'jdoe')


class ProfilesViewsTest(TestCase):
    """Tests for profiles views (index and detail)."""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='jdoe', password='pass')
        cls.profile = Profile.objects.create(user=cls.user, favorite_city='Paris')

    def test_index_view_status_and_template(self):
        """Index view returns 200 and uses the correct template."""
        url = reverse('profiles:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertIn(self.profile, response.context['profiles_list'])

    def test_detail_view_existing_profile(self):
        """Detail view for an existing profile returns 200 and correct template."""
        url = reverse('profiles:detail', args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(response.context['profile'], self.profile)

    def test_detail_view_nonexistent_profile(self):
        """Detail view for a non-existent profile returns custom 404."""
        url = reverse('profiles:detail', args=['no_user'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'profiles/profile_404.html')


class ProfilesURLsTest(TestCase):
    """Tests for profiles URL routing."""

    def test_index_url_resolves_to_index_view(self):
        """The URL for profiles:index should resolve to profiles.views.index."""
        url = reverse('profiles:index')
        resolver = resolve(url)
        self.assertEqual(resolver.func, index)

    def test_detail_url_resolves_to_profile_view(self):
        """The URL for profiles:detail should resolve to profiles.views.profile."""
        url = reverse('profiles:detail', args=['jdoe'])
        resolver = resolve(url)
        self.assertEqual(resolver.func, profile)
