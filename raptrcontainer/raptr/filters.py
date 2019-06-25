from django_filters import FilterSet
from .models import Project


class ProjectFilter(FilterSet):

    class Meta:
        model = Project
        fields = {
            'investigator_supported': ['exact'],
            'status': ['exact'],
            'year_proposed': ['exact']
        }

