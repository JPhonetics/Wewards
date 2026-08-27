from decimal import Decimal
from django.db.models import Sum
from apps.accounts.models import *
from apps.rewards.models import *
from core.lookups import *
from core.validators import *


PUNCH_CARD = "Punch Card"

def _validate_punch_card_program_type(reward_program):
    if reward_program.program_type.name != PUNCH_CARD:
        
        raise ValidationError(
            "Reward Program Type is not Punch Card."
        )


def punch_card_calculate_progress_all(
    user_id: uuid.UUID, 
    reward_program_id: uuid.UUID,
):
    reward_program = get_reward_program(reward_program_id)
    _validate_punch_card_program_type(reward_program)
    
    user = get_account_user(user_id)
    
    earnings = RewardEarning.objects.filter(
        user = user,
        reward_program = reward_program,
    ).values(
        "reward",
    ).annotate(
        total = Sum("amount_earned")
    )

    adjustments = RewardAdjustment.objects.filter(
        user = user,
        reward_program = reward_program,
    ).values(
        "reward",
    ).annotate(
        total = Sum("adjustment_amount")
    )
    
    redemptions = RewardRedemption.objects.filter(
        user = user,
        reward_program = reward_program,
    ).values(
        "reward",
    ).annotate(
        total = Sum("amount_redeemed")
    )
    
    # Converts list of dictionaries to a dictionary
    earnings_by_reward = {
        row["reward"]: row["total"]
        for row in earnings
    }

    adjustments_by_reward = {
        row["reward"]: row["total"]
        for row in adjustments
    }

    redemptions_by_reward = {
        row["reward"]: row["total"]
        for row in redemptions
    }

    rewards = punch_card_all_rewards(reward_program_id)

    progress = []

    for reward in rewards:
        # Store the value for the matching key. 0 if doesn't exist
        earned = earnings_by_reward.get(
            reward.id,
            Decimal("0"),
        )

        adjusted = adjustments_by_reward.get(
            reward.id,
            Decimal("0"),
        )

        redeemed = redemptions_by_reward.get(
            reward.id,
            Decimal("0"),
        )
        
        current_progress = (earned + adjusted - redeemed)

        progress.append({
            "reward":
                reward,
            "progress":
                current_progress,
            "eligible":
                current_progress >= reward.amount_required,
        })

    return progress


def punch_card_calculate_progress(
    user_id: uuid.UUID, 
    reward_program_id: uuid.UUID,
    reward_id: uuid.UUID,
):
    reward_program = get_reward_program(reward_program_id)
    _validate_punch_card_program_type(reward_program)
    
    reward = get_reward(reward_id)
    validate_reward_match_program(reward_program, reward)
    
    user = get_account_user(user_id)
    
    earnings = RewardEarning.objects.filter(
        user = user,
        reward_program = reward_program,
        reward = reward,
    ).aggregate(
        total = Sum("amount_earned")
    )
    earnings = (
        earnings["total"]
        if earnings["total"]
        else Decimal("0")
    )
    
    adjustments = RewardAdjustment.objects.filter(
        user = user,
        reward_program = reward_program,
        reward = reward,
    ).aggregate(
        total = Sum("adjustment_amount")
    )
    adjustments = (
        adjustments["total"]
        if adjustments["total"]
        else Decimal("0")
    )
    
    redemptions = RewardRedemption.objects.filter(
        user = user,
        reward_program = reward_program,
        reward = reward,
    ).aggregate(
        total = Sum("amount_redeemed")
    )
    redemptions = (
        redemptions["total"]
        if redemptions["total"]
        else Decimal("0")
    )
    
    return earnings + adjustments - redemptions


def punch_card_all_rewards(
    reward_program_id: uuid.UUID,
):
    reward_program = get_reward_program(reward_program_id)
    _validate_punch_card_program_type(reward_program)

    rewards = get_rewards_by_program(reward_program_id)

    return rewards


def punch_card_eligible_rewards(
    user_id: uuid.UUID, 
    reward_program_id: uuid.UUID,
):
    progress = punch_card_calculate_progress_all(
        user_id,
        reward_program_id
    )
    
    eligible_rewards = []
    
    for reward in progress:
        if reward["eligible"]:
            eligible_rewards.append(reward)

    return eligible_rewards


def punch_card_award(
    user_id: uuid.UUID, 
    reward_program_id: uuid.UUID,
    reward_id: uuid.UUID,
    amount_earned: Decimal,
    location_id: uuid.UUID = None,
    business_staff_id: uuid.UUID = None,
    receipt_number: str = None,
    receipt_total: Decimal = None,
):
    reward_program = get_reward_program(reward_program_id)
    _validate_punch_card_program_type(reward_program)
    
    reward = get_reward(reward_id)
    validate_reward_match_program(reward_program, reward)
    
    user = get_account_user(user_id)
    
    location = (
        get_business_location(location_id) 
        if location_id
        else None
    )
    staff = (
        get_business_staff(business_staff_id)
        if business_staff_id
        else None
    )
    
    if location or staff:
        business = get_business(reward_program.business_id)
            
        if location:
            validate_location_match_business(business, location)
        
        if staff:
            validate_staff_match_business(business, staff)
    
    new_award = RewardEarning.objects.create(
        user = user,
        reward_program = reward_program,
        location = location,
        granted_by_staff = staff,
        receipt_number = receipt_number,
        receipt_total = receipt_total,
        reward = reward,
        amount_earned = amount_earned,
    )
    
    return new_award
        

def punch_card_redeem(
    user_id: uuid.UUID, 
    reward_program_id: uuid.UUID,
    location_id: uuid.UUID,
    business_staff_id: uuid.UUID,
    reward_id: uuid.UUID,
):
    reward_program = get_reward_program(reward_program_id)
    _validate_punch_card_program_type(reward_program)
    
    reward = get_reward(reward_id)
    validate_reward_match_program(reward_program, reward) 
    
    balance = punch_card_calculate_progress(
        user_id,
        reward_program_id,
        reward_id
    )
    
    if balance < reward.amount_required:
        raise ValidationError (
            "Amount required not met."
        ) 

    business = get_business(reward_program.business_id)
    staff = get_business_staff(business_staff_id)
    validate_staff_match_business(business, staff)
    
    location = get_business_location(location_id) 
    validate_location_match_business(business, location)
        
    # need a validator to check the location can accept the reward
        
    user = get_account_user(user_id)
        
    redeemed = RewardRedemption.objects.create(
        user = user,
        reward_program = reward_program,
        location = location,
        processed_by_staff = staff,
        reward = reward,
        amount_redeemed = reward.amount_required,
    )
    
    return redeemed