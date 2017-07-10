from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)
from sms_simple.models import AfricasTalking, AfricasTalkingTestReceivers

cridentials = AfricasTalking.objects.get(default=True)
queryset = AfricasTalkingTestReceivers.objects.all()

# login cridentials
username = cridentials.username
apikey = cridentials.api_key

to = ','.join([r.phone_number.as_international.replace(' ', '') for r in queryset])

message = "This is a test message"

# Create a new instance of our awesome gateway class
gateway = AfricasTalkingGateway(username, apikey)


def send():
    try:

        results = gateway.sendMessage(to, message)

        for recipient in results:
            # status is either "Success" or "error message"
            print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
                                                                recipient['status'],
                                                                recipient['messageId'],
                                                                recipient['cost'])
    except AfricasTalkingGatewayException, e:
        print 'Encountered an error while sending: %s' % str(e)