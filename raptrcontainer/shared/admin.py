from django.contrib import admin
from .models import Sponsor,Sponsortype, Country, Contact, Program, Affiliation, Optsub, Location


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


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'division',
        'research_program',
        'affiliation',
        'active'
    )
    list_filter = (
        'division',
        'research_program',
        'affiliation',
        'active'
    )
    search_fields = (
        'last_name',
        'first_name'
    )
    ordering = (
        'last_name',
        'first_name'
    )
    prepopulated_fields = {
        'slug': ('last_name', 'first_name')
    }
    readonly_fields = [
        'image_tag',
    ]


class ProgramAdmin(admin.ModelAdmin):
    fields = [
        'program_short_name',
        'program_long_name',
    ]


class AffiliationAdmin(admin.ModelAdmin):
    fields = [
        'affiliation_name',
    ]

class OptsubAdmin(admin.ModelAdmin):
    fields = [
        'opt_sub',
    ]


class LocationAdmin(admin.ModelAdmin):
    fields = [
        'location',
    ]


admin.site.register(Sponsortype, SponsortypeAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Affiliation, AffiliationAdmin)
admin.site.register(Optsub, OptsubAdmin)
admin.site.register(Location, LocationAdmin)