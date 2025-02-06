from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.views.generic import FormView

from common.mixins import FullyLoggedMixin

from .forms import FeedbackForm
from .models import FeedbackResult

subject = "Un utilisateur a rempli un formulaire de feedback"


class FeedbackView(FullyLoggedMixin, SuccessMessageMixin, FormView):
    template_name = "content/feedback.html"
    form_class = FeedbackForm
    success_url = reverse_lazy("private_home")
    success_message = "Merci, vos réponses ont été enregistrées et nous aideront à améliorer cet outil "
    allowed_user_categories = ["*"]

    def form_valid(self, form):
        res = super().form_valid(form)
        content = form.to_content()
        FeedbackResult.objects.create(content=content, author=self.request.user.email)
        self.notify_admins(content)
        return res

    def notify_admins(self, body):
        body = f"Un utilisateur a rempli un formulaire\n\nUtilisateur: {self.request.user.email}\n\n{body}"
        message = EmailMessage(
            subject=subject,
            body=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=settings.MESSAGE_RECIPIENTS,
        )
        message.send()
