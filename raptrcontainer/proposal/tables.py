from .models import Proposal
import django_tables2 as tables


class ProposalTable(tables.Table):
    proposal_id = tables.Column(linkify=True)
    investigator_supported = tables.Column(linkify=True)
    sponsor = tables.Column(linkify=True)

    class Meta:
        model = Proposal
        template_name = 'proposal/proposal_list.html'
        exclude = (
            'fund_code',
            'id',
            'proposal_notes',
            'slug',
            'sponsor',
        )
