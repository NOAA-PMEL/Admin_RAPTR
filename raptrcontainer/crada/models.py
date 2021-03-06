from django.db import models
from django.urls import reverse

from shared.models import Contact, Sponsor

STATUS_CHOICES = (
    ('Open', 'Open'),
    ('Closed', 'Closed'),
    ('In Progress', 'In Progress')
)
ACTIVITY_CHOICES = (
    ('Draft', 'Draft'),
    ('Legal Review', 'Legal Review'),
    ('Signed', 'Signed'),
    ('Closed', 'Closed'),
    ('Expired', 'Expired')
)


class Crada (models.Model):
    """

    Stores information about PMEL Cooperative Research And Development Agreements (CRADAs).

    """
    docket_number = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
        null=True
    )
    project_status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        blank=True
    )
    activity_phase = models.CharField(
        max_length=15,
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
        Contact,
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
        help_text="A short label, used in the URLs to camouflage the primary key - autogenerated == docket_number.",
        unique=True,
        max_length=50,
    )

    class Meta:
        verbose_name = 'CRADA',
        verbose_name_plural = 'CRADAs'
        ordering = ['docket_number']

    def get_absolute_url(self):
        return reverse('crada:crada_detail', kwargs={'slug': self.slug})


class Filecatlist(models.Model):
    """

    Stores a list of categories for CRADA file uploads, related to :model: 'crada.Crada'.

    """

    cat_list = models.CharField(
        max_length=50,
        blank=True
    )

    class Meta:
        verbose_name = 'file category'
        verbose_name_plural = 'file categories'

    def __str__(self):
        return self.cat_list


class Fileupload(models.Model):
    """

    Uploads CRADA files to media/documents/cradas, related to :model: `crada.Crada`.

    """
    docket_number = models.ForeignKey(
        Crada,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    file_category = models.ForeignKey(
        Filecatlist,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    file_upload = models.FileField(
        upload_to='documents\\cradas'
    )
