from django_filters import FilterSet
from .models import Contact


class ContactFilter(FilterSet):

    class Meta:
        model = Contact
        fields = {
            'last_name': ['exact'],
            'division': ['exact'],
        }
