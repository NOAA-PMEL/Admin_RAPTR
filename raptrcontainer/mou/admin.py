from django.contrib import admin
from .models import Mou, Fileupload, Filecatlist, Status


class FileuploadInLine(admin.TabularInline):
    model = Fileupload
    extra = 0


@admin.register(Mou)
class MouAdmin(admin.ModelAdmin):
    list_display = (
        'mou_id',
        'investigator_supported',
        'status',
        'mou_title',
        'effective_date',
        'expiration_date',
    )
    list_filter = (
        'status',
        'investigator_supported',
    )
    ordering = (
        'mou_id',
    )
    prepopulated_fields = {
        'slug': ('mou_id',)
    }
    inlines = (
        FileuploadInLine,
    )


class FilecatlistAdmin(admin.ModelAdmin):
    fields = [
        'cat_list',
    ]

class StatusAdmin(admin.ModelAdmin):
    fields = [
        'status',
    ]


admin.site.register(Status, StatusAdmin)
admin.site.register(Filecatlist, FilecatlistAdmin)
