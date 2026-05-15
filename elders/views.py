from rest_framework import viewsets

from .models import Elder
from .serializers import ElderSerializer
from .permissions import ElderPermission


class ElderViewSet(viewsets.ModelViewSet):

    serializer_class = ElderSerializer
    permission_classes = [ElderPermission]

    def get_queryset(self):

        user = self.request.user

        if user.role == 'admin':
            return Elder.objects.all()

        if user.role == 'client':
            return Elder.objects.filter(client=user)

        if user.role == 'caregiver':
            return Elder.objects.filter(caregivers=user)

        return Elder.objects.none()

    def get_serializer_context(self):
        return {'request': self.request}