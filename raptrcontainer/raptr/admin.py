from django.contrib import admin
from .models import Contact, Project, Program, Affiliation, Status,\
    Fundfy, Fundtype, Fundcodelist, Optsub,\
    Location, Fileupload, Filecatlist


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
        'project_id',
        'project_number',
        'project_title',
        'investigator_supported',
        'sponsor',
        'status',
        'year_proposed',
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
    prepopulated_fields = {
        'slug': ('project_id',)
    }
    inlines = (
        FundfyInLine,
        FileuploadInLine
    )


class ProgramAdmin(admin.ModelAdmin):
    fields = [
        'program_short_name',
        'program_long_name',
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


admin.site.register(Program, ProgramAdmin)
admin.site.register(Affiliation, AffiliationAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Fundtype, FundtypeAdmin)
admin.site.register(Fundcodelist, FundcodelistAdmin)
admin.site.register(Optsub, OptsubAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Filecatlist, FilecatlistAdmin)
