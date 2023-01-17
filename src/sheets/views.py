import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from braces.views import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView
from django_weasyprint import WeasyTemplateResponseMixin


def create_bar(request):
    wide_df = px.data.medals_wide()

    fig = px.bar(
        wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input"
    )
    img_bytes = fig.to_image(format="png")

    return HttpResponse(img_bytes, content_type="image/png")


def create_graph(request):
    N = 100
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    sz = np.random.rand(N) * 30

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="markers",
            marker=go.scatter.Marker(
                size=sz, color=colors, opacity=0.6, colorscale="Viridis"
            ),
        )
    )

    img_bytes = fig.to_image(format="png")

    return HttpResponse(img_bytes, content_type="image/png")


class SheetHtmlView(LoginRequiredMixin, TemplateView):
    template_name = "sheets/pdf.html"


class SheetPdfView(WeasyTemplateResponseMixin, SheetHtmlView):
    pass
