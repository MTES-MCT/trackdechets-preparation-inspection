import factory

from .models import ComputedInspectionData


class ComputedInspectionDataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ComputedInspectionData

    org_id = factory.Sequence(lambda n: str(n))
    company_name = factory.Sequence(lambda n: f"company {n}")
