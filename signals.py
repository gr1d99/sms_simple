import time

from django.db.models.signals import pre_save
from .models import AfricasTalking


# default configuration should always be one incase we have multiples
def one_default(sender, instance, **kwargs):
    if instance.default is True:
        africastalking_objs = AfricasTalking.objects.all()
        for obj in africastalking_objs:
            if obj.default is True:
                obj.default = False
                obj.save()
                time.sleep(5)


pre_save.connect(one_default, sender=AfricasTalking)