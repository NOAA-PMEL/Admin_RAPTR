from django.urls import path
from . import views

app_name = 'crada'

urlpatterns = [

    path(
        '',
        views.CradaListView.as_view(),
        name='crada_list'
    ),
]
