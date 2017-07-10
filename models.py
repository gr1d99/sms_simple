
from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class MainConfiguration(models.Model):
    username = models.CharField(max_length=255, blank=True, unique=True)
    api_key = models.CharField(max_length=255, blank=True)
    secret_key = models.CharField(max_length=255, blank=True)


class AfricasTalking(MainConfiguration):
    class Meta:
        verbose_name_plural = "Africas Talking"

    default = models.BooleanField(default=False)


class AfricasTalkingTestReceivers(models.Model):
    """
    Dummy test model
    """
    phone_number = PhoneNumberField(unique=True)

