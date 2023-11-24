from django import template

register = template.Library()


@register.inclusion_tag("sheets/components/stats_graph.html")
def stats_graph(computed, bsd_type):
    return_dict = {"bsd_type": bsd_type}
    if bsd_type == "bsdd":
        return_dict.update(computed.bsdd_stats_data)
    if bsd_type == "bsdd_non_dangerous":
        return_dict.update(computed.bsdd_non_dangerous_stats_data)
    if bsd_type == "bsda":
        return_dict.update(computed.bsda_stats_data)
    if bsd_type == "bsdasri":
        return_dict.update(computed.bsdasri_stats_data)
    if bsd_type == "bsff":
        return_dict.update(computed.bsff_stats_data)
    if bsd_type == "bsvhu":
        return_dict.update(computed.bsvhu_stats_data)

    return return_dict


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
def render_icpe(computed, graph_context="web"):
    return {
        "icpe_data": computed.icpe_data,
        "graph_context": graph_context,
    }


@register.inclusion_tag("sheets/components/traceabilty_break.html")
def render_traceabilty_break(computed, graph_context="web"):
    return {
        "traceability_interruptions_data": computed.traceability_interruptions_data,
        "graph_context": graph_context,
    }


@register.inclusion_tag("sheets/components/waste_is_dangerous_statements.html")
def render_waste_is_dangerous_statements(computed, graph_context="web"):
    return {
        "waste_is_dangerous_statements_data": computed.waste_is_dangerous_statements_data,
        "graph_context": graph_context,
    }


@register.inclusion_tag("sheets/components/private_individuals_collections_table.html")
def render_private_individuals_collections_table(computed, graph_context="web"):
    return {
        "private_individuals_collections_data": computed.private_individuals_collections_data,
        "company_siret": computed.org_id,
        "graph_context": graph_context,
    }


@register.inclusion_tag("sheets/components/quantity_outliers_table.html")
def render_quantity_outliers_table(computed, graph_context="web"):
    return {
        "quantity_outliers_data": computed.quantity_outliers_data,
        "company_siret": computed.org_id,
        "graph_context": graph_context,
    }


@register.inclusion_tag("sheets/components/outliers.html")
def render_outliers(computed):
    return {
        "outliers_data": computed.outliers_data,
    }


@register.inclusion_tag("sheets/components/bs_without_icpe_authorization_tables.html")
def render_bs_without_icpe_authorization_tables(computed, graph_context="web"):
    return {
        "bs_data_2760": computed.bs_processed_without_icpe_authorization.get("2760", None),
        "bs_data_2770": computed.bs_processed_without_icpe_authorization.get("2770", None),
        "bs_data_2718": computed.bs_processed_without_icpe_authorization.get("2718", None),
        "bs_data_2790": computed.bs_processed_without_icpe_authorization.get("2790", None),
        "graph_context": graph_context,
    }


@register.inclusion_tag("sheets/components/agreements.html")
def render_agreements(computed):
    return {
        "agreement_data": computed.agreement_data,
    }


@register.inclusion_tag("sheets/components/linked_companies.html")
def render_linked_companies_data(computed, graph_context="web"):
    return {
        "linked_companies_data": computed.linked_companies_data,
        "graph_context": graph_context,
    }


@register.inclusion_tag("sheets/components/bsda_worker_stats.html")
def render_bsda_worker_stats_data(computed, graph_context="web"):
    return {
        "bsda_worker_stats_data": computed.bsda_worker_stats_data,
        "graph_context": graph_context,
    }
