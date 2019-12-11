from django import forms
from django.contrib import admin

from .models import Filecatlist, Fileupload, Fundcodelist, Fundfy, Fundtype, Project, RaHistory


class FileuploadInLine(admin.TabularInline):
    model = Fileupload
    extra = 0


class FundfyInLine(admin.TabularInline):
    model = Fundfy
    extra = 0


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

    def clean(self):
        start_date = self.cleaned_data.get('oar_accept_date')
        end_date = self.cleaned_data.get('project_expiration_date')
        if start_date > end_date:
            raise forms.ValidationError('Project Expiration Date must be after OAR Accept Date')
        return self.cleaned_data


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
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


@admin.register(RaHistory)
class RaHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'fiscal_year',
        'dollars_received'
    ]
    list_editable = [
        'dollars_received',
    ]
    ordering = [
        'fiscal_year',
    ]


admin.site.register(Fundtype, FundtypeAdmin)
admin.site.register(Fundcodelist, FundcodelistAdmin)
admin.site.register(Filecatlist, FilecatlistAdmin)
