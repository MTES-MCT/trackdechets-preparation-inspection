from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
from django.shortcuts import resolve_url

redirect_url = "prepare"


class MonaiotAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        """
        Returns the default URL to redirect to after logging in.  Note
        that URLs passed explicitly (e.g. by passing along a `next`
        GET parameter) take precedence over the value returned here.
        """
        if not request.user.is_authenticated:
            raise Exception("Not authenticated")

        return resolve_url(redirect_url)

    def get_signup_redirect_url(self, request):
        return resolve_url("post_monaiot_signup")


class MonaiotSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """
        Invoked just after a user successfully authenticates via a
        social provider, but before the login is actually processed
        (and before the pre_social_login signal is emitted).

        You can use this hook to intervene, e.g. abort the login by
        raising an ImmediateHttpResponse

        Why both an adapter hook and the signal? Intervening in
        e.g. the flow from within a signal handler is bad -- multiple
        handlers may be active and are executed in undetermined order.
        """

        # social account already exists, so this is just a login
        if sociallogin.is_existing:
            return

        email = sociallogin.account.extra_data.get("email", None)
        # verify we have a verified email address
        if not email:
            return
        User = get_user_model()
        # check if given email address already exists as a verified email on
        # an existing user's account
        try:
            existing_user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            return

        # if it does, connect this new social login to the existing user
        sociallogin.connect(request, existing_user)
