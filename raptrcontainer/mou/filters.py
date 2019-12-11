from django_filters import FilterSet

from .models import Mou


class MouFilter(FilterSet):

    class Meta:
        model = Mou
        fields = {
            'status': ['exact'],
        }
