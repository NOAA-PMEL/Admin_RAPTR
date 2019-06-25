import datetime
from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse
from shared.models import Sponsor, Contact


# set the year choices for various drop-downs - earliest data is from 2014
YEAR_CHOICES = []
for yr in range(2014, (datetime.datetime.now().year + 2)):
    YEAR_CHOICES.append((yr, str(yr)))


# support table for the file category drop-down in the projects view
# foreign key is in the Project model
class Filecatlist(models.Model):
    """

    An editable list of categories for project file uploads, related to :model: 'shared.Project'

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


# support table for the Status drop-down in the projects view
# foreign key is in the Project Model
class Status(models.Model):
    status = models.CharField(
        max_length=20,
        blank=True
    )

    class Meta:
        verbose_name_plural = 'statuses'

    def __str__(self):
        return self.status


class Fundtype(models.Model):
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
    fund_code = models.CharField(
        max_length=10,
        blank=True
    )

    class Meta:
        verbose_name = 'Fund Code List'

    def __str__(self):
        return self.fund_code


# table of Advance, Reimbursable, and Proposed Projects
class Project(models.Model):
    """

    Stores information about PMEL Reimbursable and Advance Agreements

    """
    project_id = models.CharField(
        max_length=10,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Project ID'
    )
    project_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Project Number'
    )
    slug = models.SlugField(
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
    status = models.ForeignKey(
        Status,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
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
        upload_to='documents'
    )
