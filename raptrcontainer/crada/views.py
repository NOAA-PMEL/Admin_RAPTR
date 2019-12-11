from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView

from django_filters.views import FilterView

from django_tables2 import SingleTableMixin

from .filters import CradaFilter
from .models import Crada
from .tables import CradaTable


@method_decorator(login_required, name='dispatch')
class CradaListView(SingleTableMixin, FilterView):
    table_class = CradaTable
    model = Crada
    template_name = 'crada/crada_list.html'

    filterset_class = CradaFilter
    paginate_by = 15

    def get_queryset(self):
        return super(CradaListView, self).get_queryset().all()

    def get_table_kwargs(self):
        return {'template_name': 'shared/table_bootstrap.html'}

    def get_context_data(self, **kwargs):
        context = super(CradaListView, self).get_context_data(**kwargs)
        context['title'] = 'CRADA Project List'
        context['crada_page'] = 'active'
        return context


@method_decorator(login_required, name='dispatch')
class CradaDetailView(DetailView):
    model = Crada
    template_name = 'crada/crada_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CradaDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Crada Detail'
        context['crada_page'] = 'active'
        return context
