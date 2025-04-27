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
