from rest_framework.response import Response
from rest_framework import status

from apps.accounts.views import AccountUserView
from apps.businesses.models import (
    BusinessLocation,
    BusinessStaff,
)
from apps.businesses.serializers import (
    BusinessLocationSerializer,
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

        # Save the business object
        business = business_staff.business

        # Save all the location objects
        locations = business.locations.all()

        serialized = BusinessLocationSerializer(
            locations,
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
            
        serialized = BusinessLocationSerializer(
            data = request.data,
        )
        
        # Save the location under this business object    
        if serialized.is_valid():
            serialized.save(
                business = business
            )

            return Response(
                {
                    'message':
                        'Business location added.'
                },
                status = status.HTTP_201_CREATED
            )

        return Response(
            serialized.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
        
        
class BusinessLocationDetail(AccountUserView):

    def get(self, request, business_id, location_id):

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

        # Return the selected location under this business
        location = BusinessLocation.objects.filter(
            id = location_id,
            business_id = business_id,
        ).first()

        if not location:
            return Response(
                {
                    'detail':
                        'Location not found.'
                },
                status = status.HTTP_404_NOT_FOUND
            )

        serialized = BusinessLocationSerializer(
            location
        )

        return Response(
            serialized.data,
            status = status.HTTP_200_OK
        )

    def delete(self, request, business_id, location_id):

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

        # Return the selected location under this business
        location = BusinessLocation.objects.filter(
            id = location_id,
            business_id = business_id,
        ).first()

        if not location:
            return Response(
                {
                    'detail':
                        'Location not found.'
                },
                status = status.HTTP_404_NOT_FOUND
            )

        location.delete()

        return Response(
            status = status.HTTP_204_NO_CONTENT
        )