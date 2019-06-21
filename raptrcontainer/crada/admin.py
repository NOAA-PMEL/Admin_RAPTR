from django.contrib import admin
from .models import Crada


@admin.register(Crada)
class CradaAdmin(admin.ModelAdmin):
    list_display = (
        'docket_number',
        'noaa_pi',
        'project_status',
        'activity_phase',
        'project_title',
    )
    list_filter = (
        'noaa_pi',
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
