import uuid
from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.core.exceptions import ValidationError
from .validators import validate_platform_admin_email 
from core.choices import UserStatusChoices
from core.lookups import get_account_user
            
            
class PlatformAdminManager(BaseUserManager):
    
    def check_staff_flag(
        self,
        user,
    ):
        if not user.is_staff:
            raise ValidationError(
                "Platform Admin requires is_staff True."
            )
    
    def create_platform_admin(
        self,
        user_id: uuid.UUID,
        admin_email: str,
        role: str,
        **extra_fields
    ):
        user = get_account_user(user_id)
        
        self.check_staff_flag(user)
        
        admin_email = self.normalize_email(admin_email.strip().casefold())
        
        admin = self.model(
            user = user,
            email = admin_email,
            role = role,
            **extra_fields,
        )
        
        admin.full_clean()
        admin.save(using=self._db)
        
        return admin
            

class PlatformAdmin(models.Model):
    
    class Meta:
        db_table = 'platform_admin'
        verbose_name = 'Platform Admin'
        verbose_name_plural = 'Platform Admins'
        
    class PlatformAdminRoles(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        SUPPORT = 'support', 'Support'
    
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
    # References AUTH_USER_MODEL in settings.py
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete = models.PROTECT,
        related_name = 'platform_admin',
    )
    email = models.EmailField(
        verbose_name = 'Admin Email',
        unique = True,
        validators = [
            validate_platform_admin_email,
        ]
    )
    role = models.CharField(
        verbose_name = 'Role',
        max_length = 20,
        choices = PlatformAdminRoles.choices,
    )
    status = models.CharField(
        verbose_name = 'Status',
        max_length = 25,
        choices = UserStatusChoices.choices,
        default = UserStatusChoices.PENDING,
    )
    
    objects = PlatformAdminManager()
    
    def __str__(self):
        return (
            f"Name: {self.user.first_name} {self.user.last_name} - "
            f"Role: {self.get_role_display()} - "
            f"Status: {self.get_status_display()}"
        )
        
    # Final validation ensuring linked user is staff
    def clean(self):
        super().clean()

        if self.user_id and not self.user.is_staff:
            raise ValidationError(
                "Platform Admin requires is_staff True."
            )