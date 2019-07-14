from django import template

register = template.Library()
"""

Checks if the user belongs to the group passed to the function. Returns boolean. {% load shared_extras %} to use.

"""


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()