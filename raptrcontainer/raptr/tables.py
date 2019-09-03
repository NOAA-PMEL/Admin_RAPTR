import django_tables2 as tables
from datetime import date
from .models import Project


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
            'project_notes',
            'slug',
            'sponsor',
        )
        row_attrs = {
            "class": lambda record: "status-alert-red" if record.status == 'Open' and (record.project_expiration_date - date.today()).days < 90 else "status-alert-none"
        }