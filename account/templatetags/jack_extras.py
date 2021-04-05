from logging import getLogger

from django import template
from django.conf import settings

log = getLogger(settings.DEBUG_LOGGER)


register = template.Library()


@register.filter
def remove_language_codes(value):
    value = value[3:]
    if '?next=/ja/' in value or '?next=/en/' in value :
        next_index = value.find('?next=')
        next_value = value[next_index+6:]
        new_next = next_value[3:]
        value = value[:next_index+6] + new_next
    return value


@register.filter
def percent_format(value):
    return "{:.2f}".format(value * 100)


@register.filter
def keyvalue(dict, key):
    if key in dict:
        return dict[key]
    else:
        return None


@register.filter
def subtract(value, arg):
    return value - arg
