from .models import Proposal
from .filters import ProposalFilter
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from .tables import ProposalTable
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ProposalDetailView(DetailView):
    model = Proposal
    template_name = 'proposal/proposal_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProposalDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Proposal Detail'
        context['proposal_page'] = 'active'
        return context


@method_decorator(login_required, name='dispatch')
class FilteredProposalListView(SingleTableMixin, FilterView):
    table_class = ProposalTable
    model = Proposal
    template_name = 'proposal/proposal_list.html'

    filterset_class = ProposalFilter
    paginate_by = 15

    def get_queryset(self):
        return super(FilteredProposalListView, self).get_queryset().all().order_by('-year_proposed')

    def get_table_kwargs(self):
        return {'template_name': 'shared/table_bootstrap.html'}

    def get_context_data(self, **kwargs):
        context = super(FilteredProposalListView, self).get_context_data(**kwargs)
        context['title'] = 'Proposal List'
        context['proposal_page'] = 'active'
        return context
