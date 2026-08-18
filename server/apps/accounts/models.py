import uuid
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager, 
    PermissionsMixin
)
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import PhoneNumber
from core.validators import (
    validate_first_name, 
    validate_last_name, 
)      


class AccountUserManager(BaseUserManager):
    
    def create_user(
        self,
        first_name: str,
        last_name: str,
        country: str = 'US',
        email: str | None = None,
        phone_number: str | None = None,
        **extra_fields,
    ):
        first_name = first_name.strip()
        last_name = last_name.strip()
        
        if email: 
            email = self.normalize_email(email.strip().casefold())
        else:
            email = None
            
        if phone_number:
            phone_number = PhoneNumber.from_string(
                phone_number,
                region=country,
            )

            if not phone_number.is_valid():
                raise ValidationError('Enter a valid phone number.')
        else:
            phone_number = None
                    
        user = self.model(
            country = country,
            first_name = first_name,
            last_name = last_name,
            email = email,
            phone_number = phone_number,
            **extra_fields,
        )
        user.set_unusable_password()
        user.full_clean()
        
        user.first_name = user.first_name[:1].upper() + user.first_name[1:]
        user.last_name = user.last_name[:1].upper() + user.last_name[1:]
        
        user.save(using=self._db)
        
        return user
    
    def create_staff_user(
        self, 
        first_name: str,
        last_name: str,
        password: str,
        is_superuser: bool = False,
        **extra_fields
    ):
        first_name = first_name.strip()
        last_name = last_name.strip()
        
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = is_superuser
        
        staff = self.model(
            first_name = first_name,
            last_name = last_name,
            **extra_fields,
        )
        staff.set_password(password)
        staff.full_clean()
        
        staff.first_name = staff.first_name[:1].upper() + staff.first_name[1:]
        staff.last_name = staff.last_name[:1].upper() + staff.last_name[1:]
        
        staff.save(using=self._db)
        
        return staff
    
    def create_superuser(
        self, 
        first_name: str,
        last_name: str,
        password: str,
        **extra_fields
    ):
        return self.create_staff_user(
            first_name = first_name,
            last_name = last_name,
            password = password,
            is_superuser = True,
            **extra_fields
        )

class AccountUser(AbstractBaseUser, PermissionsMixin):
    
    class Meta:
        db_table = 'account_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
        constraints = [
            models.CheckConstraint(
                condition=(
                    Q(email__isnull=False) |
                    Q(phone_number__isnull=False) |
                    Q(is_staff=True)
                ),
                name='user_requires_contact_unless_staff',
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
    country = CountryField(
        verbose_name = 'Country',
        default = 'US',
    )
    first_name = models.CharField(
        verbose_name = 'First Name',
        max_length = 100,
        validators = [
            validate_first_name,
        ]
    )
    last_name = models.CharField(
        verbose_name = 'Last Name',
        max_length = 100,
        validators = [
            validate_last_name,
        ]
    )
    email = models.EmailField(
        verbose_name = 'Email',
        unique = True,
        blank = True,
        null = True,
    )
    phone_number = PhoneNumberField(
        verbose_name = 'Phone Number',
        max_length = 16,
        unique = True,
        blank = True,
        null = True,
    )
    is_active = models.BooleanField(
        verbose_name = 'Enabled',
        default = True,
    )
    is_staff = models.BooleanField(
        verbose_name = 'Staff',
        default = False,
    )
    is_superuser = models.BooleanField(
        verbose_name = 'Superuser',
        default = False,
    )
    last_login = models.DateTimeField(
        verbose_name = 'Last Login',
        blank = True,
        null = True,
    )
    password = models.CharField(
        verbose_name = 'Password',
        max_length = 128,
    )
    
    USERNAME_FIELD = 'id'

    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
    ]

    objects = AccountUserManager()
    
    def __str__(self):
        return (
            f"Name: {self.first_name} {self.last_name} - "
            f"Email: {self.email} - "
            f"Phone Number: {self.phone_number} - "
            f"Active: {self.is_active}"
        )