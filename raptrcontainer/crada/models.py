from django.db import models
from shared.models import Sponsor

STATUS_CHOICES = (
    ('Open', 'Open'),
    ('Closed', 'Closed')
)
ACTIVITY_CHOICES =(
    ('Draft', 'Draft'),
    ('Legal Review', 'Legal Review'),
    ('Signed', 'Signed'),
    ('Closed', 'Closed'),
    ('Expired', 'Expired')
)


class Crada (models.Model):
    docket_number = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
        null=True
    )
    project_status = models.CharField(
        max_length=8,
        choices=STATUS_CHOICES,
        blank=True
    )
    activity_phase = models.CharField(
        max_length=8,
        choices=ACTIVITY_CHOICES,
        blank=True
    )
    effective_date = models.DateField(
        blank=True,
        null=True
    )
    expiration_date = models.DateField(
        blank=True,
        null=True
    )
    project_title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Project Title'
    )
    collaborator = models.ForeignKey(
        Sponsor,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    project_summary = models.TextField(
        max_length=750,
        blank=True
    )
    noaa_pi = models.ForeignKey(
        'raptr.Contact',
        on_delete=models.DO_NOTHING,
        verbose_name='NOAA PI',
        blank=True,
        null=True
    )
    partner_pi = models.CharField(
        verbose_name='Partner PI',
        max_length=200,
        blank=True
    )
    partner_contact = models.CharField(
        max_length=50,
        blank=True
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
    )
