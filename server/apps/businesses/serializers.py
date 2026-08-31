from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction

from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    ValidationError,
)

from apps.businesses.models import (
    Business,
    BusinessItem,
    BusinessLocation,
    BusinessStaff,
)
from core.choices import (
    BusinessRoleChoices,
    UserStatusChoices,
)

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
    
    timezone = CharField()
    
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

    business = BusinessSerializer()
    business_location = BusinessLocationSerializer()

    class Meta:
        model = BusinessStaff
        fields = [
            'business',
            'business_location',
        ]
        
    @transaction.atomic
    def create(self, validated_data):

        business_data = validated_data.pop('business')
        location_data = validated_data.pop('business_location')

        # Capture user information from request
        request = self.context.get('request')
        user = request.user

        business = BusinessSerializer().create(business_data)

        # Add business object into location_data under business key
        location_data['business'] = business
        location = BusinessLocationSerializer().create(location_data)

        try:
            admin = (
                BusinessStaff.objects.create_business_staff(
                    business_id = business.id,
                    user_id = user.id,
                    staff_email = user.email,
                    role = BusinessRoleChoices.ADMIN,
                    status = UserStatusChoices.ACTIVE,
                )
            )

        except DjangoValidationError as error:
            raise ValidationError(
                error.message_dict
            )

        return {
            'business': business,
            'business_location': location,
            'business_staff': admin,
        }


class BusinessStaffSerializer(ModelSerializer):

    business = BusinessSerializer(read_only = True)
    role_display = CharField(
        source = 'get_role_display',
        read_only = True
    )

    class Meta:
        model = BusinessStaff
        fields = [
            'id',
            'business',
            'role',
            'role_display',
            'status',
        ]


class BusinessItemSerializer(ModelSerializer):
    
    status_display = CharField(
            source = 'get_status_display',
            read_only = True
        )
    
    class Meta:
        model = BusinessItem
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'business': {'read_only': True},
            'created_date': {'read_only': True},
            'modified_date': {'read_only': True},
        }