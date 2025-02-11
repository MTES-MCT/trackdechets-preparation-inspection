import datetime as dt

import pytest
from django.core.management import call_command
from django.utils import timezone

from ..factories import ComputedInspectionDataFactory

pytestmark = pytest.mark.django_db


def test_void_sheets_command():
    a_lot_more_than_three_month_ago = timezone.now() - dt.timedelta(days=4 * 30)
    more_than_three_month_ago = timezone.now() - dt.timedelta(days=3 * 30 + 5)
    less_than_three_month_ago = timezone.now() - dt.timedelta(days=3 * 30 - 5)
    computed_a_lot_more_than_three_month_ago = ComputedInspectionDataFactory(
        created=a_lot_more_than_three_month_ago,
        bsdd_created_rectified_data={"lorem": "ipsum"},
        rndts_transporter_quantities_graph="blabla",
    )
    computed_more_than_three_month_ago = ComputedInspectionDataFactory(
        created=more_than_three_month_ago,
        bsdd_created_rectified_data={"lorem": "ipsum"},
        rndts_transporter_quantities_graph="blabla",
    )
    computed_less_than_three_month_ago = ComputedInspectionDataFactory(
        created=less_than_three_month_ago,
        bsdd_created_rectified_data={"lorem": "ipsum"},
        rndts_transporter_quantities_graph="blabla",
    )
    computed_today = ComputedInspectionDataFactory(
        bsdd_created_rectified_data={"lorem": "ipsum"}, rndts_transporter_quantities_graph="blabla"
    )

    call_command("void_sheets")
    computed_a_lot_more_than_three_month_ago.refresh_from_db()
    computed_more_than_three_month_ago.refresh_from_db()
    computed_less_than_three_month_ago.refresh_from_db()
    computed_today.refresh_from_db()

    # voided
    assert computed_a_lot_more_than_three_month_ago.bsdd_created_rectified_data == {}
    assert computed_a_lot_more_than_three_month_ago.rndts_transporter_quantities_graph == ""
    assert computed_a_lot_more_than_three_month_ago.voided
    assert computed_more_than_three_month_ago.bsdd_created_rectified_data == {}
    assert computed_more_than_three_month_ago.rndts_transporter_quantities_graph == ""
    assert computed_more_than_three_month_ago.voided

    # non voided
    assert computed_less_than_three_month_ago.bsdd_created_rectified_data == {"lorem": "ipsum"}
    assert computed_less_than_three_month_ago.rndts_transporter_quantities_graph == "blabla"
    assert not computed_less_than_three_month_ago.voided
    assert computed_today.bsdd_created_rectified_data == {"lorem": "ipsum"}
    assert computed_today.rndts_transporter_quantities_graph == "blabla"
    assert not computed_today.voided
