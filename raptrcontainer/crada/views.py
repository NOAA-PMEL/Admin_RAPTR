from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .tables import CradaTable
from .models import Crada
from .filters import CradaFilter


class CradaListView(SingleTableMixin, FilterView):
    table_class = CradaTable
    model = Crada
    template_name = 'crada/crada_list.html'

    filterset_class = CradaFilter
    paginate_by = 8

    def get_queryset(self):
        return super(CradaListView, self).get_queryset().all()

    def get_table_kwargs(self):
        return {'template_name': 'raptr/bootstrap.html'}

    def get_context_data(self, **kwargs):
        context = super(CradaListView, self).get_context_data(**kwargs)
        context['title'] = 'CRADA Project List'
        return context
