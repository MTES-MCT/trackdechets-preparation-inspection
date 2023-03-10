from django import template

register = template.Library()


@register.inclusion_tag("sheets/components/stats_graph.html")
def stats_graph(computed, bsd_type):
    if bsd_type == "bsdd":
        return computed.bsdd_stats_data
    if bsd_type == "bsda":
        return computed.bsda_stats_data
    if bsd_type == "bsdasri":
        return computed.bsdasri_stats_data
    if bsd_type == "bsff":
        return computed.bsff_stats_data
    if bsd_type == "bsvhu":
        return computed.bsvhu_stats_data


@register.inclusion_tag("sheets/components/in_out_table.html")
def render_in_out_table(computed, graph_context="web"):
    return {
        "input_output_waste_data": computed.input_output_waste_data,
        "graph_context": graph_context,
    }


@register.inclusion_tag("sheets/components/icpe.html")
def render_icpe(computed):
    return {
        "icpe_data": computed.icpe_data,
    }
