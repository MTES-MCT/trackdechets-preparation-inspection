from braces.views import UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class FullyLoggedMixin(UserPassesTestMixin):
    """
    Forbid access to :
     - non verified users (users logged with second factor)
     - users not coming from MonAIOT
    Redirect them :
        - to verifiy page if they're logged in without second factor and not coming from MonAIOT
        - to login page if they're not logged.

    """

    def test_func(self, user):
        if not user.is_authenticated:
            return False
        is_verified_with_otp = user.is_verified()
        is_authenticated_from_monaiot = user.is_authenticated_from_monaiot()
        return is_verified_with_otp or is_authenticated_from_monaiot

    def no_permissions_fail(self, request=None):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("second_factor"))
        return redirect_to_login(
            request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name(),
        )
