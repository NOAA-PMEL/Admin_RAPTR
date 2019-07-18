from .query_sets import *
from raptr.models import Fundfy, Project
from shared.models import Contact, Sponsor
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, View
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
from .filters import ContactFilter
from .tables import ContactTable
from django.views import generic
from django.db.models import Sum, F, Count
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
        current_fy = get_current_fy()
        context['title'] = 'Dashboard'
        context['current_fy']=current_fy
        context['by_division'] = get_by_division_data()
        context['by_division_total'] = get_by_division_total()
        context['by_research_program'] = get_by_research_program_data()
        context['by_research_program_total'] = get_by_research_program_total()
        context['open_projects_total'] = get_open_projects_total()
        context['fy_new_funds_count'] = get_fy_new_funds_count()
        context['royalty_funds_received'] = get_royalty_funds_received()
        return context


class ReportView(generic.TemplateView):
    template_name = 'shared/reports.html'

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        context['title'] = 'Reports'
        return context


class DivisionChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        current_fy = get_current_fy()
        by_division_data = Fundfy.objects.values_list('project_id__investigator_supported__division') \
            .filter(fcfy=str(current_fy), fund_type=1) \
            .annotate(Sum('budget')) \
            .order_by('-budget__sum')

        by_division_graph_labels = []
        by_division_graph_data = []
        for d in by_division_data:
            by_division_graph_labels.append(d[0])
            by_division_graph_data.append(d[1])
        labels = by_division_graph_labels
        default_items = by_division_graph_data
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


class ResearchProgramChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        current_fy = get_current_fy()
        by_research_program_data = Fundfy.objects.values_list('project_id__investigator_supported__research_program__program_short_name') \
            .filter(fcfy=str(current_fy), fund_type=1) \
            .annotate(Sum('budget')) \
            .order_by('-budget__sum')

        by_research_program_graph_labels = []
        by_research_program_graph_data = []
        for d in by_research_program_data:
            by_research_program_graph_labels.append(d[0])
            by_research_program_graph_data.append(d[1])
        labels = by_research_program_graph_labels
        default_items = by_research_program_graph_data
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)
