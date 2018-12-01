from django_filters import FilterSet
from .models import Project, Contact


class ProjectFilter(FilterSet):

    class Meta:
        model = Project
        fields = {
            'investigator_supported': ['exact'],
            'status': ['exact'],
            'year_proposed': ['exact']
        }


class ContactFilter(FilterSet):

    class Meta:
        model = Contact
        fields = {
            'last_name': ['exact'],
            'division': ['exact'],
        }
