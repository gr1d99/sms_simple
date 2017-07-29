import mock

from django.db.models.signals import pre_save
from django.test import TestCase
from .models import AfricasTalking


class AfricasTalkingTest(TestCase):

    """
    AfricasTalking model has a default field which is a boolean, each time default is set to True, the previous
    AfricasTalking object default field is automatically set to False.
    in this test case we expect account_3 object default field to be True and `account_1, and account_2 objects deffault
    fields to be False.
    """

    @classmethod
    def setUpTestData(cls):

        with mock.patch('sms_simple.signals.one_default', autospec=True) as mocked_handler:
            pre_save.connect(mocked_handler, sender=AfricasTalking)

            # create objects
            AfricasTalking.objects.create(
                username='username1',
                api_key='bcbbjcm89kdeh7dejwalmxb',
                secret_key='bchdbhcbdbchbddbchdbcycc6c5edvev',
                default=True
            )

            AfricasTalking.objects.create(
                username='username2',
                api_key='bcbbjcm89kdeh7hjkopklmxb',
                secret_key='bchdbhcbdnjnkxlpjwrycc6c5edvev',
                default=True
            )

            AfricasTalking.objects.create(
                username='username3',
                api_key='jyvcfcaeh7hjkopklmxb',
                secret_key='qazlk123dnjnkxlpjwrycc6c5edvev',
                default=True
            )

    def test_defaultaccount_is_only_one(self):

        # iterate through objects and check the default field
        # in case someone adds more objects then we'd better keep track of
        # all objects count.
        total_objs = len(AfricasTalking.objects.all())
        count = 1
        for obj in AfricasTalking.objects.all():
            if not count == total_objs:
                self.assertEqual(obj.default, False)

            else:
                # the last object added default value will always be True
                self.assertEqual(obj.default, False)

            count += 1
