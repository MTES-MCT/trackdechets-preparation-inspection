from django.templatetags.static import static
from django.urls import reverse
from simple_menu import Menu, MenuItem


class StaffMenuItem(MenuItem):
    """Custom MenuItem that checks permissions based on the view associated
    with a URL"""

    def check(self, request):
        self.visible = request.user.is_staff


Menu.add_item("main", MenuItem("Préparer une fiche", reverse("prepare"), icon="tools"))

Menu.add_item("main", MenuItem("Contrôle routier", reverse("roadcontrol"), icon="report"))

Menu.add_item(
    "main",
    MenuItem(
        "Bordereau",
        reverse("roadcontrol_bsd_search"),
    ),
)

Menu.add_item(
    "main",
    StaffMenuItem(
        "Interface d'administration équipe",
        reverse("admin:index"),
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
    MenuItem(
        "Guide d'utilisation", static("user-manual/trackdechets-mode-emploi-fiche-inspection.pdf"), target="_blank"
    ),
)
