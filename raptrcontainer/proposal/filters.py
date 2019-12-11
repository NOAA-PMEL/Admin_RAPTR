import django_filters
from django_filters import FilterSet

from shared.models import Contact

from .models import Proposal


class ProposalFilter(FilterSet):
    investigator_supported = django_filters.ModelChoiceFilter(queryset=Contact.objects.all().filter(active=True, is_pi=True), lookup_expr='exact', label='PI')

    class Meta:
        model = Proposal
        fields = {
            'status': ['exact'],
            'year_proposed': ['exact']
        }
