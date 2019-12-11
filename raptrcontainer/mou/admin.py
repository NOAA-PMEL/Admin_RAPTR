from django.contrib import admin

from .models import Filecatlist, Fileupload, Mou


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


admin.site.register(Filecatlist, FilecatlistAdmin)
