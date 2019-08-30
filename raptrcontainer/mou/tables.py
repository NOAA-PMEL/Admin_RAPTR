from .models import Mou
from datetime import date
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
        row_attrs = {
            "class": lambda record: "status-alert" if record.status == 'Open' and (record.expiration_date - date.today()).days < 90 else "good"
        }