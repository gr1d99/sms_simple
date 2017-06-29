from __future__ import unicode_literals

from django.db import models


class MainConfiguration(models.Model):
    api_key = models.CharField(max_length=255, blank=True)
    secret_key = models.CharField(max_length=255, blank=True)


class AfricasTalking(MainConfiguration):
    username = models.CharField(max_length=255)