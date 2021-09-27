from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .tokens import account_activation_token


def send_activation_email(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)
    subject = "Activate your account"
    domain = "127.0.0.1:8000"
    message = render_to_string(
        template_name="email_activation.html", context={"user": user, "domain": domain, "uid": uid, "token": token}
    )
    print(message)
    # send_mail(subject=subject, message=message, from_email="noreply@keyarabia.com", recipient_list=[user.email])
