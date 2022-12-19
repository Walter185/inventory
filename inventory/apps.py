from django.apps import AppConfig
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

class InventoryConfig(AppConfig):
    name = 'inventory'
