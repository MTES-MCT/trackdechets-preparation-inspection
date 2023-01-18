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


class BaseView(TemplateView):
    template_name = "base.html"


class SheetHtmlView(LoginRequiredMixin, TemplateView):
    template_name = "sheets/pdf.html"


class SheetPdfView(WeasyTemplateResponseMixin, SheetHtmlView):
    pass


from django.shortcuts import render
from plotly.graph_objs import Scatter
from plotly.offline import plot


def create_plot(request):
    x_data = [0, 1, 2, 3]
    y_data = [x**2 for x in x_data]
    plot_div = plot(
        [
            Scatter(
                x=x_data,
                y=y_data,
                mode="lines",
                name="test",
                opacity=0.8,
                marker_color="green",
            )
        ],
        output_type="div",
        show_link=False,
        link_text="",
    )
    return render(request, "sheets/plot.html", context={"plot_div": plot_div})
