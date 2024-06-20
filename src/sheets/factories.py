import factory

from .models import ComputedInspectionData


class ComputedInspectionDataFactory(factory.django.DjangoModelFactory):
    """Sheet created by web ui"""

    class Meta:
        model = ComputedInspectionData

    org_id = factory.Sequence(lambda n: str(n))
    company_name = factory.Sequence(lambda n: f"company {n}")


class ApiComputedInspectionDataFactory(ComputedInspectionDataFactory):
    """Sheet created by api"""

    creation_mode = ComputedInspectionData.CreationModeChoice.API
