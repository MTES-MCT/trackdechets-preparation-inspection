from django.conf import settings


def check_is_authenticated_from_monaiot(request):
    session = request.session

    return session.get("_auth_user_backend", None) == settings.MONAIOT_BACKEND
