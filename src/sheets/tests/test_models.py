import pytest

from ..factories import ComputedInspectionDataFactory
from ..models import ComputedInspectionData

pytestmark = pytest.mark.django_db


def test_computed_inspection_data_factory():
    computed = ComputedInspectionDataFactory()
    assert computed.pk


def test_computed_inspection_data_mark_as_failed(mailoutbox):
    computed = ComputedInspectionDataFactory()
    ComputedInspectionData.objects.mark_as_failed(computed.pk)

    assert len(mailoutbox) == 1
    email = mailoutbox[0]
    assert email.to == ["lorem@ipsum.lol"]
    assert email.subject == "Une fiche d'inspection est en erreur"
    assert email.body == f"La fiche d'inspection {computed.pk} est en erreur"
