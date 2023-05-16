from django import template

register = template.Library()


@register.inclusion_tag("sheets/components/stats_graph.html")
def stats_graph(computed, bsd_type):
    if bsd_type == "bsdd":
        return computed.bsdd_stats_data
    if bsd_type == "bsdd_non_dangerous":
        return computed.bsdd_non_dangerous_stats_data
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


@register.inclusion_tag("sheets/components/bsd_canceled_table.html")
def render_bsd_canceled_table(computed, graph_context="web"):
    return {
        "bsd_canceled_data": computed.bsd_canceled_data,
        "company_siret": computed.org_id,
        "graph_context": graph_context,
    }


@register.inclusion_tag("sheets/components/same_emitter_recipient_table.html")
def render_same_emitter_recipient_table(computed, graph_context="web"):
    return {
        "same_emitter_recipient_data": computed.same_emitter_recipient_data,
        "graph_context": graph_context,
    }


@register.inclusion_tag("sheets/components/icpe.html")
def render_icpe(computed):
    return {
        "icpe_data": computed.icpe_data,
    }


@register.inclusion_tag("sheets/components/traceabilty_break.html")
def render_traceabilty_break(computed):
    return {
        "traceability_interruptions_data": computed.traceability_interruptions_data,
    }


@register.inclusion_tag("sheets/components/waste_is_dangerous_statements.html")
def render_waste_is_dangerous_statements(computed):
    return {
        "waste_is_dangerous_statements_data": computed.waste_is_dangerous_statements_data,
    }


@register.inclusion_tag("sheets/components/outliers.html")
def render_outliers(computed):
    return {
        "outliers_data": computed.outliers_data,
    }


@register.inclusion_tag("sheets/components/agreements.html")
def render_agreements(computed):
    return {
        "agreement_data": computed.agreement_data,
    }
