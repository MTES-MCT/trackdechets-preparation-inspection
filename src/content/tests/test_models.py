import pytest

from ..factories import FeedbackResultFactory

pytestmark = pytest.mark.django_db


def test_feedback_result_factory():
    feedback = FeedbackResultFactory()
    assert feedback.pk
    assert feedback.author
