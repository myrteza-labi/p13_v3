oui, oui, et pour la 3eme question je ne sais pas, tu pense qu'il vaut mieux que je l'active ? 

Je vais te coller encore du code pour que tu ai plus de contexte 

lettings: 

admin.py: 
"""Admin configuration for the lettings app."""


from django.contrib import admin
from .models import Address, Letting

admin.site.register(Address)
admin.site.register(Letting)

apps.py:
"""App configuration for the lettings app."""


from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """Configuration class for the lettings app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'

models.py:
"""Models for the lettings app."""


from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Model representing an address."""

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        db_table = 'oc_lettings_site_address'
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class Letting(models.Model):
    """Model representing a letting."""

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'oc_lettings_site_letting'
        verbose_name = 'Letting'
        verbose_name_plural = 'Lettings'

tests.py:
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

urls.py:
"""URL configuration for the lettings app."""


from django.urls import path
from . import views

app_name = 'lettings'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='detail'),
]

views.py:
"""Views for the lettings app."""

from django.shortcuts import render
from .models import Letting
import logging

logger = logging.getLogger(__name__)

# Aenean leo magna, vestibulum et tincidunt fermentum,
# consectetur quis velit. Sed non placerat massa.
# Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum
# primis in faucibus orci luctus et ultrices
# posuere cubilia curae; Cras eget scelerisque


def index(request):
    """View to display the list of all lettings."""
    lettings_list = Letting.objects.all()
    logger.info("Displayed the list of all lettings.")
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent dignissim, odio eu
# consequat pretium, purus urna vulputate arcu, vitae efficitur
# lacus justo nec purus. Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim, ac
# condimentum velit libero in magna. Suspendisse potenti.
# In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis
# urna pellentesque justo mattis ullamcorper ac non tellus. In
# tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor
# risus. Mauris condimentum auctor elementum. Donec quis nisi ligula.
# Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """View to display the details of a specific letting."""
    try:
        letting = Letting.objects.get(id=letting_id)
        logger.info(f"Displayed details for letting id {letting_id}.")
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        logger.warning(f"Letting with id {letting_id} not found.")
        context = {'letting_id': letting_id}
        return render(request, 'lettings/letting_404.html', context, status=404)

oc-lettings-iste:
admin:
"""Admin configuration for the oc_lettings_site app."""

apps:
"""App configuration for the oc_lettings_site app."""


from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """Configuration class for the oc_lettings_site app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'oc_lettings_site'
    verbose_name = 'Oc Lettings Site'

asgi:
"""ASGI config for the oc_lettings_site project."""


import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_asgi_application()

settings:
"""Django settings for the oc_lettings_site project."""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# Application definition
INSTALLED_APPS = [
    'oc_lettings_site.apps.OCLettingsSiteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lettings',
    'profiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oc_lettings_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'oc-lettings-site.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Use ManifestStaticFilesStorage in production, default in tests/CI
# En tests/CI, on reste sur le stockage Django standard,
# en prod on utilise WhiteNoise compressé sans manifeste
if len(sys.argv) > 1 and sys.argv[1] == 'test':
    STATICFILES_STORAGE = (
        'django.contrib.staticfiles.storage.StaticFilesStorage'
    )
else:
    STATICFILES_STORAGE = (
        'whitenoise.storage.CompressedStaticFilesStorage'
    )

SENTRY_DSN = os.getenv('SENTRY_DSN')
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'sentry': {
            'class': 'sentry_sdk.integrations.logging.EventHandler',
            'level': 'ERROR',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'sentry'],
            'level': 'INFO',
            'propagate': True,
        },
        '': {
            'handlers': ['console', 'sentry'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

tests:
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

urls:
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

# Serve static files in all environments (even when DEBUG=False)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

views:
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

wsgi:
"""WSGI config for the oc_lettings_site project."""


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

application = get_wsgi_application()


profiles:
admin:
"""Admin configuration for the profiles app."""


from django.contrib import admin
from .models import Profile

admin.site.register(Profile)

apps:
"""App configuration for the profiles app."""


from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """Configuration class for the profiles app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

models:
"""Models for the profiles app."""


from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Model representing a user profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'oc_lettings_site_profile'
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

tests:
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

urls:"""URL configuration for the profiles app."""


from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='detail'),
]

views:
"""Views for the profiles app."""

from django.shortcuts import render
from .models import Profile
import logging

logger = logging.getLogger(__name__)

# Sed placerat quam in pulvinar commodo. Nullam laoreet
# consectetur ex, sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus


def index(request):
    """View to display the list of all profiles."""
    profiles_list = Profile.objects.all()
    logger.info("Displayed the list of all profiles.")
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis
# pharetra vulputate. Sed tincidunt, dolor id facilisis
# fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant
# morbi tristique senectus et netus et males
def profile(request, username):
    """View to display the details of a specific profile."""
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info(f"Displayed profile for username: {username}.")
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        logger.warning(f"Profile with username '{username}' not found.")
        context = {'username': username}
        return render(request, 'profiles/profile_404.html', context, status=404)
