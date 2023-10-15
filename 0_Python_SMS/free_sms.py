import json
from getpass import getpass

reset_creds=True

if reset_creds:
    twilio_sid = getpass("What's the twilio account sid?");
    twilio_secret = getpass("What's the twilio Token?");

    data={
        "twilio_sid": twilio_sid,
        "twilio_secret": twilio_secret
    }
    json_data = json.dumps(data)
    with open('creds.json','w') as f:
        f.write(json.data)



from twilio.rest import Client;

SID ='AC07f006ed7312b41db94f83dbc345f390';
Auth_Token = '5354dfd04d186858affb8d88aa29d25d';
cl = Client (SID,Auth_Token);
cl.messages.create(body='This is a new message',from_='+918767008518', to='+918087252421');
