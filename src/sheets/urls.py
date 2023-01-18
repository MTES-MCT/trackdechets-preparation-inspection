from django.urls import path

from .views import (
    BaseView,
    SheetHtmlView,
    SheetPdfView,
    create_bar,
    create_graph,
    create_plot,
)

urlpatterns = [
    path("", BaseView.as_view(), name="base"),
    path("html/", SheetHtmlView.as_view()),
    path("pdf/", SheetPdfView.as_view()),
    path("img/", create_graph, name="create_graph"),
    path("bar/", create_bar, name="create_bar"),
    path("plot/", create_plot, name="create_plot"),
]
