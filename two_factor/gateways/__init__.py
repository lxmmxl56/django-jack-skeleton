from django.conf import settings
from django.utils.module_loading import import_string


def get_gateway_class(import_path):
    return import_string(import_path)


def send_email(address, token):
    gateway = get_gateway_class(getattr(settings, 'TWO_FACTOR_EMAIL_GATEWAY'))()
    gateway.send_email_token(address=address, token=token)
