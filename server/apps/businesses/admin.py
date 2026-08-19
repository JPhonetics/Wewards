from django import forms
from django.contrib import admin
from apps.businesses.models import (
    Business,
    BusinessLocation,
    BusinessStaff,
    BusinessItem
)

## Business Forms
class BusinessAddForm(forms.ModelForm):
    
    class Meta:
        model = Business
        fields = '__all__'


class BusinessForm(forms.ModelForm):
    
    class Meta:
        model = Business
        fields = '__all__'
        

## Business Location Forms       
class BusinessLocationAddForm(forms.ModelForm):
    
    class Meta:
        model = BusinessLocation
        fields = '__all__'


class BusinessLocationForm(forms.ModelForm):
    
    class Meta:
        model = BusinessLocation
        fields = '__all__'
        
        
## Business Staff Forms
class BusinessStaffAddForm(forms.ModelForm):
    
    class Meta:
        model = BusinessStaff
        fields = '__all__'


class BusinessStaffForm(forms.ModelForm):
    
    class Meta:
        model = BusinessStaff
        fields = '__all__'
        

## Business Item Forms        
class BusinessItemAddForm(forms.ModelForm):
    
    class Meta:
        model = BusinessItem
        fields = '__all__'


class BusinessItemForm(forms.ModelForm):
    
    class Meta:
        model = BusinessItem
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