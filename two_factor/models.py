import logging
from binascii import unhexlify

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_otp.models import Device, ThrottlingMixin
from django_otp.oath import totp
from django_otp.util import hex_validator, random_hex

from .gateways import send_email


logger = logging.getLogger(__name__)


def get_available_email_methods():
    methods = []
    if getattr(settings, 'TWO_FACTOR_EMAIL_GATEWAY', None):
        methods.append(('email', _('Email message')))
    return methods


def get_available_methods():
    methods = [('generator', _('Token generator'))]
    methods.extend(get_available_email_methods())
    return methods


def key_validator(*args, **kwargs):
    """Wraps hex_validator generator, to keep makemigrations happy."""
    return hex_validator()(*args, **kwargs)


class EmailDevice(Device):
    """
    Model with email address and token seed linked to a user.
    """
    class Meta:
        app_label = 'two_factor'

    address = models.EmailField()
    key = models.CharField(
        max_length=40,
        validators=[key_validator],
        default=random_hex,
        help_text="Hex-encoded secret key"
    )
    method = 'email'

    def __repr__(self):
        return '<EmailDevice(address={!r}>'.format(
            self.address,
        )

    @property
    def bin_key(self):
        return unhexlify(self.key.encode())

    def verify_token(self, token):
        # local import to avoid circular import
        from two_factor.utils import totp_digits

        try:
            token = int(token)
        except ValueError:
            return False

        for drift in range(-5, 1):
            if totp(self.bin_key, drift=drift, digits=totp_digits()) == token:
                return True
        return False

    def generate_challenge(self):
        # local import to avoid circular import
        from two_factor.utils import totp_digits

        """
        Sends the current TOTP token to `self.number` using `self.method`.
        """
        no_digits = totp_digits()
        token = str(totp(self.bin_key, digits=no_digits)).zfill(no_digits)
        send_email(address=self.address, token=token)
