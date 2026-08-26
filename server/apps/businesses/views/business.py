from rest_framework.response import Response
from rest_framework import status

from apps.accounts.views import AccountUserView
from apps.businesses.models import (
    BusinessStaff,
)
from apps.businesses.serializers import (
    BusinessRegisterSerializer,
    BusinessSerializer,
    BusinessStaffSerializer,
)
from core.lookups import (
    get_rewards_by_business,
)


class BusinessRegister(AccountUserView):

    def post(self, request):

        # Feed the request data and auth user into the serializer
        serialized = BusinessRegisterSerializer(
            data = request.data,
            context = {
                'request': request
            }
        )

        if serialized.is_valid():
            serialized.save()

            return Response(
                {
                    'message':
                        'Business registered successfully.'
                },
                status = status.HTTP_201_CREATED
            )

        return Response(
            serialized.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
        
        
class BusinessDetail(AccountUserView):

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

        serialized = BusinessStaffSerializer(
            business_staff
        )

        return Response(
            serialized.data,
            status = status.HTTP_200_OK
        )


    def patch(self, request, business_id):

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

        business = business_staff.business

        serialized = BusinessSerializer(
            business,
            data = request.data,
            partial = True
        )

        if serialized.is_valid():
            serialized.save()

            return Response(
                serialized.data,
                status = status.HTTP_200_OK
            )

        return Response(
            serialized.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
        
        
class BusinessStats(AccountUserView):

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

        business = business_staff.business
        
        rewards = get_rewards_by_business(business.id)

        stats = {
            'locations': business.locations.count(),
            'staff': business.staff.count(),
            'items': business.items.count(),
            'reward_programs': business.reward_programs.count(),
            'rewards': rewards.count(),
        }

        return Response(
            stats,
            status = status.HTTP_200_OK
        )