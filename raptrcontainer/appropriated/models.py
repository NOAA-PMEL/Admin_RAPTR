from django.db import models
from djmoney.models.fields import MoneyField


SOURCE_CHOICES = (
    ('Base', 'Base'),
    ('OAR', 'OAR'),
    ('Other NOAA', 'Other NOAA'),
)


class AppropriatedHistory(models.Model):
    """

    Stores the historical annual dollars received in appropriated funds.

    """
    fiscal_year = models.CharField(
        max_length=4,
    )
    source = models.CharField(
        max_length=15,
        choices=SOURCE_CHOICES,
        blank=True
    )
    dollars_received = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='USD'
    )

    class Meta:
        ordering = ['fiscal_year']
        verbose_name = 'Appropriated History'
        verbose_name_plural = 'Appropriated History'
