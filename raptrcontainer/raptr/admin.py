from django.contrib import admin
from .models import Contact, Project, Division, Sponsor, Sponsortype, Program,\
    Country, Affiliation, Status, Fundfy, Fundtype, Fundcodelist, Optsub,\
    Location, Fileupload, Filecatlist


class ContactAdmin(admin.ModelAdmin):
    fields = [
        'first_name',
        'last_name',
        'job_title',
        'email_address',
        'phone_number',
        'division',
        'opt_sub_group',
        'research_program',
        'affiliation',
        'location',
        'image_tag',
        'photo',
        'archive',
    ]
    readonly_fields = [
        'image_tag',
    ]


class FileuploadAdmin(admin.ModelAdmin):
    fields = [
        'file_category',
        'file_upload',
    ]


class FileuploadInLine(admin.StackedInline):
    model = Fileupload
    extra = 0


class FundfyInLine(admin.StackedInline):
    model = Fundfy
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    fields = [
        'year_proposed',
        'project_id',
        'project_number',
        'project_title',
        'investigator_supported',
        'sponsor',
        'fund_code',
        'status',
        'oar_accept_date',
        'project_expiration_date',
        'project_notes',
    ]
    inlines = [
        FundfyInLine,
        FileuploadInLine
    ]


class DivisionAdmin(admin.ModelAdmin):
    fields = [
        'division_name',
        'division_description',
    ]


class SponsorAdmin(admin.ModelAdmin):
    fields = [
        'customer_number',
        'sponsor_acronym',
        'sponsor_name',
        'sponsor_type',
        'sponsor_country',
        'sponsor_url',
    ]


class SponsortypeAdmin(admin.ModelAdmin):
    fields = [
        'sponsor_type',
    ]


class ProgramAdmin(admin.ModelAdmin):
    fields = [
        'program_short_name',
        'program_long_name',
    ]


class CountryAdmin(admin.ModelAdmin):
    fields = [
        'country_name',
    ]


class AffiliationAdmin(admin.ModelAdmin):
    fields = [
        'affiliation_name',
    ]


class StatusAdmin(admin.ModelAdmin):
    fields = [
        'status',
    ]


class FundfyAdmin(admin.ModelAdmin):
    fields = [
        'project_id',
        'fcfy',
        'budget',
        'funds_expire',
        'fund_type',
    ]


class FundtypeAdmin(admin.ModelAdmin):
    fields = [
        'fund_type',
    ]


class FundcodelistAdmin(admin.ModelAdmin):
    fields = [
        'fund_code',
    ]


class OptsubAdmin(admin.ModelAdmin):
    fields = [
        'opt_sub',
    ]


class LocationAdmin(admin.ModelAdmin):
    fields = [
        'location',
    ]


class FilecatlistAdmin(admin.ModelAdmin):
    fields = [
        'cat_list',
    ]


admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Sponsortype, SponsortypeAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Affiliation, AffiliationAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Fundtype, FundtypeAdmin)
admin.site.register(Fundcodelist, FundcodelistAdmin)
admin.site.register(Optsub, OptsubAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Filecatlist, FilecatlistAdmin)
