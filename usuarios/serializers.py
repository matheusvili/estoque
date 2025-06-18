from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'id',
            're',
            'email',
            'first_name',
            'last_name',
            'is_staff',
            'is_superuser',
            'password',
        ]

    def create(self, validated_data):
        # Cria o usuário usando set_password para criptografar a senha
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        # Atualiza o usuário com tratamento da senha
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 're'  # agora usamos 're' em vez de 'email'

    def validate(self, attrs):
        re = attrs.get('re')
        password = attrs.get('password')

        # autentica usando 're' e 'password'
        user = authenticate(request=self.context.get(
            'request'), re=re, password=password)

        if not user:
            raise serializers.ValidationError(
                'Usuário e/ou senha incorreto(s)')

        data = super().validate({
            'username': user.re,
            'password': password
        })

        return data
