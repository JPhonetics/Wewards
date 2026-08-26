from rest_framework.response import Response
from rest_framework import status

from apps.accounts.views import AccountUserView
from apps.businesses.models import (
    BusinessStaff,
)
from apps.rewards.serializers import (
    RewardSerializer,
)
from core.lookups import (
    get_reward_program,
    get_rewards_by_business,
)
from core.validators import (
    validate_reward_program_match_business,
)


class RewardList(AccountUserView):

    def get(self, request, business_id):

        # Return the user's staff record for this business
        business_staff = BusinessStaff.objects.filter(
            business_id = business_id,
            user = request.user,
        ).first()

        if not business_staff:
            return Response(
                {
                    'detail':
                        'Business not found.'
                },
                status = status.HTTP_404_NOT_FOUND
            )

        rewards = get_rewards_by_business(
            business_id
        )

        serialized = RewardSerializer(
            rewards,
            many = True
        )

        return Response(
            serialized.data,
            status = status.HTTP_200_OK
        )
        
    def post(self, request, business_id):
            
        # Return the user's staff record for this business
        business_staff = BusinessStaff.objects.filter(
            business_id = business_id,
            user = request.user,
        ).first()

        if not business_staff:
            return Response(
                {
                    'detail':
                        'Business not found.'
                },
                status = status.HTTP_404_NOT_FOUND
            )

        # Save the business object
        business = business_staff.business

        # Get the selected reward program
        reward_program = get_reward_program(
            request.data.get('reward_program')
        )

        # Validate the reward program belongs to this business
        validate_reward_program_match_business(
            business,
            reward_program
        )
            
        serialized = RewardSerializer(
            data = request.data,
        )
        
        # Save the reward under this reward program
        if serialized.is_valid():
            serialized.save(
                reward_program = reward_program
            )

            return Response(
                {
                    'message':
                        'Business reward added.'
                },
                status = status.HTTP_201_CREATED
            )

        return Response(
            serialized.errors,
            status = status.HTTP_400_BAD_REQUEST
        )