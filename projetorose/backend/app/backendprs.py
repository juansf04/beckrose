from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User 

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            print(f"Usuário encontrado: {user.email}, ativo: {user.is_active}")
            if user and user.is_active and check_password(password, user.senha):
                return user
            else:
                print("Usuário ou senha incorretos.")
                return None
        except User.DoesNotExist:
            print("Usuário não encontrado.")
            return None

    def get_user(self, id_user):
        try:
            return User.objects.get(pk=id_user)
        except User.DoesNotExist:
            return None