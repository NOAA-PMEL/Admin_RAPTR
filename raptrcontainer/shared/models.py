from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from phone_field import PhoneField


GRADE_CHOICES = (
    ('ZA', 'ZA'),
    ('ZP', 'ZP'),
    ('ZS', 'ZS'),
    ('ZT', 'ZT'),
    ('ST', 'ST'),
    ('ES', 'ES'),
    ('GS', 'GS'),
    ('WG', 'WG'),
)

FLSA_CHOICES =(
    ('E', 'E'),
    ('N', 'N'),
)

DIVISION_CHOICES = (
    ('AD', 'AD'),
    ('CS', 'CS'),
    ('ED', 'ED'),
    ('OC', 'OC'),
    ('OD', 'OD'),
    ('OE', 'OE'),
)

PAY_BAND_CHOICES = (
    ('I', 'I'),
    ('II', 'II'),
    ('III', 'III'),
    ('IV', 'IV'),
    ('V', 'V'),
)

PAY_INTERVAL_CHOICES = (
    ('01', '01'),
    ('02', '02'),
    ('03', '03'),
    ('04', '04'),
    ('05', '05'),
)


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
        blank=True
    )

    slug = models.SlugField(
        unique=True,
        max_length=10,
    )

    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'
        ordering = ['sponsor_name']

    def __str__(self):
        return str(self.sponsor_name) + ' (' + str(self.sponsor_acronym) + ')'

    def get_absolute_url(self):
        return reverse('shared:sponsor_detail', kwargs={'slug': self.slug})


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


class Program(models.Model):
    """

    Provides an editable list of research programs, related to :model:'shared.Contact'.

    """
    program_short_name = models.CharField(
        max_length=10,
        blank=True
    )
    program_long_name = models.CharField(
        max_length=100,
        blank=True
    )
    active = models.BooleanField(
        help_text='Is the Research Program still active for use?',
        default=True
    )

    class Meta:
        verbose_name = 'Research Program'
        verbose_name_plural = 'Research Programs'
        ordering = ['program_short_name']

    def __str__(self):
        return self.program_short_name


# support table for the Affiliation drop-down in the contacts view
# foreign key is in the Contacts model
class Affiliation(models.Model):
    affiliation_name = models.CharField(
        max_length=10,
        blank=True
    )

    def __str__(self):
        return self.affiliation_name


# table of PMEL contacts (PIs)
# foreign key is in the Project model
class Contact(models.Model):
    position_billet = models.CharField(
        max_length=10,
        blank=True,
    )
    position_id = models.CharField(
        max_length=12,
        blank=True
    )
    last_name = models.CharField(
        max_length=50
    )
    first_name = models.CharField(
        max_length=50
    )
    email_address = models.EmailField(
        blank=True,
        null=True
    )
    job_title = models.CharField(
        max_length=50,
        blank=True
    )
    pay_plan = models.CharField(
        max_length=4,
        choices=GRADE_CHOICES,
        blank=True
    )
    job_series = models.CharField(
        max_length=4,
        blank=True
    )
    employee_band = models.CharField(
        choices=PAY_BAND_CHOICES,
        max_length=4,
        blank=True
    )
    employee_interval = models.CharField(
        choices=PAY_INTERVAL_CHOICES,
        max_length=4,
        blank=True
    )
    flsa_status = models.CharField(
        max_length=4,
        choices=FLSA_CHOICES,
        blank=True
    )
    phone_number = PhoneField(
        blank=True
    )
    division = models.CharField(
        max_length=4,
        choices=DIVISION_CHOICES,
        blank=True,
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
    active = models.BooleanField(
        default=True
    )
    photo = models.ImageField(
        verbose_name='Upload Photo',
        upload_to='photos',
        default='photos/no_photo.png',
        blank=True,
        null=True
    )
    slug = models.SlugField(
        unique=True,
        max_length=100,
    )

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return str(self.last_name) + ', ' + str(self.first_name)

    def get_absolute_url(self):
        return reverse('shared:contact_detail', kwargs={'slug': self.slug})

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="150" height="150" />'
                         % (self.photo))

    image_tag.short_description = 'Photo of Contact'
