# sms_simple
sms_simple is a pluggable django app that will support multiple sms gateways.

to run this app you will need to have installed `python2` and `django1.1+`

**NB This app is still in development so make sure you keep checking for more updates**

Usage
----------
1. run `pip install AfricastalkingGateway` then.

2. `git clone https://github.com/gr1d99/sms_simple.git` into your 
project or anywhere but make sure you copy it to your project directory.

3. add `sms_simple` to your project `INSTALLED_APPS`.

4. sync your db.

5. open django admin site and add your AfricasTalking `username` and `apikey`

6. Add some of the numbers you know in `AfricasTalkingTestReceivers` model.

7. That is it!!, now all you need is to run `python manage.py shell`

8. to send messages just run the code snippet below
   ```python
   from sms_simple.api import africastalking_gateway as afg
   # call the send() function
   >>> afg.send()
   ```
   
 