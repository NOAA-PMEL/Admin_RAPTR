from .models import Crada
import django_tables2 as tables


class CradaTable(tables.Table):
    docket_number = tables.Column(linkify=True)
    noaa_pi = tables.Column(linkify=True)
    collaborator = tables.Column(linkify=True)

    class Meta:
        model = Crada
        template_name = 'crada/crada_list.html'
        exclude = (
            'id',
            'slug',
            'project_summary'
        )
