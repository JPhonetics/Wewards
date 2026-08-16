import uuid
from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.core.exceptions import ValidationError
from .validators import validate_staff_email  
            
            
class StaffProfileManager(BaseUserManager):
    
    def create_staff_profile(
        self,
        user_id: uuid.UUID,
        staff_email: str,
        role: str,
        **extra_fields
    ):
        staff_email = self.normalize_email(staff_email.strip().casefold())
        
        profile = self.model(
            user_id = user_id,
            email = staff_email,
            role = role,
            **extra_fields,
        )
        
        profile.full_clean()
        profile.save(using=self._db)
        
        return profile

class StaffProfile(models.Model):
    
    class Meta:
        db_table = 'backoffice_staff_profile'
        verbose_name = 'Staff Profile'
        verbose_name_plural = 'Staff Profiles'
        
    class StaffRoles(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        SUPPORT = 'support', 'Support'
    
    id = models.UUIDField(
        verbose_name = 'ID',
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
    )
    # References the configured AUTH_USER_MODEL set in settings.py
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'staff_profile',
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created Date',
        auto_now_add = True,
    )
    modified_date = models.DateTimeField(
        verbose_name = 'Modified Date',
        auto_now = True,
    )
    email = models.EmailField(
        verbose_name = 'Staff Email',
        unique = True,
        validators = [
            validate_staff_email,
        ]
    )
    role = models.CharField(
        verbose_name = 'Role',
        max_length = 20,
        choices = StaffRoles.choices,
    )
    is_active = models.BooleanField(
        verbose_name = 'Active',
        default = True,
    )
    
    objects = StaffProfileManager()
    
    def __str__(self):
        return (
            f"Name: {self.user.first_name} {self.user.last_name} - "
            f"Role: {self.get_role_display()} - "
            f"Active: {self.is_active}"
        )
        
    def clean(self):
        super().clean()

        if self.user_id and not self.user.is_staff:
            raise ValidationError(
                "Staff profile requires is_staff True."
            )