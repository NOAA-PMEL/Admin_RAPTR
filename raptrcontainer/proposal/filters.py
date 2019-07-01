from django_filters import FilterSet
from .models import Proposal


class ProposalFilter(FilterSet):

    class Meta:
        model = Proposal
        fields = {
            'investigator_supported': ['exact'],
            'status': ['exact'],
            'year_proposed': ['exact']
        }

