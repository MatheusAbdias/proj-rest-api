from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Permite o usuario editar o proprio perfil"""

    def has_object_permissions(self, request, view, obj):
        """Checa se o usuario esta tentando editar o proprio pefil"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
