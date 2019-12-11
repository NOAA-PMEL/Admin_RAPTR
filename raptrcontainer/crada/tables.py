from datetime import date

import django_tables2 as tables

from .models import Crada


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

        row_attrs = {
            "class": lambda record: "status-alert-red" if record.activity_phase == 'Signed' and (record.expiration_date - date.today()).days < 180 else "status-alert-none"
        }
