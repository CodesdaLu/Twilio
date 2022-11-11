import os
from twilio.rest import Client

numero =  '+12183182624'
meu_numero = '+5521994602511'

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC7ee143bc4d8e0fbec758710e659634d1'
auth_token = '9b5d781bc3e98b99a5dace5400803639'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hi Luana, this's a test in Python",
                     from_= numero,
                     to= meu_numero
                 )

print(message.sid)



#-----------------------------------