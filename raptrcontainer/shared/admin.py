from django.contrib import admin
from .models import Sponsor,Sponsortype, Country


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = (
        'sponsor_acronym',
        'sponsor_name',
        'sponsor_type',
        'sponsor_country',
    )
    list_filter = (
        'sponsor_type',
        'sponsor_country'
    )
    search_fields = (
        'sponsor_acronym',
        'sponsor_name'
    )
    prepopulated_fields = {
        'slug': ('sponsor_acronym',)
    }


class SponsortypeAdmin(admin.ModelAdmin):
    fields = [
        'sponsor_type',
    ]


class CountryAdmin(admin.ModelAdmin):
    fields = [
        'country_name',
    ]


admin.site.register(Sponsortype, SponsortypeAdmin)
admin.site.register(Country, CountryAdmin)
