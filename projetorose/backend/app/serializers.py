from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Plantas

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    senha = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        senha = data.get('senha')

        user = authenticate(request=self.context.get('request'), email=email, senha=senha)

        if not user:
            raise serializers.ValidationError("Usuário ou senha incorretos")

       
        refresh = RefreshToken.for_user(user)

      
        user_plantas = self.get_user_planta(user)

       
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'user_plantas': user_plantas,
        }

    def get_user_planta(self, user):
        
        user_plantas = user_plantas.all()
        
        return plantaSerializer(user_plantas, many=True).data


class plantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantas
        fields = ['id_planta', 'nome_planta', 'tipo_planta']