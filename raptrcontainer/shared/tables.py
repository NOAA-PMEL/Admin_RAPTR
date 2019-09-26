from .models import Contact
import django_tables2 as tables

"""

Generates contact table view in contact_list.html

"""


class ContactTable(tables.Table):
    last_name = tables.Column(linkify=True)

    class Meta:
        model = Contact
        template_name = 'shared/contact_list.html'
        exclude = (
            'full_time_equivalent',
            'service_computation_date',
            'pmel_base',
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
            'entry_on_duty',
            'departure_date',
            'supervisor',
        )
