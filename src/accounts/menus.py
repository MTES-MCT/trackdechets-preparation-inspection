from django.urls import reverse
from simple_menu import Menu, MenuItem

from accounts.constants import PERMS_BSD, PERMS_DATA_EXPORT, PERMS_ROAD_CONTROL, PERMS_SHEET_AND_REGISTRY


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
    PermsItem("Préparer une fiche", reverse("sheet_prepare"), allowed_categories=PERMS_SHEET_AND_REGISTRY),
    PermsItem("Exports (Registre V2)", reverse("registry_v2_list"), allowed_categories=PERMS_SHEET_AND_REGISTRY),
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
    PermsItem("Bordereau", reverse("roadcontrol_bsd_search"), allowed_categories=PERMS_BSD),
)

Menu.add_item(
    "main",
    StaffMenuItem(
        "Cartographie",
        reverse("map_view"),
    ),
)

Menu.add_item(
    "main",
    PermsItem("Observatoires", reverse("data_export_list"), allowed_categories=PERMS_DATA_EXPORT),
)
