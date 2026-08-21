import uuid
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
    
    
def get_business_staff(
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