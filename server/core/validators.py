from django.core.exceptions import ValidationError
import re


def validate_name(value: str, message: str = "Please enter a valid name."):
    forbidden_characters = re.search(r'[~@#$%^&*{}|:<>]', value)
    
    if value.strip() == "" or forbidden_characters:
        raise ValidationError(
            message = message
        )


def validate_first_name(value: str):
    validate_name(
        value, 
        "Please enter a valid first name"
    )
    
    
def validate_last_name(value: str):
    validate_name(
        value, 
        "Please enter a valid last name"
    )
    
    
def validate_staff_match_business(
    business,
    staff,
): 
    if business.id != staff.business_id:
        raise ValidationError(
            "Staff must belong to the selected Business."
        )
    
    
def validate_location_match_business(
    business,
    location,
):
    if business.id != location.business_id:
        raise ValidationError(
            "Location must belong to the selected Business."
        )
    
    
def validate_reward_match_program(
    reward_program,
    reward,
):
    if reward_program.id != reward.reward_program_id:
        raise ValidationError(
            "Reward must belong to the selected Reward Program."
        )


# def validate_phone_number(value: str):
#     good_input = re.fullmatch(r'^\s*[0-9]+\s*$', value)
    
#     if not good_input:
#         raise ValidationError(
#             message = "Please enter numbers only."
#         )
        