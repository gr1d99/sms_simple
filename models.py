from __future__ import unicode_literals

from django.db import models


class MainConfiguration(models.Model):
    api_key = models.CharField(max_length=255, blank=True)
    secret_key = models.CharField(max_length=255, blank=True)


class AfricasTalking(MainConfiguration):
    class Meta:
        verbose_name_plural = "Africas Talking"

    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)