from .models import Project, Contact, Fundfy
import django_tables2 as tables
from django.db.models import Sum

class ProjectTable(tables.Table):
    project_id = tables.Column(linkify=True)
    investigator_supported = tables.Column(linkify=True)
    sponsor = tables.Column(linkify=True)

    class Meta:
        model = Project
        template_name = 'raptr/project_list.html'
        exclude = (
            'fund_code',
            'id',
            'oar_accept_date',
            'project_expiration_date',
            'project_notes',
            'slug',
            'sponsor',
        )


class ContactTable(tables.Table):
    last_name = tables.Column(linkify=True)

    class Meta:
        model = Contact
        template_name = 'raptr/contact_list.html'
        exclude = (
            'affiliation',
            'active',
            'employee_band',
            'employee_interval',
            'id',
            'job_title',
            'job_series',
            'pay_plan',
            'location',
            'opt_sub_group',
            'photo',
            'position_billet',
            'position_id',
            'flsa_status',
            'research_program',
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
