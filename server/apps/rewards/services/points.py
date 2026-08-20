from django.core.exceptions import ValidationError
from django.db.models import Sum
from apps.accounts.models import *
from apps.rewards.models import *
from core.lookups import *


def calculate_balance(user_id, reward_program_id):
    user = get_account_user(user_id)
    
    reward_program = get_reward_program(reward_program_id)
    
    

def eligible_rewards():
    pass


def award_points():
    pass


def redeem_points():
    pass