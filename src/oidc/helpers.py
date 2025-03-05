from django.conf import settings


def check_is_authenticated_from_oidc(request):
    session = request.session
    auth_user_backend = session.get("_auth_user_backend", None)
    return auth_user_backend in [settings.MONAIOT_BACKEND, settings.PROCONNECT_BACKEND]
