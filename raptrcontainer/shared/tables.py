from .models import Contact
from raptr.models import Fundfy
import django_tables2 as tables


class ContactTable(tables.Table):
    last_name = tables.Column(linkify=True)

    class Meta:
        model = Contact
        template_name = 'shared/contact_list.html'
        exclude = (
            'full_time_equivalent',
            'is_pi',
            'service_computation_date',
            'pmel_base',
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
        template_name = 'shared/index.html'
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