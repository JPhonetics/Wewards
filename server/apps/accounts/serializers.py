from rest_framework.serializers import ModelSerializer
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
        password = validated_data.pop('password', None)

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