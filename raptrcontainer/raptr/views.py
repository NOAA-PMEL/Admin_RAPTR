from django.views import generic
from .models import Project, Contact, Fundfy, Sponsor
from .filters import ProjectFilter
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin, MultiTableMixin
from .tables import ProjectTable
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
        return {'template_name': 'shared/bootstrap.html'}

    def get_context_data(self, **kwargs):
        context = super(FilteredProjectListView, self).get_context_data(**kwargs)
        context['title'] = 'Reimbursable & Advance Project List'
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
