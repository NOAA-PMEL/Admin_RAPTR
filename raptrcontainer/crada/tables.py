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
            'fund_code',
            'id',
            'oar_accept_date',
            'project_expiration_date',
            'project_notes',
            'slug',
        )


class NewFundsTable(tables.Table):
    project_id = tables.Column(linkify=True, footer='Total:')
    budget = tables.Column(footer=lambda table: sum(x.budget for x in table.data), attrs={"td": {"align": "right"}})

    class Meta:
        model = Fundfy
        template_name = 'raptr/index.html'
        exclude = (
            'fcfy',
            'fund_code',
            'id',
            'oar_accept_date',
            'project_expiration_date',
            'project_notes',
            'sponsor',
            'budget_currency',
            'fund_type'
        )
