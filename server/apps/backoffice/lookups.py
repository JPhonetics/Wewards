import uuid
from django.core.exceptions import ValidationError

def get_platform_admin(
        platform_admin_id: uuid.UUID,
    ):
        
        from apps.backoffice.models import PlatformAdmin
        
        try:
            confirmed_admin = PlatformAdmin.objects.get(id = platform_admin_id)
            
        except PlatformAdmin.DoesNotExist:
            raise ValidationError(
                "Platform admin does not exist."
            )

        return confirmed_admin