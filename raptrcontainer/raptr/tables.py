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
            'fund_code',
            'id',
            'oar_accept_date',
            'project_expiration_date',
            'project_notes',
            'sponsor',
        )


class ContactTable(tables.Table):
    last_name = tables.Column(linkify=True)

    class Meta:
        model = Contact
        template_name = 'raptr/contact_list.html'
        exclude = (
            'affiliation',
            'archive',
            'id',
            'job_title',
            'location',
            'opt_sub_group',
            'photo',
            'research_program',
        )
