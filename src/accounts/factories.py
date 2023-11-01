import factory
from django_otp.plugins.otp_email.models import EmailDevice

from .models import User

DEFAULT_PASSWORD = "passpass"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: f"email_{n}@trackdechets.test")
    username = factory.Faker("first_name")
    password = factory.PostGenerationMethodCall("set_password", DEFAULT_PASSWORD)


class EmailDeviceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmailDevice

    email = factory.Sequence(lambda n: f"email_{n}@trackdechets.test")
    user = factory.SubFactory(UserFactory)
