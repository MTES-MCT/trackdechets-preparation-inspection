from django.views.generic import TemplateView

from accounts.constants import UserCategoryChoice
from common.mixins import FullyLoggedMixin


class MapView(FullyLoggedMixin, TemplateView):
    template_name = "maps/map.html"
    allowed_user_categories = [UserCategoryChoice.STAFF_TD]
