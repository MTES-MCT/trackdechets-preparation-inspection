import factory

from .models import FeedbackResult


class FeedbackResultFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FeedbackResult

    content = factory.Sequence(lambda n: f"content {n}")
    author = factory.Sequence(lambda n: f"feedback{n}@test.fr")
