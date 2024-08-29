import pytest

from ..factories import PdfBundleFactory
from ..models import PdfBundle

pytestmark = pytest.mark.django_db


def test_pdf_bundle_manager():
    PdfBundleFactory(state=PdfBundle.BundleChoice.INITIAL)
    PdfBundleFactory(state=PdfBundle.BundleChoice.ERROR)
    PdfBundleFactory(state=PdfBundle.BundleChoice.PROCESSING)
    bundle_ready = PdfBundleFactory(state=PdfBundle.BundleChoice.READY)

    ready_bundles = PdfBundle.objects.ready()

    assert len(ready_bundles) == 1
    assert ready_bundles[0] == bundle_ready
