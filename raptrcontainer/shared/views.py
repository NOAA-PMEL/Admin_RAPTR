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


def get_current_fy():
    current_fy = 2000
    if datetime.date.today().month > 9:
        current_fy = datetime.date.today().year + 1
    else:
        current_fy = datetime.date.today().year
    return current_fy


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
        current_fy = get_current_fy()
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['current_fy']=current_fy
        context['by_division'] = Fundfy.objects.values(division=F('project_id__investigator_supported__division'))\
            .filter(fcfy=str(current_fy), fund_type=1)\
            .annotate(Sum('budget'))\
            .order_by('-budget__sum')
        context['by_division_total'] = Fundfy.objects.values(division=F('project_id__investigator_supported__division'))\
            .filter(fcfy=str(current_fy), fund_type=1)\
            .aggregate(Sum('budget'))
        context['by_research_program'] = Fundfy.objects.values(research_program=F('project_id__investigator_supported__research_program__program_short_name'))\
            .filter(fcfy=str(current_fy), fund_type=1)\
            .annotate(Sum('budget')).order_by('-budget__sum')
        context['by_research_program_total'] = Fundfy.objects.values(research_program=F('project_id__investigator_supported__research_program__program_short_name'))\
            .filter(fcfy=str(current_fy), fund_type=1)\
            .aggregate(Sum('budget'))
        context['open_projects_total'] = Project.objects.all().filter(status=2).aggregate(Count('status'))
        context['fy_new_funds_count'] = Fundfy.objects.all().filter(fcfy=str(current_fy), fund_type=1, project_id__status=2).aggregate(Count('fcfy'))
        context['royalty_funds_received'] = Fundfy.objects.all().filter(fcfy=str(current_fy), project_id__fund_code__fund_code='0096').aggregate(Sum('budget'))
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
