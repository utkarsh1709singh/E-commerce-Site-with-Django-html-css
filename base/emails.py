from django.conf import settings
from django.core.mail import send_mail


def send_account_activation_email(email, email_token):
    subject='Your account need to be verified'
    email_from=settings.EMAIL_HOST_USER
    mesaage=f'Please click on the link below to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
    
    send_mail(subject,mesaage,email_from,[email])
    