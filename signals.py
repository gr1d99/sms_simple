from django.db.models.signals import pre_save
from .models import AfricasTalking, PhoneNumbers
from app_settings import AppSettings

phone_number_model = AppSettings().get_phone_number_model()


# default configuration should always be one incase we have multiples
def one_default(sender, instance, **kwargs):
    if instance.default is True:
        africastalking_objs = AfricasTalking.objects.all()
        for obj in africastalking_objs:
            if obj.default is True:
                obj.default = False
                obj.save()


def one_phone_numbers_entry(sender, instance, **kwargs):
    latest_entry = PhoneNumbers.objects.last()

    if latest_entry:
        phone_numbers = latest_entry.phone_numbers
        old_phone_numbers = phone_numbers.split(',')[:-1]
        phone_number = ',%(phone_number)s' % dict(phone_number=instance.phone_number)
        new_phone_numbers = old_phone_numbers
        print type(new_phone_numbers)
    else:
        phone_number = '%(phone_number)s,' % dict(phone_number=instance.phone_number)
        PhoneNumbers.objects.create(phone_numbers=phone_number)

pre_save.connect(one_default, sender=AfricasTalking)
pre_save.connect(one_phone_numbers_entry, sender=phone_number_model)