from django import forms
from django.contrib import admin
from apps.businesses.models import (
    Business,
    BusinessLocation,
    BusinessStaff,
    BusinessItem,
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
        

## Business Admin Portal
class BusinessAdmin(admin.ModelAdmin):

    add_form = BusinessAddForm
    form = BusinessForm

    model = Business
    
    list_display = [
        'name',
        'industry',
        'email',
        'phone_number',
        'website',
        'is_active',
    ]
    
    list_filter = [
        'is_active',
    ]
    
    search_fields = [
        'name',
        'industry',
    ]
    
    ordering = [
        'name',
    ]
    
    readonly_fields = [
        'id',
        'created_date',
        'modified_date',
        'is_active',
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
            'Business Information',
            {
                'fields': (
                    'name',
                    'industry',
                    'email',
                    'phone_number',
                    'website',
                    'logo',
                )
            },
        ),
        (
            'Status',
            {
                'fields': (
                    'is_active',
                )
            },
        ),
    )
        
    add_fieldsets = (
        (
            'Create Business',
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'name',
                    'industry',
                    'email',
                    'phone_number',
                    'website',
                    'logo',
                ),
            },
        ),
    )
    
    
## Business Location Admin Portal
class BusinessLocationAdmin(admin.ModelAdmin):

    add_form = BusinessLocationAddForm
    form = BusinessLocationForm

    model = BusinessLocation
    
    def get_fieldsets(self, request, obj = None):
        if obj is None:
            return self.add_fieldsets

        return self.fieldsets
    
    list_display = [
        'name',
        'address_line_1',
        'city',
        'state_region',
        'postal_code',
    ]
    
    list_filter = [
        'is_active',
    ]
    
    search_fields = [
        'name',
        'city',
        'state_region'
    ]
    
    ordering = [
        'name',
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
            'Business Information',
            {
                'fields': (
                    'name',
                    'address_line_1',
                    'address_line_2',
                    'city',
                    'state_region',
                    'postal_code',
                    'country',
                    'timezone',
                )
            },
        ),
        (
            'Status',
            {
                'fields': (
                    'is_active',
                )
            },
        ),
    )
        
    add_fieldsets = (
        (
            'Create Business Location',
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'business',
                    'name',
                    'address_line_1',
                    'address_line_2',
                    'city',
                    'state_region',
                    'postal_code',
                    'country',
                    'timezone',
                ),
            },
        ),
    )
    
    
## Business Staff Admin Portal
class BusinessStaffAdmin(admin.ModelAdmin):

    add_form = BusinessStaffAddForm
    form = BusinessStaffForm

    model = BusinessStaff
    
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
            'Business Staff Information',
            {
                'fields': (
                    'email',
                    'role',
                )
            },
        ),
        (
            'Status',
            {
                'fields': (
                    'status',
                )
            },
        ),
    )
        
    add_fieldsets = (
        (
            'Create Business Staff',
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'business',
                    'user',
                    'email',
                    'role',
                    'status',
                ),
            },
        ),
    )
    
    
## Business Location Admin Portal
class BusinessItemAdmin(admin.ModelAdmin):

    add_form = BusinessItemAddForm
    form = BusinessItemForm

    model = BusinessItem
    
    def get_fieldsets(self, request, obj = None):
        if obj is None:
            return self.add_fieldsets

        return self.fieldsets
    
    list_display = [
        'name',
        'status',
        'discontinued_date',
    ]
    
    list_filter = [
        'status',
    ]
    
    search_fields = [
        'name',
    ]
    
    ordering = [
        'name',
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
            'Business Item Information',
            {
                'fields': (
                    'name',
                    'description',
                )
            },
        ),
        (
            'Status',
            {
                'fields': (
                    'status',
                    'discontinued_date',
                )
            },
        ),
    )
        
    add_fieldsets = (
        (
            'Create Business Item',
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'business',
                    'name',
                    'description',
                    'status',
                ),
            },
        ),
    )
    
    
admin.site.register(Business, BusinessAdmin)
admin.site.register(BusinessLocation, BusinessLocationAdmin)
admin.site.register(BusinessStaff, BusinessStaffAdmin)
admin.site.register(BusinessItem, BusinessItemAdmin)