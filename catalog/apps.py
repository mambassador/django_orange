from django.apps import AppConfig


class CatalogConfig(AppConfig):
    """Configuration class for the 'catalog' Django app

    Attributes:
        default_auto_field (str): The default auto-generated field type
                                  for models in the app.
        name (str): The name of the app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "catalog"
