from django.conf import settings
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings

from .serializers import AccountUserSerializer


ACCESS_MAX_AGE = int(
    settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds()
)
REFRESH_MAX_AGE = int(
    settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].total_seconds()
)
REFRESH_COOKIE_PATH = "/api/v1/accounts/"


def set_auth_cookies(
    response, 
    access = None, 
    refresh = None
):
    common = {
        "httponly": True,
        "secure": settings.AUTH_COOKIE_SECURE,
        "samesite": settings.AUTH_COOKIE_SAMESITE
    }
    
    if access:
        response.set_cookie(
            "access", 
            access, 
            max_age = ACCESS_MAX_AGE, 
            path = "/", 
            **common
        )
        
    if refresh:
        response.set_cookie(
            "refresh", 
            refresh, 
            max_age = REFRESH_MAX_AGE, 
            path = REFRESH_COOKIE_PATH, 
            **common
        )
    
    return response


def clear_auth_cookies(response):
    response.delete_cookie(
        "access", 
        path = "/"
    )
    
    response.delete_cookie(
        "refresh", 
        path = REFRESH_COOKIE_PATH
    )
    
    return response


def tokens_for(user):
    refresh = RefreshToken.for_user(user)
    
    return str(refresh.access_token), str(refresh)


class JWTCookieAuthentication(JWTAuthentication):
    
    def authenticate(self, request):
        raw_token = request.COOKIES.get("access")
        
        if raw_token is None:
            return None
        
        validated_token = self.get_validated_token(raw_token)
        
        return self.get_user(validated_token), validated_token


class AccountUserRegistration(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        serialized = AccountUserSerializer(
            data = request.data
        )
        
        if serialized.is_valid():
            new_user = serialized.save()
            
            access, refresh = tokens_for(new_user)
            
            response = Response(
                AccountUserSerializer(new_user).data,
                status = status.HTTP_201_CREATED
            )
            
            return set_auth_cookies(response, access, refresh)
            
        return Response(
            serialized.errors,
            status = status.HTTP_400_BAD_REQUEST
        )
        

class AccountUserLogin(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        
        username = request.data.get("email") or request.data.get("phone_number")

        if not username:
            return Response(
                "Email or phone number is required.",
                status = status.HTTP_400_BAD_REQUEST
            )
        
        username = username.strip().casefold()
        
        password = request.data.get("password")

        if not password:
            return Response(
                "Password is required.",
                status = status.HTTP_400_BAD_REQUEST
            )
        
        user = authenticate(
            username = username,
            password = password,
        )
        
        if user:
            access, refresh = tokens_for(user)
            
            response = Response(
                f"Welcome, {username}",
                status = status.HTTP_200_OK
            )
            
            return set_auth_cookies(response, access, refresh)
            
        return Response(
           "Invalid credentials.", 
           status = status.HTTP_401_UNAUTHORIZED
        )


class AccountUserRefresh(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        raw_refresh = request.COOKIES.get("refresh")
        
        if not raw_refresh:
            return Response(
                {"detail":"No refresh Token"}, 
                status = status.HTTP_401_UNAUTHORIZED
                )
        try:
            refresh = RefreshToken(raw_refresh)
            
        except TokenError:
            return clear_auth_cookies(
                Response(
                    {"detail":"Invalid or expired refresh Token"},
                    status = status.HTTP_401_UNAUTHORIZED
                )
            )
        access = str(refresh.access_token)
        
        new_refresh = None
        # Check SimpleJWT's settings to see whether refresh-token
        # rotation has been enabled.
        #
        # Rotation means every time a refresh token is used,
        # we replace it with a newly generated refresh token.
        if api_settings.ROTATE_REFRESH_TOKENS:
            # If refresh-token blacklisting is also enabled,
            # invalidate the old refresh token after it has been used.
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    refresh.blacklist()
                except AttributeError:
                    pass
            # Give the refresh token a new unique JWT ID ("jti").
            #
            # This helps distinguish the new rotated token from
            # the old refresh token.    
            refresh.set_jti()
            #new expiration time
            refresh.set_exp()
            # set a new issued at timestamp
            refresh.set_iat()
            new_refresh = str(refresh)
        response = Response({"refreshed":True})
        return set_auth_cookies(response, access, new_refresh)   

class AccountUserView(APIView):
    authentication_classes = [JWTCookieAuthentication]
    permission_classes = [IsAuthenticated]
        
        
class AccountUserInfo(AccountUserView):
    
    def get(self, request):
        user = request.user
        
        return Response(
            f"User: {user.email or user.phone_number}",
        )


class AccountUserLogout(AccountUserView):
    
    def post(self, request):
        raw_refresh = request.COOKIES.get("refresh")
        
        if raw_refresh:
            try:
                RefreshToken(raw_refresh).blacklist()
                
            except TokenError:
                pass
            
        return clear_auth_cookies(Response({"detail":"logged out"}))