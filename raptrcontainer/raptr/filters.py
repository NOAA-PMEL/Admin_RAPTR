import django_filters
from django_filters import FilterSet

from shared.models import Contact

from .models import Project

DIVISION_CHOICES = (
    ('AD', 'AD'),
    ('CS', 'CS'),
    ('ED', 'ED'),
    ('OC', 'OC'),
    ('OD', 'OD'),
    ('OE', 'OE'),
)


class ProjectFilter(FilterSet):
    investigator_supported__division = django_filters.ChoiceFilter(choices=DIVISION_CHOICES, lookup_expr='exact', label='Division')
    investigator_supported = django_filters.ModelChoiceFilter(queryset=Contact.objects.all().filter(active=True, is_pi=True), lookup_expr='exact', label='PI')

    class Meta:
        model = Project
        fields = {
            'status': ['exact'],
            'year_proposed': ['exact']
        }
