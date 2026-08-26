from rest_framework.response import Response
from rest_framework import status

from apps.accounts.views import AccountUserView
from apps.businesses.models import (
    BusinessStaff,
)
from apps.businesses.serializers import (
    BusinessStaffSerializer,
)
from core.lookups import (
    get_business_staff_by_user,
)


class BusinessStaffInfo(AccountUserView):

    def get(self, request):

        business_staff = get_business_staff_by_user(
            request.user.id
        )

        # Serialize all BusinessStaff records for the user
        serialized = BusinessStaffSerializer(
            business_staff,
            many = True
        )

        return Response(
            serialized.data,
            status = status.HTTP_200_OK
        )


class BusinessStaffList(AccountUserView):

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

        # Save all the staff objects
        staff = business.staff.all()

        serialized = BusinessStaffSerializer(
            staff,
            many = True
        )

        return Response(
            serialized.data,
            status = status.HTTP_200_OK
        )