from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9d67943f11ec7e3963725318a405a572"
# Your Auth Token from twilio.com/console
auth_token  = "0989627608aff814f2e3d85b5a4d7920"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15404973344", 
    from_="+18136963778",
    body="The W.O.R.M. posesses technology...")

print(message.sid)
