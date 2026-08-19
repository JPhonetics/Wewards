from django import forms
from django.contrib import admin
from apps.backoffice.models import PlatformAdmin


class PlatformAddForm(forms.ModelForm):
    
    class Meta:
        model = PlatformAdmin
        fields = '__all__'


class PlatformAdminForm(forms.ModelForm):
    
    class Meta:
        model = PlatformAdmin
        fields = '__all__'
        
        
@admin.register(PlatformAdmin)

class PlatformAdminAdmin(admin.ModelAdmin):

    add_form = PlatformAddForm
    form = PlatformAdminForm

    model = PlatformAdmin
    
    # Drop down to select primary records
    def get_fieldsets(self, request, obj = None):
        if obj is None:
            return self.add_fieldsets

        return self.fieldsets
    
    list_display = [
        'email',
        'role',
        'status',
    ]
    
    list_filter = [
        'role',
        'status',
    ]
    
    search_fields = [
        'email',
    ]
    
    ordering = [
        'email',
    ]
    
    readonly_fields = [
        'id',
        'created_date',
        'modified_date',
    ]
    
    fieldsets = (
        (
            'Dates',
            {
                'fields': (
                    'created_date',
                    'modified_date',
                )
            },
        ),
        (
            'Platform Admin Information',
            {
                'fields': (
                    'status',
                    'email',
                )
            },
        ),
        (
            'Role',
            {
                'fields': (
                    'role',
                )
            },
        ),
    )
        
    add_fieldsets = (
        (
            'Create Platform Admin',
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'user',
                    'email',
                    'role',
                    'status',
                ),
            },
        ),
    )