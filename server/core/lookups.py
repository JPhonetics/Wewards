import uuid
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
        

def get_account_user(
    user_id: uuid.UUID,
):
    
    # Grabs and assigns AUTH_USER_MODEL in settings.py
    auth_model = get_user_model()
    
    try:
        user = auth_model.objects.get(id = user_id)
        
    except auth_model.DoesNotExist:
        raise ValidationError(
            "User does not exist."
        )

    return user
    
    
def get_business(
    business_id: uuid.UUID,
):
    from apps.businesses.models import Business
    
    try:
        business = Business.objects.get(id = business_id)
        
    except Business.DoesNotExist:
        raise ValidationError(
            "Business does not exist."
        )

    return business
    
    
def get_business_location(
    business_location_id: uuid.UUID,
):
    from apps.businesses.models import BusinessLocation
    
    try:
        business_location = BusinessLocation.objects.get(id = business_location_id)
        
    except BusinessLocation.DoesNotExist:
        raise ValidationError(
            "Business Location does not exist."
        )

    return business_location
    
    
# Returns all businesses a user belongs to
def get_all_businesses_for_user(
    user_id: uuid.UUID,
):
    from apps.businesses.models import BusinessStaff
    
    user = get_account_user(user_id)

    business_staff = BusinessStaff.objects.filter(
        user = user
    )

    return business_staff
 
    
# Returns all staff belonging to that business
def get_all_business_staff_for_business(
    business_staff_id: uuid.UUID,
):
    from apps.businesses.models import BusinessStaff
    
    try:
        business_staff = BusinessStaff.objects.get(id = business_staff_id)
        
    except BusinessStaff.DoesNotExist:
        raise ValidationError(
            "Business Staff does not exist."
        )

    return business_staff


def get_business_staff_for_user(
    business_id: uuid.UUID,
    user_id: uuid.UUID,
):
    from apps.businesses.models import BusinessStaff
    
    try:
        business_staff = BusinessStaff.objects.get(
            business_id = business_id,
            user_id = user_id,
        )
        
    except BusinessStaff.DoesNotExist:
        raise ValidationError(
            "Business Staff does not exist."
        )

    return business_staff
    
    
def get_business_item(
    business_item_id: uuid.UUID,
):
    from apps.businesses.models import BusinessItem
    
    try:
        business_item = BusinessItem.objects.get(id = business_item_id)
        
    except BusinessItem.DoesNotExist:
        raise ValidationError(
            "Business Item does not exist."
        )

    return business_item
    
    
def get_reward_program_type(
    reward_program_type_id: uuid.UUID,
):
    from apps.rewards.models import RewardProgramType
    
    try:
        reward_program_type = RewardProgramType.objects.get(id = reward_program_type_id)
        
    except RewardProgramType.DoesNotExist:
        raise ValidationError(
            "Reward Program Type does not exist."
        )

    return reward_program_type

    
def get_reward_program(
    reward_program_id: uuid.UUID,
):
    from apps.rewards.models import RewardProgram
    
    try:
        reward_program = RewardProgram.objects.get(id = reward_program_id)
        
    except RewardProgram.DoesNotExist:
        raise ValidationError(
            "Reward Program does not exist."
        )

    return reward_program
    

def get_reward_program_location(
    reward_program_location_id: int,
):
    from apps.rewards.models import RewardProgramLocation
    
    try:
        reward_program_location = RewardProgramLocation.objects.get(id = reward_program_location_id)
        
    except RewardProgramLocation.DoesNotExist:
        raise ValidationError(
            "Reward Program Location does not exist."
        )

    return reward_program_location 

    
def get_reward(
    reward_id: uuid.UUID,
):
    from apps.rewards.models import Reward
    
    try:
        reward = Reward.objects.get(id = reward_id)
        
    except Reward.DoesNotExist:
        raise ValidationError(
            "Reward does not exist."
        )

    return reward
    
    
def get_rewards_by_program(
    reward_program_id: uuid.UUID,
):
    from apps.rewards.models import Reward

    reward_program = get_reward_program(reward_program_id)
    
    rewards = Reward.objects.filter(
        reward_program = reward_program
    )

    return rewards

    
def get_reward_location(
    reward_location_id: int,
):
    from apps.rewards.models import RewardLocation
    
    try:
        reward_location = RewardLocation.objects.get(id = reward_location_id)
        
    except RewardLocation.DoesNotExist:
        raise ValidationError(
            "Reward Location does not exist."
        )

    return reward_location
    
    
def get_business_locations_by_business(
    business_id: uuid.UUID,
):
    from apps.businesses.models import BusinessLocation

    business = get_business(business_id)

    locations = BusinessLocation.objects.filter(
        business = business
    )

    return locations

    
def get_business_items_by_business(
    business_id: uuid.UUID,
):
    from apps.businesses.models import BusinessItem

    business = get_business(business_id)

    items = BusinessItem.objects.filter(
        business = business
    )

    return items
    
    
def get_reward_programs_by_business(
    business_id: uuid.UUID,
):
    from apps.rewards.models import RewardProgram

    business = get_business(business_id)

    reward_programs = RewardProgram.objects.filter(
        business = business
    )

    return reward_programs
    
    
def get_rewards_by_business(
    business_id: uuid.UUID,
):
    from apps.rewards.models import Reward

    reward_programs = get_reward_programs_by_business(business_id)

    rewards = Reward.objects.filter(
        reward_program__in = reward_programs
    )

    return rewards


def get_reward_programs_by_user(
    user_id: uuid.UUID,
):
    from apps.rewards.models import RewardProgram

    user = get_account_user(user_id)

    reward_programs = RewardProgram.objects.filter(
        Q(earned_rewards__user = user) | 
        Q(adjusted_rewards__user = user) |
        Q(redeemed_rewards__user = user)
    ).distinct()

    return reward_programs
    

def get_reward_earning(
    reward_earning_id: uuid.UUID,
):
    from apps.rewards.models import RewardEarning
    
    try:
        reward_earning = RewardEarning.objects.get(id = reward_earning_id)
        
    except RewardEarning.DoesNotExist:
        raise ValidationError(
            "Reward Earning does not exist."
        )

    return reward_earning
    
    
def get_reward_adjustment(
    reward_adjustment_id: uuid.UUID,
):
    from apps.rewards.models import RewardAdjustment
    
    try:
        reward_adjustment = RewardAdjustment.objects.get(id = reward_adjustment_id)
        
    except RewardAdjustment.DoesNotExist:
        raise ValidationError(
            "Reward Adjustment does not exist."
        )

    return reward_adjustment
    
    
def get_reward_redemption(
    reward_redemption_id: uuid.UUID,
):
    from apps.rewards.models import RewardRedemption
    
    try:
        reward_redemption = RewardRedemption.objects.get(id = reward_redemption_id)
        
    except RewardRedemption.DoesNotExist:
        raise ValidationError(
            "Reward Redemption does not exist."
        )

    return reward_redemption