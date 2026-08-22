from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.db.models import Q


User = get_user_model()

class AccountUserBackend(BaseBackend):

    def authenticate(
        self,
        request,
        username = None,
        password = None,
        **kwargs
    ):
        if not username or not password:
            return None

        try:
            user = User.objects.get(
                Q(email = username) |
                Q(phone_number = username)
            )
            
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk = user_id)
        
        except User.DoesNotExist:
            return None