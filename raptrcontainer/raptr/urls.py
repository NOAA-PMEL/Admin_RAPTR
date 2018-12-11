from django.urls import path
from . import views

app_name = 'raptr'
urlpatterns = [
    path(
        'report/',
        views.ReportView.as_view(),
        name='reports'
    ),
    path(
        'about/',
        views.AboutView.as_view(),
        name='about'
    ),
    path(
        '',
        views.IndexView.as_view(),
        name='index'
    ),
    path(
        'contact/',
        views.FilteredContactListView.as_view(),
        name='contact_list'
    ),
    path(
        'project/<int:pk>/',
        views.ProjectDetailView.as_view(),
        name='project_detail'
    ),
    path(
        'project/',
        views.FilteredProjectListView.as_view(),
        name='project_list'
    ),
    path(
        'contact/<int:pk>/',
        views.ContactDetailView.as_view(),
        name='contact_detail'
    ),
    path(
        'sponsor/<int:pk>/',
        views.SponsorDetailView.as_view(),
        name='sponsor_detail'
    )
]
