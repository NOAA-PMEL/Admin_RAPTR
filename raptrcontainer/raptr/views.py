from django.views import generic
from .models import Project, Contact, Fundfy, Sponsor
from .filters import ProjectFilter, ContactFilter
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin, MultiTableMixin
from .tables import ProjectTable, ContactTable, NewFundsTable
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'raptr/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Project Detail'
        return context


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
        return super(FilteredContactListView, self).get_queryset().filter(active=True)

    def get_table_kwargs(self):
        return {'template_name': 'raptr/bootstrap.html'}

    def get_context_data(self, **kwargs):
        context = super(FilteredContactListView, self).get_context_data(**kwargs)
        context['title'] = 'RAPTR Contact List'
        return context


class ReportView(generic.TemplateView):
    template_name = 'raptr/reports.html'

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        context['title'] = 'RAPTR Reports'
        return context


class IndexView(MultiTableMixin, TemplateView):
    table_class = NewFundsTable
    model = Fundfy
    template_name = 'raptr/index.html'

    def get_tables(self):
        fy_funds_received = Fundfy.objects.filter(fcfy="2019", fund_type = 1).order_by('project_id')
        return [NewFundsTable(fy_funds_received)]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'RAPTR Dashboard'
        return context


class AboutView(TemplateView):
    template_name = 'raptr/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['title'] = 'About RAPTR'
        return context


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
