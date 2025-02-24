import functools

from django.utils.functional import SimpleLazyObject

from .helpers import check_is_authenticated_from_monaiot


class MonaiotMiddleware:
    """
    This must be installed after
    :class:`~django.contrib.auth.middleware.AuthenticationMiddleware` and
    adds `is_authenticated_from_monaiot` to user instance.
    """

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, "user", None)
        if user is not None:
            request.user = SimpleLazyObject(functools.partial(self._verify_monaiot_user, request, user))

        return self.get_response(request)

    def _verify_monaiot_user(self, request, user):
        user.is_authenticated_from_monaiot = functools.partial(check_is_authenticated_from_monaiot, request)

        return user
