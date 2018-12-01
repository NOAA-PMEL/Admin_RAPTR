from django.views import generic
from .models import Project, Contact, Fundfy, Sponsor
from .filters import ProjectFilter, ContactFilter
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from .tables import ProjectTable, ContactTable
from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
from django.views.generic.detail import DetailView


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'raptr/project_detail.html'


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'raptr/contact_detail.html'


class SponsorDetailView(DetailView):
    model = Sponsor
    template_name = 'raptr/sponsor_detail.html'


class FilteredProjectListView(SingleTableMixin, FilterView):
    table_class = ProjectTable
    model = Project
    template_name = 'raptr/project_list.html'

    filterset_class = ProjectFilter
    paginate_by = 8

    def get_queryset(self):
        return super(FilteredProjectListView, self).get_queryset().all()

    def get_table_kwargs(self):
        return {'template_name': 'raptr/bootstrap.html'}

    def get_context_data(self, **kwargs):
        context = super(FilteredProjectListView, self).get_context_data(**kwargs)
        context['title'] = 'RAPTR Project List'
        return context


class FilteredContactListView(SingleTableMixin, FilterView):
    table_class = ContactTable
    model = Contact
    template_name = 'raptr/contact_list.html'

    filterset_class = ContactFilter
    paginate_by = 12

    def get_queryset(self):
        return super(FilteredContactListView, self).get_queryset().all()

    def get_table_kwargs(self):
        return {'template_name': 'raptr/bootstrap.html'}

    def get_context_data(self, **kwargs):
        context = super(FilteredContactListView, self).get_context_data(**kwargs)
        context['title'] = 'RAPTR Contact List'
        return context


class FundsReceived(generic.ListView):
    model = Project
    template_name = 'raptr/fcfy_report.html'
    context_object_name = 'fcfy_project_list'

    def get_queryset(self):
        all_recs = Fundfy.objects.all().prefetch_related('project_id')
        new_funds_recs = all_recs.filter(fund_type=1)
        fy_funds_recs = new_funds_recs.filter(fcfy='2019')
        return fy_funds_recs


def index(request):
    """Renders the 'home' page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'raptr/index.html',
        {
            'title': 'RAPTR Dashboard',
            'content': 'Welcome to RAPTR',
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'raptr/about.html',
        {
            'title': 'About',
            'message': 'PMEL RAPTR.',
        }
    )


def fcfy_report(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'fcfy_report',
        {
            'report_title': 'FY19 New Funds',
        }
    )
