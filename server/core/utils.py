import phonenumbers
from django.core.exceptions import ValidationError


def normalize_phone_number(phone_number: str, country: str) -> str:
    try:
        parsed = phonenumbers.parse(phone_number, country)
    except phonenumbers.NumberParseException:
        raise ValidationError('Enter a valid phone number.')

    if not phonenumbers.is_valid_number(parsed):
        raise ValidationError('Enter a valid phone number.')

    return phonenumbers.format_number(
        parsed,
        phonenumbers.PhoneNumberFormat.E164,
    )