from django.urls import path

from .views import FeedbackView, UserManual

urlpatterns = [
    path("feedback/", FeedbackView.as_view(), name="feedback_form"),
    path("user-manual/", UserManual.as_view(), name="user_manual"),
]
