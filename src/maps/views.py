from django.views.generic import TemplateView

from accounts.constants import PERMS_MAP_ICPE, UserCategoryChoice
from common.mixins import FullyLoggedMixin


class MapView(FullyLoggedMixin, TemplateView):
    template_name = "maps/map.html"
    allowed_user_categories = [UserCategoryChoice.STAFF_TD]


class ExutMapView(FullyLoggedMixin, TemplateView):
    template_name = "maps/icpe_map.html"
    allowed_user_categories = PERMS_MAP_ICPE
