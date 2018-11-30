from .models import Project, Contact
import django_tables2 as tables


class ProjectTable(tables.Table):
    project_id = tables.Column(linkify=True)
    investigator_supported = tables.Column(linkify=True)
    sponsor = tables.Column(linkify=True)

    class Meta:
        model = Project
        template_name = 'raptr/project_list.html'
        exclude = (
            'id',
            'sponsor',
            'oar_accept_date',
            'project_expiration_date',
            'fund_code',
            'project_notes',
        )


class ContactTable(tables.Table):
    last_name = tables.Column(linkify=True)

    class Meta:
        model = Contact
        template_name = 'raptr/contact_list.html'
        exclude = (
            'id',
            'photo',
            'job_title',
            'opt_sub_group',
            'affiliation',
            'location',
            'research_program',
            'archive',
        )
