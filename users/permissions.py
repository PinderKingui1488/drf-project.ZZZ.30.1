from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class IsModer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='moderators').exists()