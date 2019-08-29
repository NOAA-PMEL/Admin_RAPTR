from .models import Project
import django_tables2 as tables


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
