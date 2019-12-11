from django.contrib import admin

from .models import Crada, Filecatlist, Fileupload


class FileuploadInLine(admin.TabularInline):
    model = Fileupload
    extra = 0


@admin.register(Crada)
class CradaAdmin(admin.ModelAdmin):
    list_display = (
        'docket_number',
        'noaa_pi',
        'project_status',
        'activity_phase',
        'project_title',
        'collaborator',
    )
    list_filter = (
        'project_status',
        'activity_phase',
    )
    search_fields = (
        'noaa_pi',
    )
    ordering = (
        'docket_number',
    )
    prepopulated_fields = {
        'slug': ('docket_number',)
    }
    inlines = (
        FileuploadInLine,
    )


class FilecatlistAdmin(admin.ModelAdmin):
    fields = [
        'cat_list',
    ]


admin.site.register(Filecatlist, FilecatlistAdmin)
