import datetime
from firebase_admin import initialize_app, messaging


class FcmIntegration(object):
    
    def initalize_firebase_app(self):
        default_app = initialize_app()

    def send_to_token(self, registration_token, title, body, data):
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            android=messaging.AndroidConfig(
                ttl=datetime.timedelta(seconds=3600),
                priority='high',
            ),
            token=registration_token,
            data=data,
        )
        response = messaging.send(message)

    def send_to_topic(self, topic, title, body):
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=title,
            ),
            topic=topic,
        )

        response = messaging.send(message)

    def send_multicast(self, registration_tokens, title, body, data, channel, sound):
        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title=title,
                body=title,
            ),
            android=messaging.AndroidConfig(
                ttl=datetime.timedelta(seconds=3600),
                priority='high',
            ),
            tokens=registration_tokens,
            data=data,
        )
        response = messaging.send_multicast(message)
