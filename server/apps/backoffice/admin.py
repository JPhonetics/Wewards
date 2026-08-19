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
        'user',
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
                    'email',
                    'role',
                    'status',
                ),
            },
        ),
    )