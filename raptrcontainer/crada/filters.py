from django_filters import FilterSet

from .models import Crada


class CradaFilter(FilterSet):

    class Meta:
        model = Crada
        fields = {
            'project_status': ['exact'],
        }
