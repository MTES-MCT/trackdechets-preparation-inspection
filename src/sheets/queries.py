sql_bsdd_query_str = """
select
    id,
    bsdd.created_at,
    bsdd.sent_at,
    bsdd.received_at,
    bsdd.processed_at,
    bsdd.emitter_company_siret,
    bsdd.emitter_company_address,
    bsdd.recipient_company_siret,
    bsdd.waste_details_quantity,
    bsdd.quantity_received,
    bsdd.waste_details_code as waste_code,
    bsdd.processing_operation_done as processing_operation_code,
    bsdd.status,
    bsdd.transporter_transport_mode,
    bsdd.no_traceability,
    bsdd.waste_details_pop as waste_pop
 from
    trusted_zone_trackdechets.bsdd
where
    (emitter_company_siret = :siret
    or recipient_company_siret = :siret)
    and is_deleted = false
    and created_at >= current_date - INTERVAL '1 year'
    and status::text not in ('DRAFT', 'INITIAL', 'SIGNED_BY_WORKER')
order by
    created_at ASC;
"""

sql_company_query_str = """
select id,
    created_at,
    siret,
    name,
    address,
    company_types,
    transporter_receipt_id,
    trader_receipt_id,
    eco_organisme_agreements,
    broker_receipt_id,
    vhu_agrement_demolisseur_id,
    vhu_agrement_broyeur_id
from trusted_zone_trackdechets.company c
where c.siret = :siret
"""

sql_bsda_query_str = """
select
    id,
    created_at,
    transporter_transport_taken_over_at as sent_at,
    destination_reception_date as received_at,
    destination_operation_date as processed_at,
    emitter_company_siret,
    emitter_company_address,
    destination_company_siret as recipient_company_siret,
    weight_value as waste_details_quantity,
    destination_reception_weight/1000 as quantity_received,
    waste_code,
    destination_operation_code as processing_operation_code,
    status,
    transporter_transport_mode,
    waste_pop
from
    trusted_zone_trackdechets.bsda
where
    (emitter_company_siret = :siret
        or destination_company_siret = :siret)
    and is_deleted = false
    and created_at >= current_date - interval '1 year'
    and status::text not in ('DRAFT', 'INITIAL', 'SIGNED_BY_WORKER')
order by
    created_at asc"""

sql_bsdasri_query_str = """
select
   id,
    created_at,
    transporter_taken_over_at as sent_at,
    destination_reception_date as received_at,
    destination_operation_signature_date as processed_at,
    emitter_company_siret,
    emitter_company_address,
    destination_company_siret as recipient_company_siret,
    emitter_waste_weight_value as waste_details_quantity,
    destination_reception_waste_weight_value/1000 as quantity_received,
    waste_code,
    destination_operation_code as processing_operation_code,
    status,
    transporter_transport_mode
from
        trusted_zone_trackdechets.bsdasri
where
    (emitter_company_siret = :siret
        or destination_company_siret = :siret)
    and is_deleted = false
    and created_at >= current_date - interval '1 year'
    and status::text not in ('DRAFT', 'INITIAL', 'SIGNED_BY_WORKER')
order by
    created_at asc"""

sql_bsff_query_str = """select
    id,
    created_at,
    transporter_transport_taken_over_at as sent_at,
    destination_reception_date as received_at,
    destination_operation_signature_date as processed_at,
    emitter_company_siret,
    emitter_company_address,
    destination_company_siret as recipient_company_siret,
    weight_value as waste_detail_quantity,
    destination_reception_weight/1000 as quantity_received,
    waste_code,
    destination_operation_code as processing_operation_code,
    status,
    transporter_transport_mode
from
    trusted_zone_trackdechets.bsff
where
    (emitter_company_siret = :siret
        or destination_company_siret = :siret)
    and is_deleted = false
    and created_at >= current_date - interval '1 year'
    and status::text not in ('DRAFT', 'INITIAL', 'SIGNED_BY_WORKER')
order by
    created_at asc"""

sql_bsvhu_query_str = """
select
    id,
    created_at,
    transporter_transport_taken_over_at as sent_at,
    destination_reception_date as received_at,
    destination_operation_signature_date as processed_at,
    emitter_company_siret,
    emitter_company_address,
    destination_company_siret as recipient_company_siret,
    weight_value as waste_detail_quantity,
    destination_reception_weight/1000 as quantity_received,
    waste_code,
    destination_operation_code as processing_operation_code,
    status
from
    trusted_zone_trackdechets.bsvhu
where
    (emitter_company_siret = :siret
        or destination_company_siret = :siret)
    and is_deleted = false
    and created_at >= current_date - interval '1 year'
    and  status::text not in ('DRAFT', 'INITIAL', 'SIGNED_BY_WORKER')
order by
    created_at asc
"""

sql_revised_bsdd_query_str = """
select id,
    bsdd_id as bs_id,
    created_at
from trusted_zone_trackdechets.bsdd_revision_request
where authoring_company_id = :company_id
    and status='ACCEPTED'
    and created_at >= current_date - INTERVAL '1 year'
"""

sql_revised_bsda_query_str = """
select id,
    bsda_id as bs_id,
    created_at
from trusted_zone_trackdechets.bsda_revision_request
where authoring_company_id = :company_id
    and status='ACCEPTED'
    and created_at >= current_date - INTERVAL '1 year'
"""


sql_get_icpe_data = """
select
    code_s3ic,
    id_nomenclature,
    date_debut_exploitation,
    date_fin_validite,
    volume,
    unite,
    rubrique,
    alinea,
    libelle_court_activite
from
    refined_zone_icpe.icpe_siretise
where siret_clean = :siret
AND en_vigueur
and id_regime in ('E','DC','D','A')
"""

sql_get_trader_receipt_id_data = """
SELECT id,
    receipt_number,
    validity_limit
FROM trusted_zone_trackdechets.trader_receipt
WHERE id = :id
"""

sql_get_transporter_receipt_id_data_str = """
SELECT id,
    receipt_number,
    validity_limit,
    department
FROM trusted_zone_trackdechets.transporter_receipt
WHERE id = :id
"""

sql_get_broker_receipt_id_data = """
SELECT id,
    receipt_number,
    validity_limit,
    department
FROM trusted_zone_trackdechets.broker_receipt
where id = :id
"""


sql_get_vhu_agrement_data = """
SELECT
    id,
    agrement_number AS receipt_number,
    department
FROM
    trusted_zone_trackdechets.vhu_agrement
WHERE
    id = :id
"""
