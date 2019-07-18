from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

app_name = 'raptr'

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('raptr:password_change_done')),
        name='password_change'
    ),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),
    path(
        'project/<slug:slug>/',
        views.ProjectDetailView.as_view(),
        name='project_detail'
    ),
    path(
        'project/',
        views.FilteredProjectListView.as_view(),
        name='project_list'
    ),
    path(
        'api/data/3/',
        views.RAHistoryChartData.as_view(),
        name='history-data'
    ),
    path(
        'api/data/4/',
        views.SponsorTypeChartData.as_view(),
        name='sponsor-type-data'
    )
]
