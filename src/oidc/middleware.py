import functools

from django.utils.functional import SimpleLazyObject

from .helpers import check_is_authenticated_from_oidc


class OidcMiddleware:
    """
    This must be installed after
    :class:`~django.contrib.auth.middleware.AuthenticationMiddleware` and
    adds `is_authenticated_from_oidc` to user instance.
    """

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        user = getattr(request, "user", None)
        if user is not None:
            request.user = SimpleLazyObject(functools.partial(self._verify_oidc_user, request, user))

        return self.get_response(request)

    def _verify_oidc_user(self, request, user):
        user.is_authenticated_from_oidc = functools.partial(check_is_authenticated_from_oidc, request)

        return user
