from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()
"""

Formatters for use in templates. {% load shared_filters %} to use.

"""


@register.filter
def currency(dollars):
    if dollars is None:
        dollars = float(0.00)
    else:
        dollars = round(float(dollars), 2)
    return "$%s%s" % (intcomma(int(dollars)), ("% 0.2f" % dollars)[-3:])


@register.filter
def div(value, arg):
    """
    Divides the value; argument is the divisor.
    Returns empty string on any error.
    """
    try:
        value = int(value)
        arg = int(arg)
        if arg: return value/arg
    except:
        pass
    return ''


@register.filter
def percent(value):
    value *= 100
    if value is None:
        value = float(0.00)
    else:
        value = round(float(value), 2)
    return "%s%s%%" % (intcomma(int(value)), ("% 0.2f" % value)[-3:])

