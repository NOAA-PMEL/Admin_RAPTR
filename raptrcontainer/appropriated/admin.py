from django.contrib import admin

from .models import AppropriatedHistory


@admin.register(AppropriatedHistory)
class AppropriatedHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'fiscal_year',
        'source',
        'dollars_received'
    ]
    list_editable = [
        'dollars_received',
    ]
    ordering = [
        'fiscal_year',
    ]
