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
        'sponsor/<slug:slug>/',
        views.SponsorDetailView.as_view(),
        name='sponsor_detail'
    ),
]