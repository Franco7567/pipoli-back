from rest_framework import serializers
from .models import Elder


class ElderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Elder
        fields = '__all__'

    def create(self, validated_data):

        request = self.context['request']
        user = request.user

        # si es cliente, se asigna automáticamente
        if user.role == 'client':
            validated_data['client'] = user

        return super().create(validated_data)