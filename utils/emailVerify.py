from envelopes import Envelope, GMailSMTP
import json
import random

data = open('data.json', 'r')
data = json.load(data)

def send_email(email, code):
    receiver = email
    sender = data['email']

    envelope = Envelope(
        from_addr=(sender, u'Verify code'),
        to_addr=(receiver, u'To Example'),
        subject=u'Envelopes demo',
        text_body=f"Code: {code}"
    )

    gmail = GMailSMTP(sender, data['pass'])
    gmail.send(envelope)

def send_email_verify(email):
    ran_code = random.randrange(10000,99999)
    send_email(email, ran_code)
    return ran_code





