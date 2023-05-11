from braces.views import LoginRequiredMixin
from django.conf import settings
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import FeedbackForm
from .models import FeedbackResult

subject = "Un utilisateur a rempli un formulaire de feedback"


class FeedbackView(LoginRequiredMixin, FormView):
    template_name = "content/feedback.html"
    form_class = FeedbackForm
    success_url = reverse_lazy("feedback_done")

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


class FeedbackDoneView(LoginRequiredMixin, TemplateView):
    template_name = "content/feedback_done.html"
