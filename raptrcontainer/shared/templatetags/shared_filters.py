from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()
"""

Currency formatter for use in templates. {% load shared_filters %} to use.

"""


def currency(dollars):
    if dollars is None:
        dollars = float(0.00)
    else:
        dollars = round(float(dollars), 2)
    return "$%s%s" % (intcomma(int(dollars)), ("% 0.2f" % dollars)[-3:])


register.filter('currency', currency)
