from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string


class AppSettings(object):

    @staticmethod
    def phone_number_field():
        field = 'phone_number'
        return field

    def get_phone_number_model(self):
        from django.conf import settings
        model = import_string(settings.PHONE_NUMBER_MODEL)

        try:
            model._meta.get_field(AppSettings.phone_number_field())
            return model

        except Exception as e:
            raise ImproperlyConfigured(e)
