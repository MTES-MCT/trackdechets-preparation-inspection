from django.urls import path

from .views import FeedbackDoneView, FeedbackView

urlpatterns = [
    path("feedback/", FeedbackView.as_view(), name="feedback_form"),
    path("feedback-done/", FeedbackDoneView.as_view(), name="feedback_done"),
]
