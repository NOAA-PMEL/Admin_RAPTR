from raptr.models import Project, Fundfy
from shared.models import Contact, Sponsor
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django_tables2 import SingleTableMixin, MultiTableMixin
from .tables import NewFundsTable
from django_filters.views import FilterView
from .filters import ContactFilter
from .tables import ContactTable
from django.views import generic
from django.db.models import Sum, F


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'shared/contact_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ContactDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Contact Detail'
        return context


class SponsorDetailView(DetailView):
    model = Sponsor
    template_name = 'shared/sponsor_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SponsorDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Sponsor Detail'
        return context


class AboutView(TemplateView):
    template_name = 'shared/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['title'] = 'About RAPTR'
        return context


class FilteredContactListView(SingleTableMixin, FilterView):
    table_class = ContactTable
    model = Contact
    template_name = 'shared/contact_list.html'

    filterset_class = ContactFilter
    paginate_by = 12

    def get_queryset(self):
        return super(FilteredContactListView, self).get_queryset().filter(active=True)

    def get_table_kwargs(self):
        return {'template_name': 'raptr/bootstrap.html'}

    def get_context_data(self, **kwargs):
        context = super(FilteredContactListView, self).get_context_data(**kwargs)
        context['title'] = 'RAPTR Contact List'
        return context


class IndexView(MultiTableMixin, generic.ListView):
    table_class = NewFundsTable
    model = Fundfy
    template_name = 'shared/index.html'

    def get_tables(self):
        fy_funds_received = Fundfy.objects.filter(fcfy="2019", fund_type = 1).order_by('project_id')
        return [NewFundsTable(fy_funds_received)]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'RAPTR Dashboard'
        return context

    def get_queryset(self):
        pass
        # by_division_1 = Project.objects.select_related('investigator_supported')
        # by_division_1 = Fundfy.objects.select_related('project_id')
        # by_division_2 = by_division_1.select_related('project_id__investigator_supported')
        # print(by_division_1)
        # print(by_division_2)
        # # by_division_2 = by_division_1.values('investigator_supported__division').filter(fundfy__fcfy="2019", fundfy__fund_type=1)
        # # print(by_division_2)
        # # by_division_sum = by_division_2.annotate(budget=Sum('fundfy__budget'))
        # # print(by_division_sum)
        # return by_division_1


class ReportView(generic.TemplateView):
    template_name = 'shared/reports.html'

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        context['title'] = 'RAPTR Reports'
        return context