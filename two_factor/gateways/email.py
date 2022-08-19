import logging

from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


class Email(object):
    @staticmethod
    def send_email_token(address, token):
        logger.info('Token email to %s: "Your token is: %s"', address, token)
        print('Token email to %s: Your token is: %s' % (address, token))

        send_mail(
            f'{settings.PROJECT_NAME} Two-Factor Authentication Token',
            f'Your token is:\n\n{token}',
            settings.DEFAULT_FROM_EMAIL,
            [address],
            fail_silently=False,
        )
