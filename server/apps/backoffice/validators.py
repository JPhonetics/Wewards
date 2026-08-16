import re
from django.core.exceptions import ValidationError

        
def validate_staff_email(value: str,):
    domain = 'wewards.app'
    my_email = 'jphonetics02@gmail.com'
    
    if not value.lower().endswith(f"@{domain}") and value.lower() != my_email:
        raise ValidationError(
            message = "Email is not authorized for staff access."
        )
    
