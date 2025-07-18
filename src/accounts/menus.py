from django.urls import reverse
from simple_menu import Menu, MenuItem

from accounts.constants import (
    PERMS_BSD_SEARCH,
    PERMS_DATA_EXPORT,
    PERMS_MAP,
    PERMS_MAP_ICPE,
    PERMS_ROAD_CONTROL,
    PERMS_SHEET_AND_REGISTRY,
)


class StaffMenuItem(MenuItem):
    """Custom MenuItem that checks permissions based on the view associated with a URL"""

    def check(self, request):
        self.visible = request.user.is_staff


class PermsItem(MenuItem):
    """User is staff and not an observatoire"""

    def check(self, request):
        allowed_categories = getattr(self, "allowed_categories", [])
        self.visible = request.user.is_staff or request.user.user_category in allowed_categories


submenu = (
    PermsItem("Fiche établissement", reverse("sheet_prepare"), allowed_categories=PERMS_SHEET_AND_REGISTRY),
    PermsItem("Registre établissement", reverse("registry_v2_prepare"), allowed_categories=PERMS_SHEET_AND_REGISTRY),
)
Menu.add_item(
    "main",
    MenuItem(
        "Établissements",
        "nevermatch",  # do not highlight except when submenu items are selected
        children=submenu,
        menu_id="id_companies",
        allowed_categories=PERMS_SHEET_AND_REGISTRY,
    ),
)
#
Menu.add_item("main", PermsItem("Contrôle routier", reverse("roadcontrol"), allowed_categories=PERMS_ROAD_CONTROL))

Menu.add_item(
    "main",
    PermsItem("Bordereau", reverse("roadcontrol_bsd_search"), allowed_categories=PERMS_BSD_SEARCH),
)

Menu.add_item(
    "main",
    PermsItem("Cartographie", reverse("map_view"), allowed_categories=PERMS_MAP),
)
Menu.add_item(
    "main",
    PermsItem("Carte des ICPE", reverse("icpe_map_view"), allowed_categories=PERMS_MAP_ICPE),
)

Menu.add_item(
    "main",
    PermsItem("Observatoires", reverse("data_export_list"), allowed_categories=PERMS_DATA_EXPORT),
)

Menu.add_item(
    "main",
    StaffMenuItem("Admin équipe", reverse("admin:index")),
)
