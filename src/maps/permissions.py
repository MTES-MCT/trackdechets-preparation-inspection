from rest_framework import permissions


class UserIsVerifedPermission(permissions.BasePermission):
    message = "User not verifed"

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False
        is_verified_with_otp = user.is_verified()
        is_authenticated_from_monaiot = user.is_authenticated_from_monaiot()
        return is_verified_with_otp or is_authenticated_from_monaiot
