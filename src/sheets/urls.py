from django.urls import path

from .views import SheetHtmlView, SheetPdfView, create_bar, create_graph

urlpatterns = [
    path("html/", SheetHtmlView.as_view()),
    path("pdf/", SheetPdfView.as_view()),
    path("img/", create_graph, name="create_graph"),
    path("bar/", create_bar, name="create_bar"),
]
