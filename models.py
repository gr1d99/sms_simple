
from __future__ import unicode_literals

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MainConfiguration(models.Model):

    username = models.CharField(max_length=255, blank=True, unique=True)
    api_key = models.CharField(max_length=255, blank=True)
    secret_key = models.CharField(max_length=255, blank=True)

    class Meta:
        abstract = True


class AfricasTalking(MainConfiguration):

    default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Africas Talking"


class AfricasTalkingTestReceivers(models.Model):
    """
    Dummy test model
    """
    phone_number = PhoneNumberField(unique=True)

    def __str__(self):
        return '%s' % self.phone_number


class PhoneNumbers(models.Model):

    class Meta:
        verbose_name = 'Phone Numbers'
        verbose_name_plural = 'Phone Numbers'


    phone_numbers = models.TextField()
