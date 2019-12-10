from django_filters import FilterSet
from .models import Contact


class ContactFilter(FilterSet):
    """

    Filter for the table view in contact_list.html

    """
    class Meta:
        model = Contact
        fields = {
            'last_name': ['contains'],
            'division': ['exact'],
            'employee_type': ['exact'],
            'affiliation': ['exact'],
        }
