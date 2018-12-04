from django.db import models
from django.utils.safestring import mark_safe
from phone_field import PhoneField
from djmoney.models.fields import MoneyField
from django.urls import reverse
import datetime

# set the year choices for various drop-downs - earliest data is from 2014
YEAR_CHOICES = []
for yr in range(2014, (datetime.datetime.now().year + 2)):
    YEAR_CHOICES.append((yr, str(yr)))


# support table for the file category drop-down in the projects view
# foreign key is in the Project model
class Filecatlist(models.Model):
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


# support table for the OPT Sub Group drop-down in the contacts view
# foreign key is in the Contact model
class Optsub(models.Model):
    opt_sub = models.CharField(
        max_length=20,
        blank=True
    )

    class Meta:
        verbose_name = 'OPT Sub'
        verbose_name_plural = 'OPT Subs'

    def __str__(self):
        return self.opt_sub


# support table for the Location drop-down in the contacts view
# foreign key is in the Contact model
class Location(models.Model):
    location = models.CharField(
        max_length=20,
        blank=True
    )

    def __str__(self):
        return self.location


# support table for the Research Program drop-down in the contacts view
# foreign key is in the Contact model
class Program(models.Model):
    program_short_name = models.CharField(
        max_length=10,
        blank=True
    )
    program_long_name = models.CharField(
        max_length=100,
        blank=True
    )

    class Meta:
        verbose_name = 'Research Program'
        verbose_name_plural = 'Research Programs'
        ordering = ['program_short_name']

    def __str__(self):
        return self.program_short_name


# support table for the Division drop-down in the contacts view
# foreign key is in the Contact model
class Division(models.Model):
    division_name = models.CharField(
        max_length=10,
        blank=True
    )
    division_description = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.division_name


# support table for the Affiliation drop-down in the contacts view
# foreign key is in the Contacts model
class Affiliation(models.Model):
    affiliation_name = models.CharField(
        max_length=10,
        blank=True
    )

    def __str__(self):
        return self.affiliation_name


# support table for the Country drop-down in the sponsors view
# foreign key is in the Sponsor model
class Country(models.Model):
    country_name = models.CharField(
        max_length=20,
        blank=True
    )

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country_name


# support table for the Sponsor Type drop-down in the sponsor view
# foreign key is in the Sponsor model
class Sponsortype(models.Model):
    sponsor_type = models.CharField(
        max_length=50,
        blank=True
    )

    class Meta:
        verbose_name = 'Sponsor Type'
        verbose_name_plural = 'Sponsor Types'

    def __str__(self):
        return self.sponsor_type


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


# table of all of the sponsors PMEL does business with
# this model supports the Sponsor drop-down in the project view
# foreign key is in the Project model
class Sponsor(models.Model):
    customer_number = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
        null=True
    )
    sponsor_acronym = models.CharField(
        max_length=10,
        blank=True
    )
    sponsor_name = models.CharField(
        max_length=100,
        blank=True
    )
    sponsor_type = models.ForeignKey(
        Sponsortype,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    sponsor_country = models.ForeignKey(
        Country,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    sponsor_url = models.URLField(
        max_length=200,
        blank=True)

    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'
        ordering = ['sponsor_name']

    def __str__(self):
        return str(self.sponsor_name) + ' (' + str(self.sponsor_acronym) + ')'

    def get_absolute_url(self):
        return reverse('raptr:sponsor_detail', args=(self.pk,))


# table of PMEL contacts (PIs)
# foreign key is in the Project model
class Contact(models.Model):
    last_name = models.CharField(
        max_length=50
    )
    first_name = models.CharField(
        max_length=50
    )
    photo = models.ImageField(
        verbose_name='Upload Photo',
        upload_to='photos',
        default='photos/no_photo.png',
        blank=True,
        null=True
    )
    email_address = models.EmailField(
        blank=True,
        null=True
    )
    job_title = models.CharField(
        max_length=50,
        blank=True
    )
    phone_number = PhoneField(
        blank=True
    )
    division = models.ForeignKey(
        Division,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    opt_sub_group = models.ForeignKey(
        Optsub,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    research_program = models.ForeignKey(
        Program,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    affiliation = models.ForeignKey(
        Affiliation,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    archive = models.BooleanField(
        null=True,
        default=False
    )

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return str(self.last_name) + ', ' + str(self.first_name)

    def get_absolute_url(self):
        return reverse('raptr:contact_detail', args=(self.pk,))

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />'
                         % (self.photo))

    image_tag.short_description = 'Photo of Contact'


# table of Advance, Reimbursable, and Proposed Projects
class Project(models.Model):
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
        verbose_name='Investigator Supported'
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
        verbose_name='FY Proposed',
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year
    )

    class Meta:
        ordering = ['project_id']

    def __str__(self):
        return str(self.project_id) \
               + ' - ' \
               + str(self.project_number) \
               + ' -- ' \
               + str(self.investigator_supported) \
               + '  -  ' \
               + str(self.sponsor)

    def get_absolute_url(self):
        return reverse('raptr:project_detail', args=(self.pk,))


class Fundfy(models.Model):
    project_id = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        blank=True,
        null=True
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
