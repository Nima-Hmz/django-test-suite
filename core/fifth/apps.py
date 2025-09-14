from django.apps import AppConfig
from django.db.models.signals import post_save


class FifthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fifth'

    def ready(self):
        from . import signals
        from second.models import Products
        import uuid
        post_save.connect(signals.call_back_email_after_save_product, sender=Products, dispatch_uid="fifth.call_back_email_after_save_product")

