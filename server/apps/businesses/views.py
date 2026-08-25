from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from apps.businesses.serializers import BusinessRegisterSerializer

from apps.accounts.views import (
    set_auth_cookies,
    tokens_for,
)


class BusinessRegister(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serialized = BusinessRegisterSerializer(
            data = request.data,
            context = {
                'request': request
            }
        )

        if serialized.is_valid():

            registration = serialized.save()

            user = registration[
                'account_user'
            ]

            response = Response(
                {
                    'message':
                        'Business registered successfully.'
                },
                status = status.HTTP_201_CREATED
            )

            # If this was a new anonymous registration,
            # log the new account in automatically.
            if not request.user.is_authenticated:

                access, refresh = tokens_for(
                    user
                )

                return set_auth_cookies(
                    response,
                    access,
                    refresh
                )

            return response

        return Response(
            serialized.errors,
            status = status.HTTP_400_BAD_REQUEST
        )