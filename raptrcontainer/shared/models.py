from django.core.validators import EmailValidator, MaxValueValidator, MinValueValidator
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

FLSA_CHOICES = (
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
    ('00', '00'),
    ('I', 'I'),
    ('II', 'II'),
    ('III', 'III'),
    ('IV', 'IV'),
    ('V', 'V'),
)

PAY_INTERVAL_CHOICES = (
    ('00', '00'),
    ('01', '01'),
    ('02', '02'),
    ('03', '03'),
    ('04', '04'),
    ('05', '05'),
)

LOCATIONS = (
    ('Seattle', 'Seattle'),
    ('Newport', 'Newport'),
    ('Hawaii', 'Hawaii'),
    ('Other', 'Other'),
)


class Country(models.Model):
    """

    Stores a list of sponsor countries, related to :model:`shared.Sponsor`.

    """
    country_name = models.CharField(
        max_length=20,
        blank=True
    )

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country_name


class Sponsortype(models.Model):
    """

    Stores a list of sponsor categories, related to :model:`shared.Sponsor`.

    """
    sponsor_type = models.CharField(
        max_length=50,
        blank=True
    )

    class Meta:
        verbose_name = 'Sponsor Type'
        verbose_name_plural = 'Sponsor Types'

    def __str__(self):
        return self.sponsor_type


class Sponsor(models.Model):
    """

    Stores information about sponsors PMEL does business with, related to model:`raptr.Project`, model:`crada.Crada`,
    and model:`proposal.Proposal`

    """
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


class Optsub(models.Model):
    """

    Stores a list of OPT codes for the employee's Division, related to :model:`shared.Contact`.

    """
    opt_sub = models.CharField(
        max_length=20,
        blank=True
    )

    class Meta:
        verbose_name = 'OPT Sub'
        verbose_name_plural = 'OPT Subs'

    def __str__(self):
        return self.opt_sub


class Program(models.Model):
    """

    Stores a list of research programs, related to :model:`shared.Contact`.

    """
    program_short_name = models.CharField(
        max_length=20,
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


class Affiliation(models.Model):
    """

    Stores a list of organizations that PMEL workers can be affiliated with, related to :model:`shared.Contact`.

    """
    affiliation_name = models.CharField(
        max_length=30,
        blank=True
    )

    active = models.BooleanField(
        default=True,
        help_text='Uncheck when the affiliation is no longer used.'
    )

    def __str__(self):
        return self.affiliation_name


class Employeetype(models.Model):
    """

    Stores a list of employee types, related to :model:`shared.Contact`.

    """
    employee_type = models.CharField(
        max_length=15,
        blank=True
    )

    class Meta:
        verbose_name = 'Employee Type'
        verbose_name_plural = 'Employee Types'

    def __str__(self):
        return self.employee_type


class Supervisor(models.Model):
    """

    Stores a list of employee supervisors, related to :model:`shared.Contact`.

    """
    last_name = models.CharField(
        max_length=15,
        blank=True
    )
    first_name = models.CharField(
        max_length=15,
        blank=True
    )
    active = models.BooleanField(
        default=True,
        help_text='Is the person still at a supervisor?'
    )

    def __str__(self):
        return self.last_name


class Contact(models.Model):
    """

    Stores a list of PMEL workers, related to :model:`raptr.Project`, :model:`proposal.Proposal`, :model:`crada.Crada`.

    """
    full_time_equivalent = models.FloatField(
        blank=True,
        default=1.0,
        validators=[
            MinValueValidator(0.0, message='FTEs must be between 0 and 1.'),
            MaxValueValidator(1.0, message='FTEs must be between 0 and 1.')
        ]
    )
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
        validators=[
            EmailValidator(),
        ],
        blank=True,
        null=True
    )
    phone_number = PhoneField(
        blank=True
    )
    room_number = models.CharField(
        max_length=15,
        blank=True
    )
    job_title = models.CharField(
        max_length=50,
        blank=True
    )
    division = models.CharField(
        choices=DIVISION_CHOICES,
        max_length=4,
        blank=True,
    )
    opt_sub_group = models.ForeignKey(
        Optsub,
        on_delete=models.DO_NOTHING,
        verbose_name='OPT Sub Group',
        blank=True,
        null=True
    )
    research_program = models.ForeignKey(
        Program,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    pay_plan = models.CharField(
        choices=GRADE_CHOICES,
        max_length=4,
        blank=True
    )
    job_series = models.CharField(
        max_length=4,
        blank=True
    )
    employee_band = models.CharField(
        choices=PAY_BAND_CHOICES,
        verbose_name='band',
        max_length=4,
        blank=True
    )
    employee_interval = models.CharField(
        choices=PAY_INTERVAL_CHOICES,
        verbose_name='interval',
        max_length=4,
        blank=True
    )
    service_computation_date = models.DateField(
        blank=True,
        null=True,
        help_text='Employee\'s retirement service computation date.'
    )
    flsa_status = models.CharField(
        verbose_name='FLSA Status',
        choices=FLSA_CHOICES,
        max_length=4,
        blank=True,
        help_text='Is the person Fair Labor Standards Act (E)xempt or (N)on Exempt?'
    )
    supervisor = models.ForeignKey(
        Supervisor,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    pmel_base = models.BooleanField(
        default=False,
        verbose_name='PMEL Base',
        help_text='Is the position funded by PMEL Base Funds?'
    )
    employee_type = models.ForeignKey(
        Employeetype,
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
    is_pi = models.BooleanField(
        default=False,
        verbose_name='PI?',
        help_text='Is this person a PMEL Principal Investigator?'
    )
    location = models.CharField(
        choices=LOCATIONS,
        max_length=15,
        blank=True
    )
    entry_on_duty = models.DateField(
        verbose_name='EOD',
        blank=True,
        null=True,
        help_text='Date person entered duty at PMEL.'
    )
    departure_date = models.DateField(
        blank=True,
        null=True,
        help_text='Date person left PMEL'
    )
    active = models.BooleanField(
        default=True,
        help_text='Is the person still at PMEL? Uncheck when departure date is entered.'
    )
    photo = models.ImageField(
        verbose_name='Upload Photo',
        upload_to='photos',
        default='photos/no_photo.png',
        blank=True,
        null=True
    )
    slug = models.SlugField(
        help_text="A short label, used in the URLs to camouflage the primary key "
                  "- autogenerated == last_name - first_name.",
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
