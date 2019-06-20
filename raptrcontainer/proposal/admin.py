from django.contrib import admin
from .models import Proposal


@admin.register(Proposal)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'proposal_id',
        'proposal_number',
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
        'proposal_number',
    )
    ordering = (
        'proposal_id',
        'proposal_number'
    )
    raw_id_fields = (
        'investigator_supported',
    )
    prepopulated_fields = {
        'slug': ('proposal_id',)
    }



