import uuid
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

def get_account_user(
        user_id: uuid.UUID,
    ):
        
        # Grabs and assigns AUTH_USER_MODEL in settings.py
        auth_model = get_user_model()
        
        try:
            confirmed_user = auth_model.objects.get(id = user_id)
            
        except auth_model.DoesNotExist:
            raise ValidationError(
                "Unable to locate account user profile."
            )

        return confirmed_user
    
    
def get_business(
        business_id: uuid.UUID,
    ):
        from apps.businesses.models import Business
        
        try:
            confirmed_business = Business.objects.get(id = business_id)
            
        except Business.DoesNotExist:
            raise ValidationError(
                "Unable to locate business."
            )

        return confirmed_business