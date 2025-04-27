"""App configuration for the lettings app."""


from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """Configuration class for the lettings app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'
