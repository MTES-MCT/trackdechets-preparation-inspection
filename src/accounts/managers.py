from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    use_for_related_fields = True

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        """Creates a superuser with the given email and password."""
        now = timezone.now()
        if not email:
            raise ValueError("The email is a required field and cannot be empty")
        if not username:
            raise ValueError("You cannot create users with no username")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            is_active=True,
            is_staff=True,
            is_superuser=True,
            date_joined=now,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, email):
        lookup = "{}__iexact".format(self.model.USERNAME_FIELD)
        return self.get(**{lookup: email})
