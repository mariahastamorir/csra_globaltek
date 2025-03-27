from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from database.models import Usuario

class LoginSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        correo = data.get('correo')
        password = data.get('password')

        if not correo or not password:
            raise AuthenticationFailed('Se requieren correo y contraseña')

        usuario = authenticate(username=correo, password=password)
        if not usuario:
            raise AuthenticationFailed('Credenciales inválidas')

        if not usuario.is_active:
            raise AuthenticationFailed('Cuenta inactiva')

        # Generar token usando simplejwt
        refresh = RefreshToken.for_user(usuario)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': {
                'id': usuario.id,
                'correo': usuario.correo,
                'nombre': usuario.nombre,
            }
        }
