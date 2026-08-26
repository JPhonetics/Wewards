from rest_framework.response import Response
from rest_framework import status

from apps.accounts.views import AccountUserView
from apps.businesses.models import (
    BusinessItem,
    BusinessStaff,
)
from apps.businesses.serializers import (
    BusinessItemSerializer,
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

        # Save the business object
        business = business_staff.business

        # Save all the item objects
        items = business.items.all()

        serialized = BusinessItemSerializer(
            items,
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
            
        serialized = BusinessItemSerializer(
            data = request.data,
        )
        
        # Save the item under this business object    
        if serialized.is_valid():
            serialized.save(
                business = business
            )

            return Response(
                {
                    'message':
                        'Business item added.'
                },
                status = status.HTTP_201_CREATED
            )

        return Response(
            serialized.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
        
    
class BusinessItemDetail(AccountUserView):

    def get(self, request, business_id, item_id):

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

        # Return the selected item under this business
        item = BusinessItem.objects.filter(
            id = item_id,
            business_id = business_id,
        ).first()

        if not item:
            return Response(
                {
                    'detail':
                        'Item not found.'
                },
                status = status.HTTP_404_NOT_FOUND
            )

        serialized = BusinessItemSerializer(
            item
        )

        return Response(
            serialized.data,
            status = status.HTTP_200_OK
        )

    def delete(self, request, business_id, item_id):

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

        # Return the selected item under this business
        item = BusinessItem.objects.filter(
            id = item_id,
            business_id = business_id,
        ).first()

        if not item:
            return Response(
                {
                    'detail':
                        'Item not found.'
                },
                status = status.HTTP_404_NOT_FOUND
            )

        item.delete()

        return Response(
            status = status.HTTP_204_NO_CONTENT
        )