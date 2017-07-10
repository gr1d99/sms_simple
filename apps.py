from __future__ import unicode_literals

from django.apps import AppConfig


class SmsSimpleConfig(AppConfig):
    name = 'sms_simple'

    def ready(self):
        import signals
