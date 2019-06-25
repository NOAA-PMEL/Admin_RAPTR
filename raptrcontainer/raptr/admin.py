from django.contrib import admin
from .models import Contact, Project, Status,\
    Fundfy, Fundtype, Fundcodelist, Fileupload, Filecatlist


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


class FilecatlistAdmin(admin.ModelAdmin):
    fields = [
        'cat_list',
    ]

class StatusAdmin(admin.ModelAdmin):
    fields = [
        'status',
    ]


admin.site.register(Fundtype, FundtypeAdmin)
admin.site.register(Fundcodelist, FundcodelistAdmin)
admin.site.register(Filecatlist, FilecatlistAdmin)
admin.site.register(Status, StatusAdmin)
