from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction

from rest_framework.serializers import ModelSerializer, ValidationError

from apps.accounts.models import AccountUser
from apps.businesses.models import (
    Business,
    BusinessItem,
    BusinessLocation,
    BusinessStaff,
)


class BusinessAccountUserSerializer(ModelSerializer):
    
    class Meta:
        model = AccountUser
        fields = [
            'id',
            'country',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'password',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }
        
    def create(self, validated_data):
        password = validated_data.pop('password')

        try:
            user = AccountUser.objects.create_user(
                **validated_data
            )

        except DjangoValidationError as error:
            raise ValidationError(
                error.message_dict
            )

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save()

        return user
    

class BusinessSerializer(ModelSerializer):
    
    class Meta:
        model = Business
        fields = [
            'id',
            'name',
            'industry',
            'email',
            'phone_number',
            'website',
            'logo',
        ]
        
    def create(self, validated_data):
        try:
            business = Business.objects.create(
                **validated_data
            )

        except DjangoValidationError as error:
            raise ValidationError(
                error.message_dict
            )

        return business


class BusinessLocationSerializer(ModelSerializer):
    
    class Meta:
        model = BusinessLocation
        fields = [
            'id',
            'name',
            'address_line_1',
            'address_line_2',
            'city',
            'state_region',
            'postal_code',
            'country',
            'timezone',
        ]
        
    def create(self, validated_data):
        try:
            location = BusinessLocation.objects.create(
                **validated_data
            )

        except DjangoValidationError as error:
            raise ValidationError(
                error.message_dict
            )

        return location


class BusinessRegisterSerializer(ModelSerializer):

    account_user = BusinessAccountUserSerializer(
        required = False
    )

    business = BusinessSerializer()

    business_location = BusinessLocationSerializer()

    class Meta:
        model = BusinessStaff
        fields = [
            'account_user',
            'business',
            'business_location',
        ]
        
    @transaction.atomic
    def create(self, validated_data):

        account_user_data = validated_data.pop(
            'account_user',
            None
        )

        business_data = validated_data.pop(
            'business'
        )

        location_data = validated_data.pop(
            'business_location'
        )

        request = self.context.get(
            'request'
        )

        user = request.user

        if not user.is_authenticated:

            if not account_user_data:
                raise ValidationError({
                    'account_user':
                        'Account information is required.'
                })

            user = BusinessAccountUserSerializer().create(
                account_user_data
            )

        business = BusinessSerializer().create(
            business_data
        )

        location_data['business'] = business

        location = BusinessLocationSerializer().create(
            location_data
        )

        try:
            admin = (
                BusinessStaff.objects.create_business_staff(
                    business_id = business.id,
                    user_id = user.id,
                    staff_email = user.email,
                    role = 'admin',
                )
            )

        except DjangoValidationError as error:
            raise ValidationError(
                error.message_dict
            )

        return {
            'account_user': user,
            'business': business,
            'business_location': location,
            'business_staff': admin,
        }


class BusinessItemSerializer(ModelSerializer):
    
    class Meta:
        model = BusinessItem
        fields = '__all__'