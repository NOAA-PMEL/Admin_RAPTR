from raptr.models import Fundfy
from shared.models import Contact, Sponsor
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, View
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .filters import ContactFilter
from .tables import ContactTable
from django.views import generic
from django.db.models import Sum, F
from rest_framework.views import APIView
from rest_framework.response import Response


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


class IndexView(generic.TemplateView):

    template_name = 'shared/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['by_division'] = Fundfy.objects.values(division=F('project_id__investigator_supported__division'))\
            .filter(fcfy="2019", fund_type=1)\
            .annotate(Sum('budget'))\
            .order_by('-budget__sum')
        context['by_division_total'] = Fundfy.objects.values(division=F('project_id__investigator_supported__division'))\
            .filter(fcfy="2019", fund_type=1)\
            .aggregate(Sum('budget'))
        context['by_research_program'] = Fundfy.objects.values(research_program=F('project_id__investigator_supported__research_program__program_short_name'))\
            .filter(fcfy="2019", fund_type=1)\
            .annotate(Sum('budget')).order_by('-budget__sum')
        context['by_research_program_total'] = Fundfy.objects.values(research_program=F('project_id__investigator_supported__research_program__program_short_name'))\
            .filter(fcfy="2019", fund_type=1)\
            .aggregate(Sum('budget'))
        context['by_division_graph_data'] = get_chart_data()
        return context


class ReportView(generic.TemplateView):
    template_name = 'shared/reports.html'

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        context['title'] = 'Reports'
        return context


def get_chart_data():
    by_division_data = Fundfy.objects.values_list('project_id__investigator_supported__division') \
        .filter(fcfy="2019", fund_type=1) \
        .annotate(Sum('budget')) \
        .order_by('-budget__sum')
    print(by_division_data)
    by_division_graph_labels = []
    for d in by_division_data:
        by_division_graph_labels.append(d[0])
    print(by_division_graph_labels)
    by_division_graph_data = []
    for gd in by_division_data:
         by_division_graph_data.append(gd[1])
    print(by_division_graph_data)
    data = {
             "labels": by_division_graph_labels,
             "data": by_division_graph_data,
         }
    print(data)
    return by_division_graph_labels
