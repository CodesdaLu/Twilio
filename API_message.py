import os
from twilio.rest import Client

numero =  '+12183182624'
meu_numero = '+5521994602511'

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hi Luana, this's a test in Python",
                     from_= numero,
                     to= meu_numero
                 )

print(message.sid)



#-----------------------------------
