from django.db import models
from django.urls import reverse


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

