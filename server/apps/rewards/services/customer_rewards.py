from apps.rewards.services.points import (
    points_calculate_balance,
    points_all_rewards,
)
from apps.rewards.services.punch_card import (
    punch_card_calculate_progress_all,
)
from core.lookups import (
    get_reward_programs_by_user,
)


# Functions that require both program types
# Notes: login with post for token, then get will work

def get_customer_rewards(
    user_id,
):

    reward_programs = get_reward_programs_by_user(
        user_id
    )

    customer_rewards = {}

    for reward_program in reward_programs:

        business = reward_program.business

        # create a dictionary for the business if it doesn't exist yet
        if business.id not in customer_rewards:

            customer_rewards[business.id] = {
                'business':
                    business,
                'reward_programs':
                    [],
            }

        # starting dictionary as we loop through each reward_program
        reward_data = {
            'reward_program':
                reward_program,
        }

        # If the type is points calculate the balance and add it to the 
        # dictionary
        if reward_program.program_type.name == "Points":

            balance = points_calculate_balance(
                user_id,
                reward_program.id
            )

            rewards = points_all_rewards(
                reward_program.id
            )

            rewards_with_eligibility = []

            for reward in rewards:

                rewards_with_eligibility.append({
                    'reward':
                        reward,
                    'eligible':
                        balance >= reward.amount_required,
                })

            reward_data['balance'] = balance
            reward_data['rewards'] = rewards_with_eligibility

        # if the type is punch card run it through the method and place the
        # output inside rewards
        elif reward_program.program_type.name == "Punch Card":

            reward_data['rewards'] = punch_card_calculate_progress_all(
                user_id,
                reward_program.id
            )

        # append each reward program dictionary to the business
        customer_rewards[business.id]['reward_programs'].append(
            reward_data
        )

    return list(
        customer_rewards.values()
    )