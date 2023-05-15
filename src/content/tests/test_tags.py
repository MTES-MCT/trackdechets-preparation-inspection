import pytest
from django.template import Context, Template
from django.test import RequestFactory

from accounts.factories import UserFactory
from content.factories import FeedbackResultFactory

pytestmark = pytest.mark.django_db


def test_survey_callout_tag_displays_callout():
    t = Template("{% load survey_tags %}{% survey_callout %}")
    factory = RequestFactory()
    request = factory.get("/")

    FeedbackResultFactory(author="somebody@gouv.fr")
    request.user = UserFactory(email="somebodyelse@gouv.fr")
    c = Context({"request": request})
    res = t.render(c)
    assert "Aidez-nous à améliorer cet outil" in res


def test_survey_callout_tag_does_not_display_callout():
    t = Template("{% load survey_tags %}{% survey_callout %}")
    factory = RequestFactory()
    request = factory.get("/")

    FeedbackResultFactory(author="somebody@gouv.fr")
    request.user = UserFactory(email="somebody@gouv.fr")
    c = Context({"request": request})
    res = t.render(c)
    assert "Aidez-nous à améliorer cet outil" not in res
