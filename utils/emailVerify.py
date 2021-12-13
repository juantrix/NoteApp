from envelopes import Envelope, GMailSMTP
import random

def send_email(email, code):
    receiver = email
    sender = 'bot.huannotes@gmail.com'

    envelope = Envelope(
        from_addr=(sender, u'Verify code'),
        to_addr=(receiver, u'To Example'),
        subject=u'Envelopes demo',
        text_body=f"Code: {code}"
    )

    # Send the envelope using an ad-hoc connection...
    # envelope.send('smtp.googlemail.com', login=sender,
    #             password='43042962', tls=True)

    # Or send the envelope using a shared GMail connection...
    gmail = GMailSMTP(sender, '43042962')
    gmail.send(envelope)

def send_email_verify(email):
    ran_code = random.randrange(10000,99999)
    send_email(email, ran_code)
    return ran_code



