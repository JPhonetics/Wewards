from rest_framework.response import Response
from rest_framework import status

from apps.accounts.views import AccountUserView
from apps.businesses.models import (
    BusinessStaff,
)
from apps.rewards.models import (
    RewardProgramType,
)
from apps.rewards.serializers import (
    RewardProgramTypeSerializer,
    RewardProgramSerializer,
)


class RewardProgramTypesList(AccountUserView):

    def get(self, request):

        reward_program_types = RewardProgramType.objects.all()

        serialized = RewardProgramTypeSerializer(
            reward_program_types,
            many = True
        )

        return Response(
            serialized.data,
            status = status.HTTP_200_OK
        )


class RewardProgramsList(AccountUserView):

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

        # Save the business object
        business = business_staff.business

        # Save all the reward program objects
        reward_programs = business.reward_programs.all()

        serialized = RewardProgramSerializer(
            reward_programs,
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

        serialized = RewardProgramSerializer(
            data = request.data
        )

        # Save the reward program under this business object
        if serialized.is_valid():
            serialized.save(
                business = business
            )

            return Response(
                {
                    'message':
                        'Reward program added.'
                },
                status = status.HTTP_201_CREATED
            )

        return Response(
            serialized.errors,
            status = status.HTTP_400_BAD_REQUEST
        )