import re

from django import template
from django.utils.translation import gettext as _

from ..models import EmailDevice

register = template.Library()

email_mask = re.compile('(?<=.).(?=.+@)')


@register.filter
def mask_email_address(address):
    """
    Masks an email address, only first and last letters of the local part visible.

    Example:

    * `a*****b@domain.com`

    :param number: str object
    :return: str
    """

    return email_mask.sub('*', address)


@register.filter
def device_action(device):
    """
    Generates an actionable text for a :class:`~two_factor.models.EmailDevice`.

    Examples:

    * Send message to `a*****b@domain.com`
    """
    assert isinstance(device, EmailDevice)
    address = mask_email_address(device.address)
    return _('Send token to %s') % address
