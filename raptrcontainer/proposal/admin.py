from django.contrib import admin
from .models import Proposal, Status, Fundtype, Fundfy, Fundcodelist, Filecatlist, Fileupload


class FileuploadInLine(admin.TabularInline):
    model = Fileupload
    extra = 0


class FundfyInLine(admin.TabularInline):
    model = Fundfy
    extra = 0


@admin.register(Proposal)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'proposal_id',
        'proposal_title',
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
        'proposal_id',
    )
    ordering = (
        'proposal_id',
    )
    raw_id_fields = (
        'investigator_supported',
    )
    prepopulated_fields = {
        'slug': ('proposal_id',)
    }
    inlines = (
        FundfyInLine,
        FileuploadInLine
    )


class FundfyAdmin(admin.ModelAdmin):
    fields = [
        'proposal_id',
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


admin.site.register(Status, StatusAdmin)
admin.site.register(Fundtype, FundtypeAdmin)
admin.site.register(Fundcodelist, FundcodelistAdmin)
admin.site.register(Filecatlist, FilecatlistAdmin)
