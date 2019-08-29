from .models import Mou
import django_tables2 as tables


class MouTable(tables.Table):
    mou_id = tables.Column(linkify=True)
    investigator_supported = tables.Column(linkify=True)
    sponsor = tables.Column(linkify=True)

    class Meta:
        model = Mou
        template_name = 'mou/mou_list.html'
        exclude = (
            'id',
            'slug',
            'mou_notes'
        )
