import factory
from factory.django import DjangoModelFactory

from accounts.factories import UserFactory

from .models import RegistryV2Export


class RegistryV2ExportFactory(DjangoModelFactory):
    """Factory for the RegistryV2Export model."""

    class Meta:
        model = RegistryV2Export

    siret = factory.Sequence(lambda n: str(n))
    created_by = factory.SubFactory(UserFactory)
