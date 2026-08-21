import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django_countries.fields import CountryField
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from timezone_field import TimeZoneField
from core.choices import (
    BusinessRoleChoices,
    ItemStatusChoices,
    UserStatusChoices,
)
from core.lookups import (
    get_account_user,
    get_business,
)


class BusinessStaffManager(BaseUserManager):
    
    def create_business_staff(
        self,
        business_id: uuid.UUID,
        user_id: uuid.UUID,
        staff_email: str,
        role: str,
        **extra_fields
    ):
        business = get_business(business_id)
        
        user = get_account_user(user_id)
        
        staff_email = self.normalize_email(staff_email.strip().casefold())
        
        staff = self.model(
            business = business,
            user = user,
            email = staff_email,
            role = role,
            **extra_fields,
        )
        
        staff.full_clean()
        staff.save(using=self._db)
        
        return staff


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
    country = CountryField(
        verbose_name = 'Country',
        default = 'US',
    )
    name = models.CharField(
        verbose_name = 'Business Name',
        max_length = 255,
    )
    industry = models.CharField(
        verbose_name = 'Industry',
        max_length = 255,
    )
    email = models.EmailField(
        verbose_name = 'Business Email',
    )
    phone_number = PhoneNumberField(
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
            f"Name: {self.name} - "
            f"Industry: {self.industry} - "
            f"Active: {self.is_active}"
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
    name = models.CharField(
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
            f"Business: {self.business.name} - "
            f"Location: {self.name} - "
            f"City: {self.city} State/Region: {self.state_region} - "
            f"Active: {self.is_active}"
        )
    

class BusinessStaff(models.Model):
    
    class Meta:
        db_table = 'business_staff'
        verbose_name = 'Business Staff'
        verbose_name_plural = 'Business Staff'
        
        constraints = [
            # Prevents a user from being added to the same business more than once
            models.UniqueConstraint(
                fields = ['business', 'user'],
                name = 'unique_business_user',
            ),
            # Prevents the same email being used at the same business
            models.UniqueConstraint(
                fields = ['business', 'email'],
                name = 'unique_business_staff_email',
            ),
        ]
        
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
    business = models.ForeignKey(
        Business,
        on_delete = models.CASCADE,
        related_name = 'staff',
    )
    # References the configured AUTH_USER_MODEL set in settings.py
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'business_staff',
    )
    email = models.EmailField(
        verbose_name='Staff Email',
    )
    role = models.CharField(
        verbose_name = 'Role',
        max_length = 20,
        choices = BusinessRoleChoices.choices,
    )
    status = models.CharField(
        verbose_name = 'Status',
        max_length = 25,
        choices = UserStatusChoices.choices,
        default = UserStatusChoices.PENDING,
    )

    objects = BusinessStaffManager()
    
    def __str__(self):
        return (
            f"Business: {self.business.name} - "
            f"Name: {self.user.first_name} {self.user.last_name} - "
            f"Role: {self.get_role_display()} - "
            f"Status: {self.get_status_display()}"
        )
        
        
class BusinessItem(models.Model):
    
    class Meta:
        db_table = 'business_item'
        verbose_name = 'Business Item'
        verbose_name_plural = 'Business Items'
       
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
    business = models.ForeignKey(
        Business,
        on_delete = models.CASCADE,
        related_name = 'items'
    )
    name = models.CharField(
        verbose_name = 'Name',
        max_length = 255,
    )
    description = models.TextField(
        verbose_name = 'Description',
        max_length = 255,
        blank = True,
    )
    status = models.CharField(
        verbose_name = 'Status',
        max_length = 25,
        choices = ItemStatusChoices.choices,
        default = ItemStatusChoices.DRAFT,
    )
    discontinued_date = models.DateTimeField(
        verbose_name = 'Discontinued Date',
        blank = True,
        null = True,
    )
    
    def __str__(self):
        return (
            f"Business: {self.business.name} - "
            f"Item: {self.name} - "
            f"Status: {self.get_status_display()}"
        )