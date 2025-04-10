from rest_framework import serializers

from sheets.constants import COMPANY_TYPES

from .centroids import DEPARTMENTS_CENTROIDS, REGIONS_CENTROIDS
from .models import CartoCompany


class BaseCompanySerializer(serializers.Serializer):
    name = serializers.SerializerMethodField()

    lat = serializers.SerializerMethodField()
    long = serializers.SerializerMethodField()
    count = serializers.IntegerField(source="cnt")
    admin_unit_field = ""
    centroids = {}

    def get_region(self, obj):
        """Cache result"""
        if not obj.get("_cached_admin_unit"):
            code_admin_unit = str(obj[self.admin_unit_field])
            obj["_cached_region"] = self.centroids[code_admin_unit]

        return obj["_cached_region"]

    def get_name(self, obj):
        region = self.get_region(obj)
        return region["name"]

    def get_lat(self, obj):
        region = self.get_region(obj)
        return region["lat"]

    def get_long(self, obj):
        region = self.get_region(obj)
        return region["long"]


class RegionCompanySerializer(BaseCompanySerializer):
    admin_unit_field = "code_region_insee"
    centroids = REGIONS_CENTROIDS


class DepartmentCompanySerializer(BaseCompanySerializer):
    admin_unit_field = "code_departement_insee"
    centroids = DEPARTMENTS_CENTROIDS


WASTE_NAMES = [
    "Déchets dangereux",
    "Amiante",
    "Fluides Frigorigènes",
    "Dasri",
    "Vehicules hors d'usage",
    "Sortie de statut de déchet",
    "Déchets non dangereux",
    "Terres et sédiments - DD",
    "Terres et sédiments - DND",
]


class CompanySerializer(serializers.ModelSerializer):
    lat = serializers.SerializerMethodField()
    long = serializers.SerializerMethodField()
    wastes = serializers.SerializerMethodField()
    profiles = serializers.SerializerMethodField()

    class Meta:
        model = CartoCompany
        fields = ("siret", "nom_etablissement", "adresse_td", "lat", "long", "wastes", "profiles")

    def get_lat(self, obj):
        return obj.coords[1]

    def get_long(self, obj):
        return obj.coords[0]

    def get_wastes(self, obj):
        vector = [obj.bsdd, obj.bsda, obj.bsff, obj.bsdasri, obj.bsvhu, obj.ssd, obj.bsdnd, obj.texs_dd, obj.texs]
        return ", ".join([n for i, n in enumerate(WASTE_NAMES) if vector[i]])

    def get_profiles(self, obj):
        if not obj.profils:
            return ""

        return ", ".join([COMPANY_TYPES.get(p) for p in obj.profils if p in COMPANY_TYPES])


class ClusterSerializer(serializers.Serializer):
    lat = serializers.SerializerMethodField()
    long = serializers.SerializerMethodField()
    count = serializers.IntegerField()

    def get_lat(self, obj):
        return obj["location"].coords[1]

    def get_long(self, obj):
        return obj["location"].coords[0]
