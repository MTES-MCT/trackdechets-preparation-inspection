from allauth.socialaccount.forms import SignupForm


class MonAiotSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].disabled = True
        self.fields["email"].disabled = True
