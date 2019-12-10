from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from django.views.generic.detail import DetailView
from .tables import MouTable
from .models import Mou
from .filters import MouFilter
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class MouListView(SingleTableMixin, FilterView):
    table_class = MouTable
    model = Mou
    template_name = 'mou/mou_list.html'

    filterset_class = MouFilter
    paginate_by = 15

    def get_queryset(self):
        return super(MouListView, self).get_queryset().all()

    def get_table_kwargs(self):
        return {'template_name': 'shared/table_bootstrap.html'}

    def get_context_data(self, **kwargs):
        context = super(MouListView, self).get_context_data(**kwargs)
        context['title'] = 'MOU List'
        context['mou_page'] = 'active'
        return context


@method_decorator(login_required, name='dispatch')
class MouDetailView(DetailView):
    model = Mou
    template_name = 'mou/mou_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MouDetailView, self).get_context_data(**kwargs)
        context['title'] = 'MOU Detail'
        context['mou_page'] = 'active'
        return context
