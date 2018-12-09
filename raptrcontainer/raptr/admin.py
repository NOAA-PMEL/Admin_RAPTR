from django.contrib import admin
from .models import Contact, Project, Division, Sponsor, Sponsortype, Program,\
    Country, Affiliation, Status, Fundfy, Fundtype, Fundcodelist, Optsub,\
    Location, Fileupload, Filecatlist


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'division',
        'research_program',
    )
    list_filter = (
        'division',
        'research_program'
    )
    search_fields = (
        'last_name',
        'first_name'
    )
    ordering = (
        'last_name',
        'first_name'
    )
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


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'year_proposed',
        'project_id',
        'project_number',
        'project_title',
        'investigator_supported',
        'sponsor',
        'status',
    )
    list_filter = (
        'year_proposed',
        'status'
    )
    search_fields = (
        'project_id',
        'project_number',
    )
    ordering = (
        'project_id',
        'project_number'
    )
    raw_id_fields = (
        'investigator_supported',
    )
    inlines = (
        FundfyInLine,
        FileuploadInLine
    )


class DivisionAdmin(admin.ModelAdmin):
    fields = [
        'division_name',
        'division_description',
    ]


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


admin.site.register(Division, DivisionAdmin)
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
