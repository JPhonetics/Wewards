from django.db import models

class BillingStatusChoices(models.TextChoices):
    TRIAL = 'trial', 'Trial'
    ACTIVE = 'active', 'Active'
    PAST_DUE = 'past_due', 'Past Due'
    CANCELED = 'canceled', 'Canceled'
    
class BusinessRoleChoices(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    MANAGER = 'manager', 'Manager'
    EMPLOYEE = 'employee', 'Employee'
    
class ItemStatusChoices(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    ACTIVE = 'active', 'Active'
    UNAVAILABLE = 'unavailable', 'Unavailable'
    DISCONTINUED = 'discontinued', 'Discontinued'
    
class RewardAdjustmentChoices(models.TextChoices):
    OTHER = 'other', 'Other'
    
class RewardProgramStatusChoices(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    SCHEDULED = 'scheduled', 'Scheduled'
    ACTIVE = 'active', 'Active'
    PAUSED = 'paused', 'Paused'
    ENDED = 'ended', 'Ended'
    
class RewardTypeChoices(models.TextChoices):
    DISCOUNT_AMOUNT = 'discount_amount', 'Discount Amount'
    DISCOUNT_PERCENTAGE = 'discount_percentage', 'Discount Percentage'
    FREE_ITEM = 'free_item', 'Free Item'
    
class UserStatusChoices(models.TextChoices):
    PENDING = 'pending', 'Pending'
    ACTIVE = 'active', 'Active'
    SUSPENDED = 'suspended', 'Suspended'
    TERMINATED = 'terminated', 'Terminated'