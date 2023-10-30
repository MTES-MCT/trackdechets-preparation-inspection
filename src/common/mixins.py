from braces.views import UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class SecondFactorMixin(UserPassesTestMixin):
    """
    Forbid access to non verified user (user logged with second factor).
    Redirect them :
        - to verifiy page if they'rr logged in without second factor
        - to login page if they're not logged.

    """

    def test_func(self, user):
        return user.is_authenticated and user.is_verified()

    def no_permissions_fail(self, request=None):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("second_factor"))
        return redirect_to_login(
            request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name(),
        )
