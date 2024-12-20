import datetime
import uuid
from mailbox import Message

import courier
from courier.client import Courier
from dotenv import load_dotenv
import os

from application import SECRET_KEY, mail
import jwt

load_dotenv()

email_token = os.getenv('EMAIL_KEY')


class EmailHandler:

    @staticmethod
    def generate_password_token():
        token_id = str(uuid.uuid4())

        payload = {
            'token_id': token_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }
        _token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return _token

    @classmethod
    def handle_admin_notification(cls, subject, message):
        cls.email('info@horizonvaut.com', subject, message)

    @classmethod
    def email(cls, recipient, subject, body):
        # client = Courier(
        #     authorization_token=email_token
        # )
        #
        # response = client.send(
        #     message=courier.ContentMessage(
        #         to=courier.UserRecipient(
        #             email=recipient,
        #         ),
        #         content=courier.ElementalContentSugar(
        #             title=subject,
        #             body=body,
        #         ),
        #         routing=courier.Routing(method="all", channels=["inbox", "email"]),
        #     )
        # )
        #
        # return response

        mail.send_message(subject=subject, body=body, recipients=[recipient])
        return 'Email sent successfully!'



