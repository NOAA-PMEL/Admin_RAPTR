from django.db import models
from django.utils.safestring import mark_safe
from phone_field import PhoneField
from djmoney.models.fields import MoneyField
from django.urls import reverse
import datetime

YEAR_CHOICES = []
for yr in range(2014, (datetime.datetime.now().year+2)):
    YEAR_CHOICES.append((yr, str(yr)))


class Filecatlist(models.Model):
    cat_list = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.cat_list

    class Meta:
        verbose_name = 'file category'
        verbose_name_plural = 'file categories'


class Optsub(models.Model):
    opt_sub = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.opt_sub

    class Meta:
        verbose_name = 'OPT Sub'


class Location(models.Model):
    location = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.location


class Status(models.Model):
    status = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = 'statuses'


class Program(models.Model):
    program_short_name = models.CharField(max_length=10, blank=True)
    program_long_name = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['program_short_name']

    def __str__(self):
        return self.program_short_name


class Country (models.Model):
    country_name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name_plural = 'countries'


class Affiliation (models.Model):
    affiliation_name = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.affiliation_name


class Sponsortype (models.Model):
    sponsor_type = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.sponsor_type

    class Meta:
        verbose_name = 'sponsor type'


class Fundtype (models.Model):
    fund_type = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.fund_type

    class Meta:
        verbose_name = 'fund type'


class Fundcodelist (models.Model):
    fund_code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return  self.fund_code

    class Meta:
        verbose_name = 'fund code list'


class Sponsor (models.Model):
    customer_number = models.CharField(max_length=15, unique=True,blank=True, null=True)
    sponsor_acronym = models.CharField(max_length=10, blank=True)
    sponsor_name = models.CharField(max_length=100, blank=True)
    sponsor_type = models.ForeignKey(Sponsortype, on_delete=models.DO_NOTHING, blank=True, null=True)
    sponsor_country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True, null=True)
    sponsor_url = models.URLField(max_length=200, blank=True)

    class Meta:
        ordering = ['sponsor_name']

    def __str__(self):
        return str(self.sponsor_name)+ ' (' + str(self.sponsor_acronym) +')'


class Division (models.Model):
    division_name = models.CharField(max_length=10, blank=True)
    division_description = models.CharField(max_length=50)

    def __str__(self):
        return self.division_name


class Contact(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    photo = models.ImageField('Upload Photo',upload_to='photos', default='photos/no_photo.png', blank=True, null=True)
    email_address = models.EmailField(blank=True,null=True)
    job_title = models.CharField(max_length = 50, blank=True)
    phone_number = PhoneField(blank=True)
    division = models.ForeignKey(Division,on_delete=models.DO_NOTHING, blank=True, null=True)
    opt_sub_group = models.ForeignKey(Optsub,on_delete=models.DO_NOTHING, blank=True, null=True)
    research_program = models.ForeignKey(Program, on_delete=models.DO_NOTHING, blank=True, null=True)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, blank=True, null=True)
    archive = models.BooleanField(null=True, default=False)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return str(self.last_name) + ', ' + str(self.first_name)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.photo))

    def get_absolute_url(self):
        return reverse('raptr:contact_detail', args=(self.pk,))

    image_tag.short_description = 'Photo of Contact'


class Project(models.Model):
    project_id = models.CharField(max_length=10, unique=True, blank=True, null=True)
    project_number = models.CharField(max_length=20, unique=True,blank=True, null=True)
    project_title = models.CharField(max_length=200, blank=True)
    investigator_supported = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=True, null=True)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.DO_NOTHING, blank=True, null=True)
    fund_code = models.ForeignKey(Fundcodelist, on_delete=models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING,blank=True, null=True)
    oar_accept_date = models.DateField(blank=True, null=True)
    project_expiration_date = models.DateField(blank=True, null=True)
    project_notes = models.TextField(blank=True)
    year_proposed = models.IntegerField(verbose_name='FY Proposed', choices=YEAR_CHOICES, default=datetime.datetime.now().year)


    class Meta:
        ordering = ['project_id']

    def __str__(self):
        return str(self.project_id) + ' - ' + str(self.project_number) + ' -- ' + str(self.investigator_supported) + \
               '  -  ' + str(self.sponsor)

    def get_absolute_url(self):
        return reverse('raptr:project_detail', args=(self.pk,))


class Fundfy(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    fcfy = models.CharField(max_length=10, blank=True)
    budget = MoneyField(max_digits=14, decimal_places=2, default_currency = 'USD')
    funds_expire = models.DateField(blank=True, null=True)
    fund_type = models.ForeignKey(Fundtype, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        ordering = ['fcfy']

    def __str__(self):
        return str(self.project_id) + ', ' + str(self.fund_type) + ', ' + str(self.fcfy) + ', ' + str(self.budget)


class Fileupload(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    file_category = models.ForeignKey(Filecatlist, on_delete=models.DO_NOTHING, blank=True, null=True)
    file_upload = models.FileField(upload_to='documents')
