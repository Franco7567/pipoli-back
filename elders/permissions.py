from rest_framework.permissions import BasePermission


class ElderPermission(BasePermission):

    def has_permission(self, request, view):

        # usuario no autenticado
        if not request.user.is_authenticated:
            return False

        # admin puede todo
        if request.user.role == 'admin':
            return True

        # clientes pueden ver y crear
        if request.user.role == 'client':
            return True

        # cuidadores solo lectura
        if request.user.role == 'caregiver':

            if request.method in ['GET']:
                return True

        return False