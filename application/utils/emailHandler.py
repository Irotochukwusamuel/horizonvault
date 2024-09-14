import datetime
import uuid

from dotenv import load_dotenv
import base64
from pathlib import Path
import os
import mailtrap as mt

from application import SECRET_KEY
import jwt
load_dotenv()

token = "f45fb90ea2ca196d3e67ae7c4ef78389"
base_url = "http://3.145.101.11:5000/"


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
    def send_invite_email(cls, recipient, school_name, role, link):
        subject = f'You have been invited to join {school_name}'
        body = f"""

                <p>
                    You have been invited to join {school_name} as a {role}, click the button below to set up your profile. Once you're done, you can then login with your email and password.
                    if you have any questions, feel free to reach out to the school admin.
                </p>

                
                <a href="{link}" class="mb-20">Set up profile</a>

        """

        return cls.send_email(recipient, subject, '', body)

    @classmethod
    def welcome_mail(cls, recipient, username):
        subject = 'Your Key Academy Account has been created.'
        _token = cls.generate_password_token()
        body = f"""

                <p>
                    Now that your account has been created, click the button below to setup your password so that you
                    can login to your account. After that, you can always log into your account using your email address
                    and the password you have set up!
                </p>

                <!-- Add your reset password link -->
                <a href="https://keyhub-frontend.vercel.app/auth/new-user/password-setup?email={recipient}&token={_token}" class="mb-20">Reset Password</a>

        """

        return cls.send_email(recipient, subject, username, body)

    @classmethod
    def send_otp(cls, recipient, otp, token):
        subject = 'Your Key Academy Account OTP'
        body = f"""

                <p>
                   Your OTP is <b>{otp}.</b> The OTP expires in 2 minutes.</p>
                </p>

                <!-- Add your reset password link -->
                <a href="https://keyhub-frontend.vercel.app/auth/password-setup?token={token}&email={recipient}" class="mb-20">Reset Password</a>

        """

        return cls.send_email(recipient, subject, '', body)

    @classmethod
    def send_email(cls, recipient, subject, username, body):
        current_year = datetime.datetime.now().year
        mail = mt.Mail(
            sender=mt.Address(email="mailtrap@axetechinnovations.com", name="Key Academy"),
            to=[mt.Address(email=recipient, name="clair")],
            subject=subject,
            html=f"""
            <!doctype html>
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Account Created</title>
                <style>
                    @font-face {{
                        font-family: 'QuickSand';
                        src: url('{base_url}fonts/quicksand/Quicksand-Regular.ttf') format('woff2'),
                        url('{base_url}fonts/quicksand/Quicksand-Regular.ttf') format('woff');
                    }}
    
                    @font-face {{
                        font-family: 'QuickSand Bold';
                        src: url('{base_url}fonts/quicksand/Quicksand-Bold.ttf') format('woff2'),
                        url('{base_url}fonts/quicksand/Quicksand-Bold.ttf') format('woff');
                    }}
    
                    body {{
                        margin: 0;
                        padding: 0;
                        font-family: 'QuickSand', sans-serif;
                        background-color: #fff;
                    }}
    
                    .container {{
                        max-width: 90%;
                        margin: auto;
                    }}
                    

    
                    .header-container {{
                        width : 100%;
                        height : 400px;
                        background-image: url('{base_url}images/login_image.png');
                        background-size: cover;
                        background-position: top;
                        background-repeat: no-repeat;
                    }}
    
                    .bold {{
                        font-family: 'QuickSand Bold', 'Arial', sans-serif;
                    }}
    
                    table {{
                        width: 100%;
                        border-collapse: collapse;
                    }}
    
                    img {{
                        width: 100%;
                        height: auto;
                        
                    }}
    
                    td {{
                        padding: 20px;
                        text-align: left;
                    }}
    
                    h2 {{
                        color: #333;
                        font-size: 35px;
                    }}
    
                    a {{
                        display: inline-block;
                        padding: 20px 30px;
                        background-color: #007BFF;
                        color: white !important;
                        text-decoration: none;
                        border-radius: 5px;
                    }}
    
                    p {{
                        color: #555;
                        line-height: 30px;
                        margin: 0 0 20px 0;
                    }}
    
                    footer {{
                        background-color: #F5F6FA;
                        padding: 10px;
                        text-align: center;
                    }}
    
                    footer > img {{
                        height: 50px;
                        width: auto;
                    }}
    
                    footer > p {{
                        margin: 0;
                    }}
    
                    .mb-20 {{
                        margin-bottom: 20px !important;
                    }}
                    

                    
                </style>
            </head>
            <body>
            <div class="container">
                <!-- Header with Full-width Image -->
                <div class="header-container"></div>
    
                <!-- Email Content -->
                <table>
                    <tr>
                        <td>
                            <h2 class="bold">{subject}</h2>
    
                            <p>Hello <span class="bold">{username}</span>,</p>
                            
                            {body}
    
                            <p>
                                Best Regards, <br>The Key Academy Team
                            </p>
    
                        </td>
                    </tr>
                </table>
    
                <!-- Footer -->
                <footer>
                    <p>&copy; Key Academy. <span id="currentYear">{current_year}</span>. All Rights Reserved</p>
                    <img src="{base_url}images/old_logo.png" alt="Logo">
                </footer>
            </div>
            
            
    

            </body>
            </html>
    
            """
        )

        client = mt.MailtrapClient(token=token)
        client.send(mail)
        return True
