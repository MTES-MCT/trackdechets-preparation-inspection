from django.urls import reverse
from simple_menu import Menu, MenuItem


class StaffMenuItem(MenuItem):
    """Custom MenuItem that checks permissions based on the view associated with a URL"""

    def check(self, request):
        self.visible = request.user.is_staff


class MainMenuItem(MenuItem):
    """User is staff and not an observatoire"""

    def check(self, request):
        self.visible = request.user.is_staff or not request.user.is_observatoire


class ObservatoireMenuItem(MenuItem):
    """Custom MenuItem that checks permissions based on the view associated with a URL"""

    def check(self, request):
        self.visible = request.user.is_staff or request.user.is_observatoire or request.user.is_administration_centrale


submenu = (
    MainMenuItem("Préparer une fiche", reverse("sheet_prepare"), icon="tools"),
    MainMenuItem("Registre exhaustif", reverse("registry_prepare"), icon="tools"),
    MainMenuItem("Exports (Registre V2)", reverse("registry_v2_list"), icon="tools"),
)
Menu.add_item("main", MenuItem("Établissements", "", children=submenu, menu_id="id_companies"))

Menu.add_item("main", MainMenuItem("Contrôle routier", reverse("roadcontrol"), icon="report"))

Menu.add_item(
    "main",
    MainMenuItem(
        "Bordereau",
        reverse("roadcontrol_bsd_search"),
    ),
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
    ObservatoireMenuItem(
        "Observatoires",
        reverse("data_export_list"),
    ),
)
