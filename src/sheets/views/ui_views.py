from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from accounts.constants import ALL_USER_CATEGORIES
from common.mixins import FullyLoggedMixin


class PublicHomeView(TemplateView):
    template_name = "public_home.html"

    def get(self, request, *args, **kwargs):
        """Redirect user to private home or second_factor page wether they're logged in or verified."""
        if request.user.is_verified() or request.user.is_authenticated_from_oidc():
            return HttpResponseRedirect(reverse_lazy("private_home"))
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("second_factor"))
        return super().get(request, *args, **kwargs)


class PrivateHomeView(FullyLoggedMixin, TemplateView):
    template_name = "private_home.html"
    allowed_user_categories = ALL_USER_CATEGORIES
