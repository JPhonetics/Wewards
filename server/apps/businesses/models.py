import uuid
from django.db import models
from django_countries.fields import CountryField
from django.conf import settings 
from phonenumber_field.modelfields import PhoneNumberField
from timezone_field import TimeZoneField

class Business(models.Model):
    
    class Meta:
        db_table = 'business'
        verbose_name = 'Business'
        verbose_name_plural = 'Businesses'
        
    id = models.UUIDField(
        verbose_name = 'ID',
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created Date',
        auto_now_add = True,
    )
    modified_date = models.DateTimeField(
        verbose_name = 'Modified Date',
        auto_now = True,
    )
    business_name = models.CharField(
        verbose_name = 'Business Name',
        max_length = 255,
    )
    business_type = models.CharField(
        verbose_name = 'Business Type',
        max_length = 255,
    )
    business_email = models.EmailField(
        verbose_name = 'Business Email',
    )
    business_phone_number = PhoneNumberField(
        verbose_name = 'Business Phone Number',
        max_length = 16,
    )
    website = models.URLField(
        verbose_name = 'Website',
        blank = True,
    )
    logo = models.URLField(
        verbose_name = 'Logo',
        blank = True,
    )
    is_active = models.BooleanField(
        verbose_name = 'Active',
        default = True,
    )
    
    def __str__(self):
        return (
            f"Name:{self.business_name} - "
            f"Type:{self.business_type} - "
            f"Active:{self.is_active}"
        )
    
    
class BusinessLocation(models.Model):
    
    class Meta:
        db_table = 'business_location'
        verbose_name = 'Business Location'
        verbose_name_plural = 'Business Locations'
        
    id = models.UUIDField(
        verbose_name = 'ID',
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
    )
    business = models.ForeignKey(
        Business,
        on_delete = models.CASCADE,
        related_name = 'locations'
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created Date',
        auto_now_add = True,
    )
    modified_date = models.DateTimeField(
        verbose_name = 'Modified Date',
        auto_now = True,
    )
    location_name = models.CharField(
        verbose_name = 'Location Name',
        max_length = 255,
    )
    address_line_1 = models.CharField(
        verbose_name = 'Address Line 1',
        max_length = 255,
    )
    address_line_2 = models.CharField(
        verbose_name = 'Address Line 2',
        max_length = 255,
        blank = True,
    )
    city = models.CharField(
        verbose_name = 'City',
        max_length = 255,
    )
    state_region = models.CharField(
        verbose_name = 'State/Region',
        max_length = 100,
    )
    postal_code = models.CharField(
        verbose_name = 'Postal Code',
        max_length = 20,
    )
    country = CountryField(
        verbose_name = 'Country',
    )
    timezone = TimeZoneField(
        verbose_name = 'Time Zone',
    )
    is_active = models.BooleanField(
        verbose_name = 'Active',
        default = True,
    )
    
    def __str__(self):
        return (
            f"Business:{self.business.business_name} - "
            f"Location:{self.location_name} - "
            f"City:{self.city} State/Region:{self.state_region} - "
            f"Active:{self.is_active}"
        )
    

class BusinessUser(models.Model):
    
    class Meta:
        db_table = 'business_user'
        verbose_name = 'Business User'
        verbose_name_plural = 'Business Users'
        
        # Prevents a user from being added to the same business more than once
        constraints = [
            models.UniqueConstraint(
                fields = ['user', 'business'],
                name = 'unique_user_business',
            )
        ]
        
    class BusinessRoles(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        MANAGER = 'manager', 'Manager'
        EMPLOYEE = 'employee', 'Employee'
        
    id = models.UUIDField(
        verbose_name = 'ID',
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
    )
    business = models.ForeignKey(
        Business,
        on_delete = models.CASCADE,
        related_name = 'business_users',
    )
    # References the configured AUTH_USER_MODEL set in settings.py
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'business_users',
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created Date',
        auto_now_add = True,
    )
    modified_date = models.DateTimeField(
        verbose_name = 'Modified Date',
        auto_now = True,
    )
    role = models.CharField(
        verbose_name = 'Role',
        max_length = 20,
        choices = BusinessRoles.choices,
    )
    is_active = models.BooleanField(
        verbose_name = 'Active',
        default = True,
    )
    
    def __str__(self):
        return (
            f"Business:{self.business.business_name} - "
            f"Name:{self.user.first_name} {self.user.last_name} - "
            f"Role:{self.get_role_display()} - "
            f"Active:{self.is_active}"
        )