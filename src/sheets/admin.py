from django.contrib import admin
from django.urls import reverse_lazy
from django.utils.html import format_html

from .models import ComputedInspectionData, RegistryDownload


@admin.register(ComputedInspectionData)
class ComputedInspectionDataAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "org_id",
        "created",
        "get_render",
        "state",
        "data_start_date",
        "data_end_date",
        "creation_mode",
        "created_by",
        "processing_duration",
        "pdf_rendering_duration",
    ]
    list_filter = ["created", "creation_mode"]
    search_fields = ["org_id"]

    def get_queryset(self, request):
        # Don't load heavy unused fields
        return (
            super()
            .get_queryset(request)
            .defer(
                "bsdd_created_rectified_data",
                "bsdd_stock_data",
                "bsdd_stats_data",
                "bsdd_non_dangerous_created_rectified_data",
                "bsdd_non_dangerous_stock_data",
                "bsdd_non_dangerous_stats_data",
                "bsda_created_rectified_data",
                "bsda_stock_data",
                "bsda_stats_data",
                "bsdasri_created_rectified_data",
                "bsdasri_stock_data",
                "bsdasri_stats_data",
                "bsff_created_rectified_data",
                "bsff_stock_data",
                "bsff_stats_data",
                "bsvhu_created_rectified_data",
                "bsvhu_stock_data",
                "bsvhu_stats_data",
                "all_bsd_data_empty",
                "storage_data",
                "waste_origin_data",
                "waste_origin_map_data",
                "waste_flows_data",
                "icpe_data",
                "agreement_data",
                "traceability_interruptions_data",
                "waste_is_dangerous_statements_data",
                "bsd_canceled_data",
                "same_emitter_recipient_data",
                "private_individuals_collections_data",
                "quantity_outliers_data",
                "bsdd_created_rectified_graph",
                "bsdd_stock_graph",
                "bsdd_non_dangerous_created_rectified_graph",
                "bsdd_non_dangerous_stock_graph",
                "bsda_created_rectified_graph",
                "bsda_stock_graph",
                "bsdasri_created_rectified_graph",
                "bsdasri_stock_graph",
                "bsff_created_rectified_graph",
                "bsff_stock_graph",
                "bsvhu_created_rectified_graph",
                "bsvhu_stock_graph",
                "waste_origin_graph",
                "waste_origin_map_graph",
                "icpe_2770_data",
                "icpe_2770_graph",
                "icpe_2790_data",
                "icpe_2790_graph",
                "icpe_2760_1_data",
                "icpe_2760_1_graph",
                "icpe_2771_data",
                "icpe_2771_graph",
                "icpe_2791_data",
                "icpe_2791_graph",
                "icpe_2760_2_data",
                "icpe_2760_2_graph",
                "bs_processed_without_icpe_authorization",
                "bsda_worker_stats_data",
                "bsda_worker_quantity_data",
                "bsda_worker_quantity_graph",
                "transporter_bordereaux_stats_graph_data",
                "transporter_bordereaux_stats_graph",
                "quantities_transported_stats_graph_data",
                "quantities_transported_stats_graph",
                "transporter_bordereaux_stats_data",
                "followed_with_pnttd_data",
                "gistrid_stats_data",
                "non_dangerous_waste_quantities_graph_data",
                "non_dangerous_waste_quantities_graph",
                "non_dangerous_waste_statements_graph_data",
                "non_dangerous_waste_statements_graph",
                "non_dangerous_waste_stats_data",
                "pdf",
            )
        )

    def get_render(self, obj):
        if obj.state in [
            ComputedInspectionData.StateChoice.INITIAL,
            ComputedInspectionData.StateChoice.COMPUTED_FAILED,
        ]:
            return None
        url = reverse_lazy("sheet", args=[obj.pk])
        return format_html("<a href='{}' _target='blank'>Voir</a>", url)

    get_render.short_description = "Rendu"


@admin.register(RegistryDownload)
class RegistryDownloadAdmin(admin.ModelAdmin):
    list_display = ["id", "org_id", "created", "created_by"]
    list_filter = ["created"]
    search_fields = ["org_id"]
