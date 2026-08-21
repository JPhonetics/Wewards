from decimal import Decimal
from django.db.models import Sum
from apps.accounts.models import *
from apps.rewards.models import *
from core.lookups import *


def calculate_balance(
    user_id: uuid.UUID, 
    reward_program_id: uuid.UUID,
):
    user = get_account_user(user_id)
    reward_program = get_reward_program(reward_program_id)
    
    user_earnings = RewardEarning.objects.filter(
        user = user,
        reward_program = reward_program
    )
    earnings = user_earnings.aggregate(
        total = Sum("amount_earned")
    )
    earnings = (
        earnings["total"]
        if earnings["total"]
        else Decimal("0")
    )
    
    user_adjustments = RewardAdjustment.objects.filter(
        user = user,
        reward_program = reward_program
    )
    adjustments = user_adjustments.aggregate(
        total = Sum("adjustment_amount")
    )
    adjustments = (
        adjustments["total"]
        if adjustments["total"]
        else Decimal("0")
    )
    
    user_redemptions = RewardRedemption.objects.filter(
        user = user,
        reward_program = reward_program
    )
    redemptions = user_redemptions.aggregate(
        total = Sum("amount_redeemed")
    )
    redemptions = (
        redemptions["total"]
        if redemptions["total"]
        else Decimal("0")
    )
    
    return earnings + adjustments - redemptions


def eligible_rewards(
    user_id: uuid.UUID, 
    reward_program_id: uuid.UUID,
):
    balance = calculate_balance(user_id, reward_program_id)
    rewards = Reward.objects.filter(reward_program = reward_program_id)
    
    eligible_rewards = rewards.filter(amount_required__lte = balance)
    
    return eligible_rewards


def award_points(
    user_id: uuid.UUID, 
    reward_program_id: uuid.UUID,
    amount_earned: Decimal,
    location_id: uuid.UUID = None,
    business_staff_id: uuid.UUID = None,
    receipt_number: str = None,
    receipt_total: Decimal = None,
    reward_id: uuid.UUID = None,
):
    user = get_account_user(user_id)
    reward_program = get_reward_program(reward_program_id)
    
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
    reward = (
        get_reward(reward_id)
        if reward_id
        else None
    )
    
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
        

def redeem_points(
    user_id: uuid.UUID, 
    reward_program_id: uuid.UUID,
    location_id: uuid.UUID,
    business_staff_id: uuid.UUID,
    reward_id: uuid.UUID,
):
    user = get_account_user(user_id)
    reward_program = get_reward_program(reward_program_id)
    location = get_business_location(location_id) 
    staff = get_business_staff(business_staff_id)
    reward = get_reward(reward_id)
    
    balance = calculate_balance(user_id, reward_program_id)
    
    if balance < reward.amount_required:
        raise ValidationError (
            "Insufficient Points."
        )
        
    redeemed = RewardRedemption.objects.create(
        user = user,
        reward_program = reward_program,
        location = location,
        processed_by_staff = staff,
        reward = reward,
        amount_redeemed = reward.amount_required,
    )
    
    return redeemed