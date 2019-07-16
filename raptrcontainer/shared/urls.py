from django.urls import path
from . import views

app_name = 'shared'

urlpatterns = [
    path(
        'contact/<slug:slug>/',
        views.ContactDetailView.as_view(),
        name='contact_detail'
    ),
    path(
        'contact/',
        views.FilteredContactListView.as_view(),
        name='contact_list'
    ),
    path(
        'sponsor/<slug:slug>/',
        views.SponsorDetailView.as_view(),
        name='sponsor_detail'
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
        'report/',
        views.ReportView.as_view(),
        name='reports'
    ),
    path(
        'api/data/',
        views.ChartData.as_view(),
        name='api-data'
    ),
]