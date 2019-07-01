from django.urls import path
from . import views

app_name = 'proposal'

urlpatterns = [
    path(
        'proposal/<slug:slug>/',
        views.ProposalDetailView.as_view(),
        name='proposal_detail'
    ),
    path(
        '',
        views.FilteredProposalListView.as_view(),
        name='proposal_list'
    ),
]
