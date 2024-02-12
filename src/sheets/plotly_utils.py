from base64 import b64encode

from plotly.io import from_json


def data_to_bs64_plot(json_plotly):
    """Takes a precomputed json from plotly and returns a base 64 png to embed in pdf."""
    if not json_plotly:
        return ""
    fig = from_json(json_plotly)
    return b64encode(fig.to_image(format="png", width=1280, height=720)).decode("ascii")
