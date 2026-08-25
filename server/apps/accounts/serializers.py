from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    ValidationError,
)
from apps.accounts.models import AccountUser


class AccountUserSerializer(ModelSerializer):
    
    class Meta:
        model = AccountUser
        fields = [
            'id',
            'created_date',
            'country',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'password',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
            'password': {'write_only': True},
        }
        
    def create(self, validated_data):
        
        # Pull the password out of the validator
        password = validated_data.pop('password')

        user = AccountUser.objects.create_user(
            **validated_data
        )

        # Temporarily allowing password before setting up passwordless
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()        
            
        user.save()

        return user
    

class AccountUserProfileSerializer(ModelSerializer):

    class Meta:
        model = AccountUser
        fields = [
            'id',
            'created_date',
            'country',
            'first_name',
            'last_name',
            'email',
            'phone_number',
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'created_date': {'read_only': True},
        }


class AccountUserPasswordSerializer(Serializer):

    current_password = CharField(write_only = True)
    new_password = CharField(write_only = True)

    def validate_current_password(self, value):
        user = self.context['request'].user

        if not user.check_password(value):
            raise ValidationError(
                'Current password is incorrect.'
            )

        return value

    def save(self):

        user = self.context['request'].user

        new_password = self.validated_data[
            'new_password'
        ]

        user.set_password(new_password)

        user.save(
            update_fields = [
                'password'
            ]
        )

        return user