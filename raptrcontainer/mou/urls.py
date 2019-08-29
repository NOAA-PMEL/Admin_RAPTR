from django.urls import path
from . import views

app_name = 'mou'

urlpatterns = [

    path(
        '',
        views.MouListView.as_view(),
        name='mou_list'
    ),
    path(
        'mou/<slug:slug>/',
        views.MouDetailView.as_view(),
        name='mou_detail'
    ),
]