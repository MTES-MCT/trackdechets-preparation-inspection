from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from accounts.models import ALL_USER_CATEGORIES
from common.mixins import FullyLoggedMixin
from content.models import FeedbackResult


class PublicHomeView(TemplateView):
    template_name = "public_home.html"

    def get(self, request, *args, **kwargs):
        """Redirect user to private home or second_factor page wether they're logged in or verified."""
        if request.user.is_verified():
            return HttpResponseRedirect(reverse_lazy("private_home"))
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy("second_factor"))
        return super().get(request, *args, **kwargs)


class PrivateHomeView(FullyLoggedMixin, TemplateView):
    template_name = "private_home.html"
    allowed_user_categories = ALL_USER_CATEGORIES

    def has_filled_survey(self):
        return FeedbackResult.objects.filter(author=self.request.user.email).exists()

    def get_context_data(self, **kwargs):
        # display survey links until user fills it
        return super().get_context_data(**kwargs, has_filled_survey=self.has_filled_survey())
