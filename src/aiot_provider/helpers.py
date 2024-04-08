PROVIDER_ID = "monaiot"
SOCIAL_ACCOUNT_KEY = "socialaccount"


def check_is_authenticated_from_monaiot(request):
    session = request.session
    auth_methods = session.get("account_authentication_methods", [])
    methods = [m.get("method", "") for m in auth_methods]

    providers = [m.get("provider", "") for m in auth_methods]

    return SOCIAL_ACCOUNT_KEY in methods and PROVIDER_ID in providers
