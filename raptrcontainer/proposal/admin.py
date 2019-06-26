from django.contrib import admin
from .models import Proposal, Status


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


class StatusAdmin(admin.ModelAdmin):
    fields = [
        'status',
    ]


admin.site.register(Status, StatusAdmin)
