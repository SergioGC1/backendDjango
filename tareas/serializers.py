from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tarea
# Si usas CustomTokenObtainPairSerializer, aquí también lo importas

# 📌 Serializer para la app de tareas
class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
        read_only_fields = ['usuario', 'creada_en']

# 📌 Serializer para registro
class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user
