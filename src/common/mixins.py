from braces.views._access import AccessMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class FullyLoggedMixin(AccessMixin):
    """
    This mixin extends AccessMixin to handle multi-factor authentication (MFA) and OIDC plus
    user category-based permissions. It ensures users are fully authenticated
    (two-factor verification or coming from OIDC) and belong to allowed user categories.

    Forbid access to :
     - non verified users (users logged with second factor)
     - users not coming from MonAIOT
     - user not having the relevant category

    User are redirected :
        - to verifiy page if they're logged in without second factor and not coming from MonAIOT
        - to login page if they're not logged.
    When fully logged, they're denied access if they do not have the right categories

    Attributes:
    allowed_user_categories (list): Categories of users allowed to access views
        using this mixin. Must be explicitly set in subclasses. Use ["*"]
        for unlimited access.

    Example:
    class SecureView(FullyLoggedMixin, View):
        allowed_user_categories = ['admin', 'manager']

        def get(self, request):
            return HttpResponse('Secure content')

    Note:
    - Place this mixin before other view classes in inheritance
    - Staff users automatically bypass category restrictions
    - Setting allowed_user_categories = ["*"] allows access to all authenticated users

    """

    allowed_user_categories = []

    def no_permissions_fail(self, request=None):
        """Handle failed permission checks by redirecting users appropriately."""
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("second_factor"))
        return redirect_to_login(
            request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name(),
        )

    def test_is_fullly_logged(self, user):
        """Verify if a user has completed all required authentication steps."""
        if not user.is_authenticated:
            return False
        is_verified_with_otp = user.is_verified()
        is_authenticated_from_monaiot = user.is_authenticated_from_monaiot()
        return is_verified_with_otp or is_authenticated_from_monaiot

    def get_allowed_user_categories(self):
        """Retrieve the list of allowed user categories.Raises an error if not set in the view"""
        if not self.allowed_user_categories:
            raise ImproperlyConfigured(
                f"{self.__class__.__name__} requires the `allowed_user_categories` attribute to be set"
            )

        return self.allowed_user_categories

    def check_has_right_categories(self, categories):
        """Verify if the user belongs to allowed categories."""
        if self.request.user.is_staff:
            return True

        if self.allowed_user_categories == ["*"]:
            return True

        user_category = self.request.user.user_category
        return user_category in categories

    def dispatch(self, request, *args, **kwargs):
        """Check if user is fully logged, then if has appropriate categories"""
        user_test_result = self.test_is_fullly_logged(request.user)

        if not user_test_result:
            return self.handle_no_permission(request)

        in_category = self.check_has_right_categories(self.get_allowed_user_categories())
        if not in_category:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)
