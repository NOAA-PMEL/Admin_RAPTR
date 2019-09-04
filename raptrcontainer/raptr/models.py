import datetime
from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse
from shared.models import Sponsor, Contact

STATUS_CHOICES = (
    ('Open', 'Open'),
    ('Closed', 'Closed'),
    ('In Progress', 'In Progress'),
    ('Active','Active'),
    ('Cancelled', 'Cancelled')
)

# set the year choices for various drop-downs - earliest data is from 2014
YEAR_CHOICES = []
for yr in range(2014, (datetime.datetime.now().year + 2)):
    YEAR_CHOICES.append((yr, str(yr)))


class Filecatlist(models.Model):
    """

    Stores list of categories for project file uploads, related to :model:`raptr.Fileupload`.

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


class Fundtype(models.Model):
    """

    Stores the status of funding (e.g. new, carry over, proposed, etc.), related to :model:`project.Fundfy`.

    """
    fund_type = models.CharField(
        max_length=25,
        blank=True
    )

    class Meta:
        verbose_name = 'Fund Type'
        verbose_name_plural = 'Fund Types'

    def __str__(self):
        return self.fund_type


class Fundcodelist(models.Model):
    """

    Stores a list of the fund codes, related to :model:`raptr.Fundfy`

    """
    fund_code = models.CharField(
        max_length=10,
        blank=True
    )

    class Meta:
        verbose_name = 'Fund Code List'

    def __str__(self):
        return self.fund_code


# TODO: Add validators to oar_accept_date and project_expiration_date
class Project(models.Model):
    """

    Stores information about PMEL Reimbursable and Advance Agreements.

    """
    project_id = models.CharField(
        help_text="The PMEL FY-## project designator.",
        max_length=10,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Project ID'
    )
    project_number = models.CharField(
        help_text="The CBS Project-Task code.",
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Project Number'
    )
    slug = models.SlugField(
        help_text="A short label, used in the URLs to camouflage the primary key - autogenerated == project_id.",
        unique=True,
        max_length=10,
    )
    project_title = models.CharField(
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
        related_name='contact'
    )
    sponsor = models.ForeignKey(
        Sponsor,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    fund_code = models.ForeignKey(
        Fundcodelist,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        blank=True
    )
    oar_accept_date = models.DateField(
        blank=True,
        null=True
    )
    project_expiration_date = models.DateField(
        blank=True,
        null=True
    )
    project_notes = models.TextField(
        blank=True
    )
    year_proposed = models.IntegerField(
        verbose_name='FY Submitted',
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year
    )

    class Meta:
        ordering = ['project_id']

    def __str__(self):
        return str(self.project_id) \
               + ' - ' \
               + str(self.project_number)

    def get_absolute_url(self):
        return reverse('raptr:project_detail', kwargs={'slug': self.slug})


class Fundfy(models.Model):
    """

    Stores the funds proposed, received, and carried over. Related to :model:`raptr.Project`.

    """
    project_id = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    fcfy = models.CharField(
        max_length=10,
        blank=True
    )
    budget = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='USD'
    )
    funds_expire = models.DateField(
        blank=True,
        null=True
    )
    # TODO: consider changing to an enumerated list - will this change that often?
    fund_type = models.ForeignKey(
        Fundtype,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['fcfy']

    def __str__(self):
        return str(self.project_id) \
               + ', '\
               + str(self.fund_type)\
               + ', '\
               + str(self.fcfy)\
               + ', '\
               + str(self.budget)


class Fileupload(models.Model):
    """

    Uploads Project files to media/documents/projects, related to :model:`raptr.Project`.

    """
    project_id = models.ForeignKey(
        Project,
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
        upload_to='documents/projects'
    )


class RaHistory(models.Model):
    """

    Stores the historical annual dollars received in R&A funds.

    """
    fiscal_year = models.CharField(
        max_length=4,
    )
    dollars_received = models.DecimalField(
        max_digits=14,
        decimal_places=2,
    )
    
    class Meta:
        ordering = ['fiscal_year']
        verbose_name='RA History'
        verbose_name_plural = 'RA History'
