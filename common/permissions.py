from rest_framework import permissions


class GeneralPermission(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")
    user_type = None

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.type.lower() == self.user_type

    def has_object_permission(self, request, view, obj):
        return request.user.type.lower() == self.user_type


class IsAdmin(GeneralPermission):
    user_type = "admin"


class IsStaff(GeneralPermission):
    user_type = "staff"


class IsEmployee(GeneralPermission):
    user_type = "employee"


class IsOwner(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user or request.user.employee == obj.employee
