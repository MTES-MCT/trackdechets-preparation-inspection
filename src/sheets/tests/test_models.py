import datetime as dt

import pytest
from django.utils import timezone

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


def test_computed_inspection_data_to_void():
    a_lot_more_than_three_month_ago = timezone.now() - dt.timedelta(days=4 * 30)
    more_than_three_month_ago = timezone.now() - dt.timedelta(days=3 * 30 + 5)
    less_than_three_month_ago = timezone.now() - dt.timedelta(days=3 * 30 - 5)
    computed_a_lot_more_than_three_month_ago = ComputedInspectionDataFactory(created=a_lot_more_than_three_month_ago)
    computed_more_than_three_month_ago = ComputedInspectionDataFactory(created=more_than_three_month_ago)
    computed_less_than_three_month_ago = ComputedInspectionDataFactory(created=less_than_three_month_ago)
    computed_today = ComputedInspectionDataFactory()
    to_void = ComputedInspectionData.objects.to_void()

    pks = [sheet.pk for sheet in to_void]

    assert computed_a_lot_more_than_three_month_ago.pk in pks
    assert computed_more_than_three_month_ago.pk in pks
    assert computed_less_than_three_month_ago.pk not in pks
    assert computed_today.pk not in pks
