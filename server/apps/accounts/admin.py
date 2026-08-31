from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.accounts.models import AccountUser


class AccountUserAddForm(forms.ModelForm):
    
    class Meta:
        model = AccountUser
        fields = '__all__'


class AccountUserForm(forms.ModelForm):
    
    class Meta:
        model = AccountUser
        fields = '__all__'
        

@admin.register(AccountUser)

class AccountUserAdmin(UserAdmin):

    add_form = AccountUserAddForm
    form = AccountUserForm

    model = AccountUser
    
    list_display = [
        'last_name',
        'first_name',
        'email',
        'phone_number',
        'is_active',
        'is_staff',
        'is_superuser',
    ]
    
    list_filter = [
        'is_active',
        'is_staff',
        'is_superuser',
    ]
    
    search_fields = [
        'first_name',
        'last_name',
        'email',
        'phone_number',
    ]
    
    ordering = [
        'last_name',
    ]
    
    readonly_fields = [
        'id',
        'created_date',
        'modified_date',
        'last_login',
    ]
    
    fieldsets = (
        (
            'Dates',
            {
                'fields': (
                    'created_date',
                    'modified_date',
                    'last_login',
                )
            },
        ),
        (
            'User Information',
            {
                'fields': (
                    'is_active',
                    'country',
                    'first_name',
                    'last_name',
                    'email',
                    'phone_number',
                )
            },
        ),
        (
            'Access',
            {
                'fields': (
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
    )
        
    add_fieldsets = (
        (
            'Create User',
            {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'country',
                    'first_name',
                    'last_name',
                    'email',
                    'phone_number',
                ),
            },
        ),
    )