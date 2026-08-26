from rest_framework.response import Response
from rest_framework import status

from apps.accounts.views import AccountUserView
from apps.businesses.models import (
    BusinessItem,
    BusinessLocation,
    BusinessStaff,
)

from apps.businesses.serializers import (
    BusinessItemSerializer,
    BusinessLocationSerializer,
    BusinessRegisterSerializer,
    BusinessSerializer,
    BusinessStaffSerializer,
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
        
    
class BusinessStaffInfo(AccountUserView):

    def get(self, request):

        business_staff = BusinessStaff.objects.filter(
            user = request.user
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

        stats = {
            'locations': business.locations.count(),
            'staff': business.staff.count(),
            'items': business.items.count(),
        }

        return Response(
            stats,
            status = status.HTTP_200_OK
        )


class BusinessLocations(AccountUserView):

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

        locations = BusinessLocation.objects.filter(
            business_id = business_id
        )

        serialized = BusinessLocationSerializer(
            locations,
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

        staff = BusinessStaff.objects.filter(
            business_id = business_id
        )

        serialized = BusinessStaffSerializer(
            staff,
            many = True
        )

        return Response(
            serialized.data,
            status = status.HTTP_200_OK
        )


class BusinessItems(AccountUserView):

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

        items = BusinessItem.objects.filter(
            business_id = business_id
        )

        serialized = BusinessItemSerializer(
            items,
            many = True
        )

        return Response(
            serialized.data,
            status = status.HTTP_200_OK
        )