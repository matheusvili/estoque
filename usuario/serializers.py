from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 're'  # agora usamos 're' em vez de 'email'

    def validate(self, attrs):
        re = attrs.get('re')
        password = attrs.get('password')

        # autentica usando 're' e 'password'
        user = authenticate(request=self.context.get('request'), re=re, password=password)

        if not user:
            raise serializers.ValidationError('Usuário e/ou senha incorreto(s)')

        data = super().validate({
            'username': user.re,
            'password': password
        })

        return data
