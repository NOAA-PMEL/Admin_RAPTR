import datetime

from django.db import models
from django.urls import reverse
from shared.models import Sponsor, Contact

# set the year choices for various drop-downs - earliest data is from 2014
YEAR_CHOICES = []
for yr in range(2014, (datetime.datetime.now().year + 2)):
    YEAR_CHOICES.append((yr, str(yr)))


class Status(models.Model):
    status = models.CharField(
        max_length=20,
        blank=True
    )

    class Meta:
        verbose_name_plural = 'statuses'

    def __str__(self):
        return self.status


# table of Advance, Reimbursable, and Proposed Projects
class Proposal(models.Model):
    proposal_id = models.CharField(
        max_length=10,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Project ID'
    )
    proposal_title = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Project Title'
    )
    investigator_supported = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Investigator Supported',
        related_name='proposal_contact'
    )
    sponsor = models.ForeignKey(
        Sponsor,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    date_submitted = models.DateField(
        blank=True,
        null=True
    )
    proposal_notes = models.TextField(
        blank=True
    )
    year_proposed = models.IntegerField(
        verbose_name='FY Submitted',
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year
    )
    slug = models.SlugField(
        unique=True,
        max_length=10,
    )

    class Meta:
        ordering = ['proposal_id']

    def __str__(self):
        return str(self.proposal_id) \
               + ' - ' \
               + str(self.proposal_number)

    def get_absolute_url(self):
        return reverse('raptr:proposal_detail', kwargs={'slug': self.slug})
