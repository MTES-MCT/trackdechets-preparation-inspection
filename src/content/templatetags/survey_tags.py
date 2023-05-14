from django import template

from content.models import FeedbackResult

register = template.Library()


@register.inclusion_tag("content/tags/survey_callout.html", takes_context=True)
def survey_callout(context):
    return {
        "display_survey": not FeedbackResult.objects.filter(
            author=context["request"].user.email
        ).exists()
    }
