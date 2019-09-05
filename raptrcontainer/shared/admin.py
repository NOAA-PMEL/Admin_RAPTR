from django.contrib import admin
from .models import Sponsor,Sponsortype, Country, Contact, Program, Affiliation, Optsub, Employeetype, Supervisor


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


class EmployeetypeAdmin(admin.ModelAdmin):
    fields = [
        'employee_type'
    ]


class SupervisorAdmin(admin.ModelAdmin):
    fields = [
        'last_name',
        'first_name',
        'active'
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
        'job_title',
        'pay_plan',
        'job_series',
        'employee_band',
        'employee_interval',
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


admin.site.site_header = 'RAPTR Admin Dashboard'
admin.site.register(Sponsortype, SponsortypeAdmin)
admin.site.register(Employeetype, EmployeetypeAdmin)
admin.site.register(Supervisor, SupervisorAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Affiliation, AffiliationAdmin)
admin.site.register(Optsub, OptsubAdmin)