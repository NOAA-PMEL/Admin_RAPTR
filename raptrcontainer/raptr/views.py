from shared.query_sets import *
from .models import Project, RaHistory
from .filters import ProjectFilter
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from .tables import ProjectTable
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import LoginForm
from rest_framework.views import APIView
from rest_framework.response import Response


@method_decorator(login_required, name='dispatch')
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'raptr/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Project Detail'
        context['ra_page'] = 'active'
        return context


@method_decorator(login_required, name='dispatch')
class FilteredProjectListView(SingleTableMixin, FilterView):
    table_class = ProjectTable
    model = Project
    template_name = 'raptr/project_list.html'

    filterset_class = ProjectFilter
    paginate_by = 15

    def get_queryset(self):
        return super(FilteredProjectListView, self).get_queryset().all()

    def get_table_kwargs(self):
        return {'template_name': 'shared/table_bootstrap.html'}

    def get_context_data(self, **kwargs):
        context = super(FilteredProjectListView, self).get_context_data(**kwargs)
        context['title'] = 'Reimbursable & Advance Project List'
        context['ra_page'] = 'active'
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


@method_decorator(login_required, name='dispatch')
class RAHistoryChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        ra_history_data = RaHistory.objects.values_list().order_by('-fiscal_year')[:5]
        ra_history_graph_labels = []
        ra_history_graph_data = []
        for d in reversed(ra_history_data):
            ra_history_graph_labels.append(d[1])
            ra_history_graph_data.append(d[3])
        labels = ra_history_graph_labels
        default_items = ra_history_graph_data
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


@method_decorator(login_required, name='dispatch')
class SponsorTypeChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        by_sponsor_type_data = get_by_sponsor_type_chart_data()
        by_sponsor_type_graph_labels = []
        by_sponsor_type_graph_data = []
        for d in by_sponsor_type_data:
            by_sponsor_type_graph_labels.append(d[0])
            by_sponsor_type_graph_data.append(d[1])
        labels = by_sponsor_type_graph_labels
        default_items = by_sponsor_type_graph_data
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)