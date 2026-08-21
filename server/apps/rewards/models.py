import uuid
from django.db import models
from django.core.exceptions import ValidationError
from apps.accounts.models import AccountUser
from apps.backoffice.models import PlatformAdmin
from apps.businesses.models import (
    Business,
    BusinessItem,
    BusinessLocation,
    BusinessStaff,
)
from core.choices import (
    RewardAdjustmentChoices,
    RewardProgramStatusChoices,
    RewardTypeChoices,
)


class RewardProgramType(models.Model):
    
    class Meta:
        db_table = 'reward_program_type'
        verbose_name = 'Reward Program Type'
        verbose_name_plural = 'Reward Program Types'
        
    id = models.BigAutoField(
        verbose_name='ID',
        primary_key=True,
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created Date',
        auto_now_add = True,
    )
    modified_date = models.DateTimeField(
        verbose_name = 'Modified Date',
        auto_now = True,
    )
    name = models.CharField(
        verbose_name = 'Name',
        max_length = 25,
        unique = True,
    )
    description = models.TextField(
        verbose_name = 'Description',
        max_length = 255,
        blank = True,
    )
    
    def __str__(self):
        return (
            f"Reward Program Type: {self.name} - "
            f"Description: {self.description}"
        )
    
        
class RewardProgram(models.Model):
    
    class Meta:
        db_table = 'reward_program'
        verbose_name = 'Reward Program'
        verbose_name_plural = 'Reward Programs'
        
    id = models.UUIDField(
        verbose_name = 'ID',
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created Date',
        auto_now_add = True,
    )
    modified_date = models.DateTimeField(
        verbose_name = 'Modified Date',
        auto_now = True,
    )
    business = models.ForeignKey(
        Business,
        on_delete = models.PROTECT,
        related_name = 'reward_programs',
    )
    program_type = models.ForeignKey(
        RewardProgramType,
        on_delete = models.PROTECT,
        related_name = 'reward_programs',
    )
    start_date = models.DateTimeField(
        verbose_name = 'Start Date',
        blank = True,
        null = True,
    )
    name = models.CharField(
        verbose_name = 'Name',
        max_length = 255,
    )
    description = models.TextField(
        verbose_name = 'Description',
        max_length = 255,
        blank = True,
    )
    status = models.CharField(
        verbose_name = 'Status',
        max_length = 25,
        choices = RewardProgramStatusChoices.choices,
        default = RewardProgramStatusChoices.DRAFT,
    )
    end_date = models.DateTimeField(
        verbose_name = 'End Date',
        blank = True,
        null = True,
    )
    
    def __str__(self):
        return (
            f"Program Name: {self.name} - "
            f"Program Type: {self.program_type.name} - "
            f"Status: {self.get_status_display()} - "
            f"Start Date: {self.start_date} - "
            f"End Date: {self.end_date}"
        )
        

class RewardProgramLocation(models.Model):
    
    class Meta:
        db_table = 'reward_program_location'
        verbose_name = 'Participating Reward Program Location'
        verbose_name_plural = 'Participating Reward Program Locations'
        
        constraints = [
            models.UniqueConstraint(
                fields = ['reward_program', 'location'],
                name = 'unique_reward_program_location',
            ),
        ]
        
    id = models.BigAutoField(
        verbose_name='ID',
        primary_key=True,
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created Date',
        auto_now_add = True,
    )
    modified_date = models.DateTimeField(
        verbose_name = 'Modified Date',
        auto_now = True,
    )
    reward_program = models.ForeignKey(
        RewardProgram,
        on_delete = models.PROTECT,
        related_name = 'program_locations',
    )
    location = models.ForeignKey(
        BusinessLocation,
        on_delete = models.PROTECT,
        related_name = 'reward_program_locations',
    )
    
    def __str__(self):
        return (
            f"Business: {self.reward_program.business.name} - "
            f"Location: {self.location.name} - "
            f"Program Type: {self.reward_program.program_type.name} - "
            f"Program Name: {self.reward_program.name}"
        )
    
    # Final validation ensuring Program and Location belong to the same business
    def clean(self):
        super().clean()

        if self.reward_program.business_id != self.location.business_id:
            raise ValidationError(
                "Reward Program and Business Location must belong to the same business."
            )
    

class Reward(models.Model):
    
    class Meta:
        db_table = 'reward'
        verbose_name = 'Reward'
        verbose_name_plural = 'Rewards'
        
    id = models.UUIDField(
        verbose_name = 'ID',
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created Date',
        auto_now_add = True,
    )
    modified_date = models.DateTimeField(
        verbose_name = 'Modified Date',
        auto_now = True,
    )
    reward_program = models.ForeignKey(
        RewardProgram,
        on_delete = models.PROTECT,
        related_name = 'rewards',
    )
    name = models.CharField(
        verbose_name = 'Name',
        max_length = 255,
    )
    reward_type = models.CharField(
        verbose_name = 'Reward Type',
        max_length = 25,
        choices = RewardTypeChoices.choices,
    )
    description = models.TextField(
        verbose_name = 'Description',
        max_length = 255,
        blank = True,
    )
    qualifying_item = models.ForeignKey(
        BusinessItem,
        on_delete = models.PROTECT,
        related_name = 'qualifying_rewards',
        blank = True,
        null = True,
    )
    amount_required = models.PositiveIntegerField(
        verbose_name = 'Amount Required',
    )
    earned_item = models.ForeignKey(
        BusinessItem,
        on_delete = models.PROTECT,
        related_name = 'earned_rewards',
        blank = True,
        null = True,
    )
    discount_amount = models.DecimalField(
        verbose_name = 'Discount Amount',
        max_digits = 5,
        decimal_places = 2,
        blank = True,
        null = True,
    )
    discount_percentage = models.DecimalField(
        verbose_name = 'Discount Percentage',
        max_digits = 5,
        decimal_places = 2,
        blank = True,
        null = True,
    )
    # Revisit!!! Does Reward need its own choices?
    status = models.CharField(
        verbose_name = 'Status',
        max_length = 25,
        choices = RewardProgramStatusChoices.choices,
        default = RewardProgramStatusChoices.DRAFT,
    )
    end_date = models.DateTimeField(
        verbose_name = 'End Date',
        blank = True,
        null = True,
    )
        
    def __str__(self):
        return (
            f"Name: {self.name} - "
            f"Type: {self.get_reward_type_display()} - "
            f"Qualifying Item: {self.qualifying_item.name} - "
            f"Amount Required: {self.amount_required} - "
            f"Reward Item: {self.earned_item.name}"
        )
    
    def clean(self):
        super().clean()
        
        business_id = self.reward_program.business_id

        if (
            self.qualifying_item
            and business_id != self.qualifying_item.business_id
        ):
            raise ValidationError(
                "Reward Program and Qualifying Item must belong to the same business."
            )   

        if (
            self.earned_item
            and business_id != self.earned_item.business_id
        ):
            raise ValidationError(
                "Reward Program and Earned Item must belong to the same business."
            )   
        

class RewardLocation(models.Model):
    
    class Meta:
        db_table = 'reward_location'
        verbose_name = 'Participating Reward Location'
        verbose_name_plural = 'Participating Reward Locations'
        
        constraints = [
            models.UniqueConstraint(
                fields = ['reward', 'location'],
                name = 'unique_reward_location',
            ),
        ]
        
    id = models.BigAutoField(
        verbose_name='ID',
        primary_key=True,
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created Date',
        auto_now_add = True,
    )
    modified_date = models.DateTimeField(
        verbose_name = 'Modified Date',
        auto_now = True,
    )
    reward = models.ForeignKey(
        Reward,
        on_delete = models.CASCADE,
        related_name = 'reward_locations',
    )
    location = models.ForeignKey(
        BusinessLocation,
        on_delete = models.CASCADE,
        related_name = 'reward_locations',
    )
    
    def __str__(self):
        return (
            f"Reward: {self.reward.name} - "
            f"Location: {self.location.name}"
        )
        
    def clean(self):
        super().clean()

        if self.reward.reward_program.business_id != self.location.business_id:
            raise ValidationError(
                "Reward and Business Location must belong to the same business."
            )
        

class RewardEarning(models.Model):
    
    class Meta:
        db_table = 'reward_earning'
        verbose_name = 'Reward Earning'
        verbose_name_plural = 'Reward Earnings'
    
    id = models.UUIDField(
        verbose_name = 'ID',
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created Date',
        auto_now_add = True,
    )
    modified_date = models.DateTimeField(
        verbose_name = 'Modified Date',
        auto_now = True,
    )
    user = models.ForeignKey(
        AccountUser,
        on_delete = models.PROTECT,
        related_name = 'earned_rewards',
    )
    reward_program = models.ForeignKey(
        RewardProgram,
        on_delete = models.PROTECT,
        related_name = 'earned_rewards',
    )
    location = models.ForeignKey(
        BusinessLocation,
        on_delete = models.SET_NULL,
        related_name = 'earned_rewards',
        null = True,
    )
    granted_by_staff = models.ForeignKey(
        BusinessStaff,
        on_delete = models.PROTECT,
        related_name = 'earned_rewards',
        blank = True,
        null = True,
    )
    receipt_number = models.CharField(
        verbose_name = 'Receipt Number',
        max_length = 255,
        blank = True,
        null = True,
    )
    receipt_total = models.DecimalField(
        verbose_name = 'Receipt Total',
        max_digits = 8,
        decimal_places = 2,
        blank = True,
        null = True,
    )
    reward = models.ForeignKey(
        Reward,
        on_delete = models.PROTECT,
        related_name = 'earned_rewards',
        blank = True,
        null = True,
    )
    amount_earned = models.DecimalField(
        verbose_name = 'Amount Earned',
        max_digits = 8,
        decimal_places = 2,
    )
    
    def __str__(self):
        return (
            f"Name: {self.user.first_name} {self.user.last_name} - "
            f"Date: {self.created_date} - "
            f"Reward Program: {self.reward_program.name} - "
            f"Earned: {self.amount_earned}"
        )
        
    def clean(self):
        super().clean()
        
        business_id = self.reward_program.business_id

        if (
            self.location
            and business_id != self.location.business_id
        ):
            raise ValidationError(
                "Reward Program and Business Location must belong to the same business."
            )   
            
        if (
            self.granted_by_staff
            and business_id != self.granted_by_staff.business_id
        ):
            raise ValidationError(
                "Reward Program and Staff Member must belong to the same business."
            )   

        if (
            self.reward
            and self.reward_program_id != self.reward.reward_program_id
        ):
            raise ValidationError(
                "Reward Program and Reward Item must belong to the same business."
            )   

class RewardAdjustment(models.Model):
    
    class Meta:
        db_table = 'reward_adjustment'
        verbose_name = 'Reward Adjustment'
        verbose_name_plural = 'Reward Adjustments'
        
    id = models.UUIDField(
        verbose_name = 'ID',
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created Date',
        auto_now_add = True,
    )
    modified_date = models.DateTimeField(
        verbose_name = 'Modified Date',
        auto_now = True,
    )
    user = models.ForeignKey(
        AccountUser,
        on_delete = models.PROTECT,
        related_name = 'adjusted_rewards',
    )
    reward_program = models.ForeignKey(
        RewardProgram,
        on_delete = models.PROTECT,
        related_name = 'adjusted_rewards',
    )
    location = models.ForeignKey(
        BusinessLocation,
        on_delete = models.SET_NULL,
        related_name = 'adjusted_rewards',
        null = True,
    )
    adjusted_by_staff = models.ForeignKey(
        BusinessStaff,
        on_delete = models.PROTECT,
        related_name = 'adjusted_rewards',
        blank = True,
        null = True,
    )
    adjusted_by_admin = models.ForeignKey(
        PlatformAdmin,
        on_delete = models.PROTECT,
        related_name = 'adjusted_rewards',
        blank = True,
        null = True,
    )
    adjustment_type = models.CharField(
        verbose_name = 'Adjustment Type',
        max_length = 50,
        choices = RewardAdjustmentChoices.choices,
    )
    reason = models.TextField(
        verbose_name = 'Reason',
        max_length = 255,
        blank = True,
    )
    reward = models.ForeignKey(
        Reward,
        on_delete = models.PROTECT,
        related_name = 'adjusted_rewards',
        blank = True,
        null = True,
    )
    adjustment_amount = models.DecimalField(
        verbose_name = 'Amount Adjusted',
        max_digits = 8,
        decimal_places = 2,
    )
    
    def __str__(self):
        return (
            f"Name: {self.user.first_name} {self.user.last_name} - "
            f"Reason: {self.reason} - "
            f"Adjusted: {self.adjustment_amount}"
        )
        
    def clean(self):
        super().clean()
        
        business_id = self.reward_program.business_id

        if (
            self.location
            and business_id != self.location.business_id
        ):
            raise ValidationError(
                "Reward Program and Business Location must belong to the same business."
            )   
            
        if (
            self.adjusted_by_staff
            and business_id != self.adjusted_by_staff.business_id
        ):
            raise ValidationError(
                "Reward Program and Staff Member must belong to the same business."
            )   

        if (
            self.reward
            and self.reward_program_id != self.reward.reward_program_id
        ):
            raise ValidationError(
                "Reward Program and Reward Item must belong to the same business."
            )

        if not self.adjusted_by_staff and not self.adjusted_by_admin:
            raise ValidationError(
                "Reward Adjustment must be adjusted by either staff or a platform admin."
        )
            
        if self.adjusted_by_staff and self.adjusted_by_admin:
            raise ValidationError(
                "Reward Adjustment cannot be adjusted by both staff and a platform admin."
            )


class RewardRedemption(models.Model):
    
    class Meta:
        db_table = 'reward_redemption'
        verbose_name = 'Reward Redemption'
        verbose_name_plural = 'Reward Redemptions'
        
    id = models.UUIDField(
        verbose_name = 'ID',
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
    )
    created_date = models.DateTimeField(
        verbose_name = 'Created Date',
        auto_now_add = True,
    )
    modified_date = models.DateTimeField(
        verbose_name = 'Modified Date',
        auto_now = True,
    )
    user = models.ForeignKey(
        AccountUser,
        on_delete = models.PROTECT,
        related_name = 'redeemed_rewards',
    )
    reward_program = models.ForeignKey(
        RewardProgram,
        on_delete = models.PROTECT,
        related_name = 'redeemed_rewards',
    )
    location = models.ForeignKey(
        BusinessLocation,
        on_delete = models.SET_NULL,
        related_name = 'redeemed_rewards',
        null = True,
    )
    processed_by_staff = models.ForeignKey(
        BusinessStaff,
        on_delete = models.PROTECT,
        related_name = 'redeemed_rewards',
    )
    reward = models.ForeignKey(
        Reward,
        on_delete = models.PROTECT,
        related_name = 'redeemed_rewards',
    )
    amount_redeemed = models.DecimalField(
        verbose_name = 'Amount Redeemed',
        max_digits = 8,
        decimal_places = 2,
    )
    
    def __str__(self):
        return (
            f"Name: {self.user.first_name} {self.user.last_name} - "
            f"Date: {self.created_date} - "
            f"Reward Program: {self.reward_program.name} - "
            f"Redeemed For: {self.reward.name}"
        )

    def clean(self):
        super().clean()
        
        business_id = self.reward_program.business_id

        if (
            self.location
            and business_id != self.location.business_id
        ):
            raise ValidationError(
                "Reward Program and Business Location must belong to the same business."
            )   
            
        if (
            self.processed_by_staff
            and business_id != self.processed_by_staff.business_id
        ):
            raise ValidationError(
                "Reward Program and Staff Member must belong to the same business."
            )   

        if (
            self.reward
            and self.reward_program_id != self.reward.reward_program_id
        ):
            raise ValidationError(
                "Reward Program and Reward Item must belong to the same business."
            )   