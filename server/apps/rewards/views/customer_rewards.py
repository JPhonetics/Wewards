from rest_framework.response import Response
from rest_framework import status

from apps.accounts.views import AccountUserView
from apps.rewards.serializers.customer_rewards import (
    CustomerRewardsSerializer,
)
from apps.rewards.services.customer_rewards import (
    get_customer_rewards,
)


class CustomerRewards(AccountUserView):

    def get(self, request):

        # data comes back as a list of customer reward dictionaries
        customer_rewards = get_customer_rewards(
            request.user.id
        )

        # run customer_rewards through the serializer
        serializer = CustomerRewardsSerializer(
            customer_rewards,
            many = True
        )

        return Response(
            serializer.data,
            status = status.HTTP_200_OK
        )