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
from phonenumber_field.phonenumber import PhoneNumber
from core.normalizers import (
    normalize_email,
    normalize_name,
)
from core.validators import (
    validate_first_name, 
    validate_last_name,
    validate_phone_number,
)


class AccountUserManager(BaseUserManager):
    
    def create_user(
        self,
        email: str,
        first_name: str,
        last_name: str,
        country: str,
        phone_number: str,
        **extra_fields,
    ):       
        user = self.model(
            email = email,
            first_name = first_name,
            last_name = last_name,
            country = country,
            phone_number = phone_number,
            **extra_fields,
        )
        user.set_unusable_password()
        user.full_clean() 
        user.save(using=self._db)
        
        return user
    
    def create_staff_user(
        self, 
        email: str,
        first_name: str,
        last_name: str,
        country: str,
        phone_number: str,
        password: str,
        is_superuser: bool = False,
        **extra_fields
    ):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = is_superuser
        
        staff = self.model(
            email = email,
            first_name = first_name,
            last_name = last_name,
            country = country,
            phone_number = phone_number,
            **extra_fields,
        )
        staff.set_password(password)
        staff.full_clean()        
        staff.save(using=self._db)
        
        return staff
    
    def create_superuser(
        self, 
        email: str,
        first_name: str,
        last_name: str,
        country: str,
        phone_number: str,
        password: str,
        **extra_fields
    ):
        return self.create_staff_user(
            email = email,
            first_name = first_name,
            last_name = last_name,
            password = password,
            country = country,
            phone_number = phone_number,
            is_superuser = True,
            **extra_fields
        )

class AccountUser(AbstractBaseUser, PermissionsMixin):
    
    class Meta:
        db_table = 'account_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
        # constraints = [
        #     models.CheckConstraint(
        #         condition = (
        #             Q(email__isnull = False) |
        #             Q(phone_number__isnull = False) |
        #             Q(is_staff = True)
        #         ),
        #         name = 'user_requires_contact_unless_staff',
        #     ),
        # ]
    
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
    )
    phone_number = models.CharField(
        verbose_name = 'Phone Number',
        max_length = 16,
        unique = True,
        validators = [
            validate_phone_number,
        ]
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
    
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'country',
        'phone_number',
    ]

    objects = AccountUserManager()
    
    def __str__(self):
        return (
            f"Name: {self.first_name} {self.last_name} - "
            f"Email: {self.email} - "
            f"Phone Number: {self.phone_number} - "
            f"Active: {self.is_active}"
        )
    
    
    def clean(self):
        super().clean()

        if self.email:
            self.email = normalize_email(self.email)

        if self.first_name:
            self.first_name = normalize_name(self.first_name)
                    
        if self.last_name:
            self.last_name = normalize_name(self.last_name)

        # Moved phone_number verification to clean because different 
        # function between API and Admin portal
        # if self.phone_number:
        #     phone_number = PhoneNumber.from_string(
        #         self.phone_number,
        #         region = str(self.country),
        #     )

        #     if not phone_number.is_valid():
        #         raise ValidationError(
        #             'Enter a valid phone number.'
        #         )
                
        #     self.phone_number = str(phone_number)