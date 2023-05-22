--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: dbt_test__audit; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA dbt_test__audit;


ALTER SCHEMA dbt_test__audit OWNER TO pao;

--
-- Name: elementary; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA elementary;


ALTER SCHEMA elementary OWNER TO pao;

--
-- Name: raw_zone; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA raw_zone;


ALTER SCHEMA raw_zone OWNER TO pao;

--
-- Name: raw_zone_gsheet; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA raw_zone_gsheet;


ALTER SCHEMA raw_zone_gsheet OWNER TO pao;

--
-- Name: raw_zone_icpe; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA raw_zone_icpe;


ALTER SCHEMA raw_zone_icpe OWNER TO pao;

--
-- Name: raw_zone_insee; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA raw_zone_insee;


ALTER SCHEMA raw_zone_insee OWNER TO pao;

--
-- Name: raw_zone_trackdechets; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA raw_zone_trackdechets;


ALTER SCHEMA raw_zone_trackdechets OWNER TO pao;

--
-- Name: raw_zone_zammad; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA raw_zone_zammad;


ALTER SCHEMA raw_zone_zammad OWNER TO pao;

--
-- Name: re; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA re;


ALTER SCHEMA re OWNER TO pao;

--
-- Name: re_internal; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA re_internal;


ALTER SCHEMA re_internal OWNER TO pao;

--
-- Name: refined_zone; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA refined_zone;


ALTER SCHEMA refined_zone OWNER TO pao;

--
-- Name: refined_zone_analytics; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA refined_zone_analytics;


ALTER SCHEMA refined_zone_analytics OWNER TO pao;

--
-- Name: refined_zone_enriched; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA refined_zone_enriched;


ALTER SCHEMA refined_zone_enriched OWNER TO pao;

--
-- Name: refined_zone_icpe; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA refined_zone_icpe;


ALTER SCHEMA refined_zone_icpe OWNER TO pao;

--
-- Name: refined_zone_stats_publiques; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA refined_zone_stats_publiques;


ALTER SCHEMA refined_zone_stats_publiques OWNER TO pao;

--
-- Name: trusted_zone; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA trusted_zone;


ALTER SCHEMA trusted_zone OWNER TO pao;

--
-- Name: trusted_zone_gsheet; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA trusted_zone_gsheet;


ALTER SCHEMA trusted_zone_gsheet OWNER TO pao;

--
-- Name: trusted_zone_icpe; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA trusted_zone_icpe;


ALTER SCHEMA trusted_zone_icpe OWNER TO pao;

--
-- Name: trusted_zone_insee; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA trusted_zone_insee;


ALTER SCHEMA trusted_zone_insee OWNER TO pao;

--
-- Name: trusted_zone_trackdechets; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA trusted_zone_trackdechets;


ALTER SCHEMA trusted_zone_trackdechets OWNER TO pao;

--
-- Name: trusted_zone_zammad; Type: SCHEMA; Schema: -; Owner: pao
--

CREATE SCHEMA trusted_zone_zammad;


ALTER SCHEMA trusted_zone_zammad OWNER TO pao;

--
-- Name: pg_stat_statements; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pg_stat_statements WITH SCHEMA public;


--
-- Name: EXTENSION pg_stat_statements; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_stat_statements IS 'track planning and execution statistics of all SQL statements executed';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: accepted_values_bsdd_36c9fc6f86a2ed9126bf2ac22f12ac35; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.accepted_values_bsdd_36c9fc6f86a2ed9126bf2ac22f12ac35 (
    value_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.accepted_values_bsdd_36c9fc6f86a2ed9126bf2ac22f12ac35 OWNER TO pao;

--
-- Name: accepted_values_bsdd_4c0d5af17d2d3ceb8285a9219fe4278f; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.accepted_values_bsdd_4c0d5af17d2d3ceb8285a9219fe4278f (
    value_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.accepted_values_bsdd_4c0d5af17d2d3ceb8285a9219fe4278f OWNER TO pao;

--
-- Name: accepted_values_bsdd_9dd4a471ccda82a9dc9992185e5cbb7e; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.accepted_values_bsdd_9dd4a471ccda82a9dc9992185e5cbb7e (
    value_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.accepted_values_bsdd_9dd4a471ccda82a9dc9992185e5cbb7e OWNER TO pao;

--
-- Name: accepted_values_bsdd_eb37a8ac37e4a84e927dcc2951fcb3be; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.accepted_values_bsdd_eb37a8ac37e4a84e927dcc2951fcb3be (
    value_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.accepted_values_bsdd_eb37a8ac37e4a84e927dcc2951fcb3be OWNER TO pao;

--
-- Name: accepted_values_bsdd_quantity_received_type__REAL__ESTIMATED; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit."accepted_values_bsdd_quantity_received_type__REAL__ESTIMATED" (
    value_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit."accepted_values_bsdd_quantity_received_type__REAL__ESTIMATED" OWNER TO pao;

--
-- Name: dbt_utils_accepted_range_bsdd_waste_details_quantity__False__0; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit."dbt_utils_accepted_range_bsdd_waste_details_quantity__False__0" (
    id character varying,
    custom_id character varying,
    readable_id character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    status character varying,
    is_deleted boolean,
    owner_id character varying,
    waste_details_code character varying,
    waste_details_name character varying,
    waste_details_pop boolean,
    waste_details_is_dangerous boolean,
    waste_details_onu_code character varying,
    waste_details_quantity double precision,
    waste_details_quantity_type character varying,
    waste_details_consistence character varying,
    waste_details_packaging_infos jsonb,
    waste_details_analysis_references jsonb,
    waste_details_land_identifiers jsonb,
    waste_details_parcel_numbers jsonb,
    waste_acceptation_status character varying,
    waste_refusal_reason character varying,
    emitter_company_siret character varying,
    emitter_company_name character varying,
    emitter_type character varying,
    emitter_company_address character varying,
    emitter_company_contact character varying,
    emitter_company_mail character varying,
    emitter_company_phone character varying,
    emitter_is_foreignship boolean,
    emitter_company_omi_number character varying,
    emitter_is_private_individual boolean,
    emitter_pickup_site character varying,
    emitter_worksite_name character varying,
    emitter_worksite_address character varying,
    emitter_worksite_postal_code character varying,
    emitter_worksite_city character varying,
    emitter_worksite_infos character varying,
    emitted_by_eco_organisme boolean,
    emitted_at timestamp without time zone,
    emitted_by character varying,
    signed_at timestamp without time zone,
    signed_by character varying,
    signed_by_transporter boolean,
    taken_over_at timestamp without time zone,
    taken_over_by character varying,
    transporter_company_siret character varying,
    transporter_company_name character varying,
    transporter_company_address character varying,
    transporter_department character varying,
    transporter_company_contact character varying,
    transporter_company_mail character varying,
    transporter_company_phone character varying,
    transporter_number_plate character varying,
    transporter_receipt character varying,
    transporter_validity_limit timestamp without time zone,
    transporter_transport_mode character varying,
    transporter_company_vat_number character varying,
    transporter_custom_info character varying,
    transporter_is_exempted_of_receipt boolean,
    current_transporter_siret character varying,
    sent_at timestamp without time zone,
    sent_by character varying,
    next_transporter_siret character varying,
    recipient_company_siret character varying,
    recipient_company_name character varying,
    recipient_company_address character varying,
    recipient_company_contact character varying,
    recipient_company_mail character varying,
    recipient_company_phone character varying,
    recipient_is_temp_storage boolean,
    recipient_processing_operation character varying,
    recipient_cap character varying,
    received_at timestamp without time zone,
    received_by character varying,
    processed_at timestamp without time zone,
    processed_by character varying,
    quantity_received double precision,
    quantity_received_type character varying,
    processing_operation_done character varying,
    processing_operation_description character varying,
    no_traceability boolean,
    is_accepted boolean,
    next_destination_company_siret character varying,
    next_destination_company_name character varying,
    next_destination_company_address character varying,
    next_destination_company_country character varying,
    next_destination_company_contact character varying,
    next_destination_company_mail character varying,
    next_destination_company_phone character varying,
    next_destination_company_vat_number character varying,
    next_destination_processing_operation character varying,
    broker_company_siret character varying,
    broker_company_name character varying,
    broker_company_address character varying,
    broker_department character varying,
    broker_company_contact character varying,
    broker_company_mail character varying,
    broker_company_phone character varying,
    broker_receipt character varying,
    broker_validity_limit timestamp without time zone,
    trader_company_siret character varying,
    trader_company_name character varying,
    trader_company_address character varying,
    trader_department character varying,
    trader_company_contact character varying,
    trader_company_mail character varying,
    trader_company_phone character varying,
    trader_receipt character varying,
    trader_validity_limit timestamp without time zone,
    eco_organisme_siret character varying,
    eco_organisme_name character varying,
    is_imported_from_paper boolean,
    forwarded_in_id character varying
);


ALTER TABLE dbt_test__audit."dbt_utils_accepted_range_bsdd_waste_details_quantity__False__0" OWNER TO pao;

--
-- Name: dbt_utils_accepted_range_bsdd_waste_details_quantity__True__0; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit."dbt_utils_accepted_range_bsdd_waste_details_quantity__True__0" (
    id character varying,
    custom_id character varying,
    readable_id character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    status character varying,
    is_deleted boolean,
    owner_id character varying,
    waste_details_code character varying,
    waste_details_name character varying,
    waste_details_pop boolean,
    waste_details_is_dangerous boolean,
    waste_details_onu_code character varying,
    waste_details_quantity double precision,
    waste_details_quantity_type character varying,
    waste_details_consistence character varying,
    waste_details_packaging_infos jsonb,
    waste_details_analysis_references jsonb,
    waste_details_land_identifiers jsonb,
    waste_details_parcel_numbers jsonb,
    waste_acceptation_status character varying,
    waste_refusal_reason character varying,
    emitter_company_siret character varying,
    emitter_company_name character varying,
    emitter_type character varying,
    emitter_company_address character varying,
    emitter_company_contact character varying,
    emitter_company_mail character varying,
    emitter_company_phone character varying,
    emitter_is_foreignship boolean,
    emitter_company_omi_number character varying,
    emitter_is_private_individual boolean,
    emitter_pickup_site character varying,
    emitter_worksite_name character varying,
    emitter_worksite_address character varying,
    emitter_worksite_postal_code character varying,
    emitter_worksite_city character varying,
    emitter_worksite_infos character varying,
    emitted_by_eco_organisme boolean,
    emitted_at timestamp without time zone,
    emitted_by character varying,
    signed_at timestamp without time zone,
    signed_by character varying,
    signed_by_transporter boolean,
    sent_at timestamp without time zone,
    sent_by character varying,
    transporter_company_siret character varying,
    transporter_company_name character varying,
    transporter_company_address character varying,
    transporter_department character varying,
    transporter_company_contact character varying,
    transporter_company_mail character varying,
    transporter_company_phone character varying,
    transporter_number_plate character varying,
    transporter_receipt character varying,
    transporter_validity_limit timestamp without time zone,
    transporter_transport_mode character varying,
    transporter_company_vat_number character varying,
    transporter_custom_info character varying,
    transporter_is_exempted_of_receipt boolean,
    current_transporter_siret character varying,
    next_transporter_siret character varying,
    taken_over_at timestamp without time zone,
    taken_over_by character varying,
    recipient_company_siret character varying,
    recipient_company_name character varying,
    recipient_company_address character varying,
    recipient_company_contact character varying,
    recipient_company_mail character varying,
    recipient_company_phone character varying,
    recipient_is_temp_storage boolean,
    recipient_cap character varying,
    received_at timestamp without time zone,
    received_by character varying,
    processed_at timestamp without time zone,
    processed_by character varying,
    quantity_received double precision,
    quantity_received_type character varying,
    processing_operation_description character varying,
    no_traceability boolean,
    is_accepted boolean,
    next_destination_company_siret character varying,
    next_destination_company_name character varying,
    next_destination_company_address character varying,
    next_destination_company_country character varying,
    next_destination_company_contact character varying,
    next_destination_company_mail character varying,
    next_destination_company_phone character varying,
    next_destination_company_vat_number character varying,
    next_destination_processing_operation character varying,
    broker_company_siret character varying,
    broker_company_name character varying,
    broker_company_address character varying,
    broker_department character varying,
    broker_company_contact character varying,
    broker_company_mail character varying,
    broker_company_phone character varying,
    broker_receipt character varying,
    broker_validity_limit timestamp without time zone,
    trader_company_siret character varying,
    trader_company_name character varying,
    trader_company_address character varying,
    trader_department character varying,
    trader_company_contact character varying,
    trader_company_mail character varying,
    trader_company_phone character varying,
    trader_receipt character varying,
    trader_validity_limit timestamp without time zone,
    eco_organisme_siret character varying,
    eco_organisme_name character varying,
    is_imported_from_paper boolean,
    forwarded_in_id character varying,
    recipient_processing_operation text,
    processing_operation_done text
);


ALTER TABLE dbt_test__audit."dbt_utils_accepted_range_bsdd_waste_details_quantity__True__0" OWNER TO pao;

--
-- Name: dbt_utils_relationships_where__1a13549bffe2a11743f077531667d7ec; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.dbt_utils_relationships_where__1a13549bffe2a11743f077531667d7ec (
    id character varying,
    right_id character varying
);


ALTER TABLE dbt_test__audit.dbt_utils_relationships_where__1a13549bffe2a11743f077531667d7ec OWNER TO pao;

--
-- Name: dbt_utils_relationships_where__e333998fdbcefbf261b5c1696489382a; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.dbt_utils_relationships_where__e333998fdbcefbf261b5c1696489382a (
    id character varying,
    right_id character varying
);


ALTER TABLE dbt_test__audit.dbt_utils_relationships_where__e333998fdbcefbf261b5c1696489382a OWNER TO pao;

--
-- Name: elementary_column_anomalies_bsdd_max_length__readable_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_column_anomalies_bsdd_max_length__readable_id (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_column_anomalies_bsdd_max_length__readable_id OWNER TO pao;

--
-- Name: elementary_dimension_anomalies_bsda_status; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_dimension_anomalies_bsda_status (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying,
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_dimension_anomalies_bsda_status OWNER TO pao;

--
-- Name: elementary_dimension_anomalies_bsdasri_status; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_dimension_anomalies_bsdasri_status (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying,
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_dimension_anomalies_bsdasri_status OWNER TO pao;

--
-- Name: elementary_dimension_anomalies_bsdd_status; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_dimension_anomalies_bsdd_status (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying,
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_dimension_anomalies_bsdd_status OWNER TO pao;

--
-- Name: elementary_schema_changes_bsda_; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_schema_changes_bsda_ (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_schema_changes_bsda_ OWNER TO pao;

--
-- Name: elementary_schema_changes_bsdasri_; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_schema_changes_bsdasri_ (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_schema_changes_bsdasri_ OWNER TO pao;

--
-- Name: elementary_schema_changes_bsdd_; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_schema_changes_bsdd_ (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_schema_changes_bsdd_ OWNER TO pao;

--
-- Name: elementary_schema_changes_from_baseline_bsda_; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_schema_changes_from_baseline_bsda_ (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_schema_changes_from_baseline_bsda_ OWNER TO pao;

--
-- Name: elementary_schema_changes_from_baseline_bsdasri_; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_schema_changes_from_baseline_bsdasri_ (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_schema_changes_from_baseline_bsdasri_ OWNER TO pao;

--
-- Name: elementary_schema_changes_from_baseline_bsdd_; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_schema_changes_from_baseline_bsdd_ (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_schema_changes_from_baseline_bsdd_ OWNER TO pao;

--
-- Name: elementary_source_schema_chang_00f8379eb83555d423e3c7ea22fc212b; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_00f8379eb83555d423e3c7ea22fc212b (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_00f8379eb83555d423e3c7ea22fc212b OWNER TO pao;

--
-- Name: elementary_source_schema_chang_0228df0a3d48055b4993b81d3d7505dd; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_0228df0a3d48055b4993b81d3d7505dd (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_0228df0a3d48055b4993b81d3d7505dd OWNER TO pao;

--
-- Name: elementary_source_schema_chang_0a1be69cb798442f9b6932ebdb6497c7; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_0a1be69cb798442f9b6932ebdb6497c7 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_0a1be69cb798442f9b6932ebdb6497c7 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_10281038073a6eb16c37f76550f7fd30; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_10281038073a6eb16c37f76550f7fd30 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_10281038073a6eb16c37f76550f7fd30 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_10795bf8112706b32e23efb588bc34de; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_10795bf8112706b32e23efb588bc34de (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_10795bf8112706b32e23efb588bc34de OWNER TO pao;

--
-- Name: elementary_source_schema_chang_113952ab7db142948da0062e899ec753; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_113952ab7db142948da0062e899ec753 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_113952ab7db142948da0062e899ec753 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_13248cb4c3aeb0bfccce8ae573e5abc1; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_13248cb4c3aeb0bfccce8ae573e5abc1 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_13248cb4c3aeb0bfccce8ae573e5abc1 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_17cb2509082eccd5bddcdd4d61e9a66c; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_17cb2509082eccd5bddcdd4d61e9a66c (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_17cb2509082eccd5bddcdd4d61e9a66c OWNER TO pao;

--
-- Name: elementary_source_schema_chang_291c5ea7bfc319abb32aa64133c1c200; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_291c5ea7bfc319abb32aa64133c1c200 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_291c5ea7bfc319abb32aa64133c1c200 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_317d6a7a28b8649a24f15bfe6c9da262; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_317d6a7a28b8649a24f15bfe6c9da262 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_317d6a7a28b8649a24f15bfe6c9da262 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_34afd93dd6bd31e227f68e8f28d0ba6e; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_34afd93dd6bd31e227f68e8f28d0ba6e (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_34afd93dd6bd31e227f68e8f28d0ba6e OWNER TO pao;

--
-- Name: elementary_source_schema_chang_388d9c3229c3a804c34eb0fd52e2eab8; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_388d9c3229c3a804c34eb0fd52e2eab8 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_388d9c3229c3a804c34eb0fd52e2eab8 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_3f46066d6ac0a223d990dd5f48586661; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_3f46066d6ac0a223d990dd5f48586661 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_3f46066d6ac0a223d990dd5f48586661 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_6dbae9749c4bc2fc18b371e351b85353; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_6dbae9749c4bc2fc18b371e351b85353 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_6dbae9749c4bc2fc18b371e351b85353 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_6df2d5cb36919af48a80b19a91e1614f; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_6df2d5cb36919af48a80b19a91e1614f (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_6df2d5cb36919af48a80b19a91e1614f OWNER TO pao;

--
-- Name: elementary_source_schema_chang_6f6e988e9e757968932f0a76fbcbc06d; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_6f6e988e9e757968932f0a76fbcbc06d (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_6f6e988e9e757968932f0a76fbcbc06d OWNER TO pao;

--
-- Name: elementary_source_schema_chang_7a62bc975e34c60f2fc52b5b93c9de52; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_7a62bc975e34c60f2fc52b5b93c9de52 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_7a62bc975e34c60f2fc52b5b93c9de52 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_8487b0c2c7b56dc83ec8d6239b23e928; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_8487b0c2c7b56dc83ec8d6239b23e928 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_8487b0c2c7b56dc83ec8d6239b23e928 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_883b064ab76ae9efbcb762eb14ca2ceb; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_883b064ab76ae9efbcb762eb14ca2ceb (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_883b064ab76ae9efbcb762eb14ca2ceb OWNER TO pao;

--
-- Name: elementary_source_schema_chang_8e0dfb522135d889d0e5f3bdd1eb11af; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_8e0dfb522135d889d0e5f3bdd1eb11af (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_8e0dfb522135d889d0e5f3bdd1eb11af OWNER TO pao;

--
-- Name: elementary_source_schema_chang_921a2c7ef03720ee86f186a805e77bd0; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_921a2c7ef03720ee86f186a805e77bd0 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_921a2c7ef03720ee86f186a805e77bd0 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_a1754a62304166d2bea8a3b006a62819; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_a1754a62304166d2bea8a3b006a62819 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_a1754a62304166d2bea8a3b006a62819 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_a40be0dac4f44716523e68ffa143b2e0; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_a40be0dac4f44716523e68ffa143b2e0 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_a40be0dac4f44716523e68ffa143b2e0 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_a670eda47e275a2d213dec263569cbbb; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_a670eda47e275a2d213dec263569cbbb (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_a670eda47e275a2d213dec263569cbbb OWNER TO pao;

--
-- Name: elementary_source_schema_chang_bd3ae06fcd4a349e6953c382eeb7ef9b; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_bd3ae06fcd4a349e6953c382eeb7ef9b (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_bd3ae06fcd4a349e6953c382eeb7ef9b OWNER TO pao;

--
-- Name: elementary_source_schema_chang_c433d8ecbc64c5e8e979295712649248; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_c433d8ecbc64c5e8e979295712649248 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_c433d8ecbc64c5e8e979295712649248 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_d0ddeafc86328b0983cf8e9afbefd0fb; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_d0ddeafc86328b0983cf8e9afbefd0fb (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_d0ddeafc86328b0983cf8e9afbefd0fb OWNER TO pao;

--
-- Name: elementary_source_schema_chang_d6e06b32220dd00a29e8c619eda96c56; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_d6e06b32220dd00a29e8c619eda96c56 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_d6e06b32220dd00a29e8c619eda96c56 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_dcf37b3bb45ec5e5e5eeb915f3858a76; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_dcf37b3bb45ec5e5e5eeb915f3858a76 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_dcf37b3bb45ec5e5e5eeb915f3858a76 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_e0f3e11fe4f8b18414a8f3c34f2a6018; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_e0f3e11fe4f8b18414a8f3c34f2a6018 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_e0f3e11fe4f8b18414a8f3c34f2a6018 OWNER TO pao;

--
-- Name: elementary_source_schema_chang_e94232a409c5d8c3dfdd2eb057b9192c; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_e94232a409c5d8c3dfdd2eb057b9192c (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_e94232a409c5d8c3dfdd2eb057b9192c OWNER TO pao;

--
-- Name: elementary_source_schema_chang_f5dade6df32e7eeaa3242d0c506eba88; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_schema_chang_f5dade6df32e7eeaa3242d0c506eba88 (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name text COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE dbt_test__audit.elementary_source_schema_chang_f5dade6df32e7eeaa3242d0c506eba88 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_0089482117bb32ba0a31786088d4b4e9; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_0089482117bb32ba0a31786088d4b4e9 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_0089482117bb32ba0a31786088d4b4e9 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_009ef35f9fadd27a8f6d51fef028599c; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_009ef35f9fadd27a8f6d51fef028599c (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_009ef35f9fadd27a8f6d51fef028599c OWNER TO pao;

--
-- Name: elementary_source_table_anomal_0894205a57b4b176db6f191d5cb0df32; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_0894205a57b4b176db6f191d5cb0df32 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_0894205a57b4b176db6f191d5cb0df32 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_1d367b7320fbcf4ee75cef6edb362fde; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_1d367b7320fbcf4ee75cef6edb362fde (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_1d367b7320fbcf4ee75cef6edb362fde OWNER TO pao;

--
-- Name: elementary_source_table_anomal_2ce586c6f3e4f8063b169987feaae13b; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_2ce586c6f3e4f8063b169987feaae13b (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_2ce586c6f3e4f8063b169987feaae13b OWNER TO pao;

--
-- Name: elementary_source_table_anomal_35d1f5da1941954a451ec76dd44e2b25; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_35d1f5da1941954a451ec76dd44e2b25 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_35d1f5da1941954a451ec76dd44e2b25 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_44cfef083ffc0f32db98b6705dc35ad0; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_44cfef083ffc0f32db98b6705dc35ad0 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_44cfef083ffc0f32db98b6705dc35ad0 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_50b0081412febdc0c8d0d995ef652e95; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_50b0081412febdc0c8d0d995ef652e95 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_50b0081412febdc0c8d0d995ef652e95 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_5f94a447827c99331825f91d2aef4371; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_5f94a447827c99331825f91d2aef4371 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_5f94a447827c99331825f91d2aef4371 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_6483d795700a62151389ec1e6bfcf88c; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_6483d795700a62151389ec1e6bfcf88c (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_6483d795700a62151389ec1e6bfcf88c OWNER TO pao;

--
-- Name: elementary_source_table_anomal_66ea4e1a2b28feb56dcb8e2062c5639a; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_66ea4e1a2b28feb56dcb8e2062c5639a (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_66ea4e1a2b28feb56dcb8e2062c5639a OWNER TO pao;

--
-- Name: elementary_source_table_anomal_6922bee41dc7a8222bb41fd6f593515f; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_6922bee41dc7a8222bb41fd6f593515f (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_6922bee41dc7a8222bb41fd6f593515f OWNER TO pao;

--
-- Name: elementary_source_table_anomal_6d949def88d2afa17ab00368ab6ff63e; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_6d949def88d2afa17ab00368ab6ff63e (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_6d949def88d2afa17ab00368ab6ff63e OWNER TO pao;

--
-- Name: elementary_source_table_anomal_70bb5b2f80298a764b560b83136eb1c1; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_70bb5b2f80298a764b560b83136eb1c1 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_70bb5b2f80298a764b560b83136eb1c1 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_79064ff00378ab7aa09d85a7c86dfd08; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_79064ff00378ab7aa09d85a7c86dfd08 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_79064ff00378ab7aa09d85a7c86dfd08 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_8ae550499177376556dec32eea2e0352; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_8ae550499177376556dec32eea2e0352 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_8ae550499177376556dec32eea2e0352 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_9179bf27bcb5053d6160d55aead4d286; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_9179bf27bcb5053d6160d55aead4d286 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_9179bf27bcb5053d6160d55aead4d286 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_99bd6699ae18bd60c6013f8219cf8ec0; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_99bd6699ae18bd60c6013f8219cf8ec0 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_99bd6699ae18bd60c6013f8219cf8ec0 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_a8a958ffbe7dd831b6b3697e2de73ea6; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_a8a958ffbe7dd831b6b3697e2de73ea6 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_a8a958ffbe7dd831b6b3697e2de73ea6 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_a9871704fefe774dee8ff97e81dac500; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_a9871704fefe774dee8ff97e81dac500 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_a9871704fefe774dee8ff97e81dac500 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_b5d36f853301338947bdcba2fa9782a3; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_b5d36f853301338947bdcba2fa9782a3 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_b5d36f853301338947bdcba2fa9782a3 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_bc53169e3be501d9d1a396e586686ac9; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_bc53169e3be501d9d1a396e586686ac9 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_bc53169e3be501d9d1a396e586686ac9 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_d870d9b5fc538a8c0671304f1ab7d0ad; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_d870d9b5fc538a8c0671304f1ab7d0ad (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_d870d9b5fc538a8c0671304f1ab7d0ad OWNER TO pao;

--
-- Name: elementary_source_table_anomal_e410a3b12c1c8948840e47a10d2a2998; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_e410a3b12c1c8948840e47a10d2a2998 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_e410a3b12c1c8948840e47a10d2a2998 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_e8b8106e417026fb3ac49fc729bfff32; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_e8b8106e417026fb3ac49fc729bfff32 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_e8b8106e417026fb3ac49fc729bfff32 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_eac987f6a6c305f6a2fa0635b2ce1304; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_eac987f6a6c305f6a2fa0635b2ce1304 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_eac987f6a6c305f6a2fa0635b2ce1304 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_ec5a1623ff20ffd27275867d99b96713; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_ec5a1623ff20ffd27275867d99b96713 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_ec5a1623ff20ffd27275867d99b96713 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_ee4f0978f9dc0231db3d5643886a52f0; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_ee4f0978f9dc0231db3d5643886a52f0 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_ee4f0978f9dc0231db3d5643886a52f0 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_eea115f626a0a0fb27a0c9e41e36f288; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_eea115f626a0a0fb27a0c9e41e36f288 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_eea115f626a0a0fb27a0c9e41e36f288 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_f8784b3f7da20b5cb9935284ab57005e; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_f8784b3f7da20b5cb9935284ab57005e (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_f8784b3f7da20b5cb9935284ab57005e OWNER TO pao;

--
-- Name: elementary_source_table_anomal_f8824826e03ae40bfab56a70b5b92a81; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_f8824826e03ae40bfab56a70b5b92a81 (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_f8824826e03ae40bfab56a70b5b92a81 OWNER TO pao;

--
-- Name: elementary_source_table_anomal_fce5986eee907f6ebf51f5842987908b; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_source_table_anomal_fce5986eee907f6ebf51f5842987908b (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_source_table_anomal_fce5986eee907f6ebf51f5842987908b OWNER TO pao;

--
-- Name: elementary_table_anomalies_bsda_row_count; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_table_anomalies_bsda_row_count (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_table_anomalies_bsda_row_count OWNER TO pao;

--
-- Name: elementary_table_anomalies_bsdasri_row_count; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_table_anomalies_bsdasri_row_count (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_table_anomalies_bsdasri_row_count OWNER TO pao;

--
-- Name: elementary_table_anomalies_bsdd_row_count; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.elementary_table_anomalies_bsdd_row_count (
    value double precision,
    average double precision,
    min_value double precision,
    max_value double precision,
    start_time timestamp without time zone,
    end_time timestamp without time zone,
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    anomaly_description text,
    is_anomalous boolean
);


ALTER TABLE dbt_test__audit.elementary_table_anomalies_bsdd_row_count OWNER TO pao;

--
-- Name: not_null_bsdd_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.not_null_bsdd_id (
    id character varying,
    custom_id character varying,
    readable_id character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    status character varying,
    is_deleted boolean,
    owner_id character varying,
    waste_details_code character varying,
    waste_details_name character varying,
    waste_details_pop boolean,
    waste_details_is_dangerous boolean,
    waste_details_onu_code character varying,
    waste_details_quantity double precision,
    waste_details_quantity_type character varying,
    waste_details_consistence character varying,
    waste_details_packaging_infos jsonb,
    waste_details_analysis_references jsonb,
    waste_details_land_identifiers jsonb,
    waste_details_parcel_numbers jsonb,
    waste_acceptation_status character varying,
    waste_refusal_reason character varying,
    emitter_company_siret character varying,
    emitter_company_name character varying,
    emitter_type character varying,
    emitter_company_address character varying,
    emitter_company_contact character varying,
    emitter_company_mail character varying,
    emitter_company_phone character varying,
    emitter_is_foreignship boolean,
    emitter_company_omi_number character varying,
    emitter_is_private_individual boolean,
    emitter_pickup_site character varying,
    emitter_worksite_name character varying,
    emitter_worksite_address character varying,
    emitter_worksite_postal_code character varying,
    emitter_worksite_city character varying,
    emitter_worksite_infos character varying,
    emitted_by_eco_organisme boolean,
    emitted_at timestamp without time zone,
    emitted_by character varying,
    signed_at timestamp without time zone,
    signed_by character varying,
    signed_by_transporter boolean,
    sent_at timestamp without time zone,
    sent_by character varying,
    transporter_company_siret character varying,
    transporter_company_name character varying,
    transporter_company_address character varying,
    transporter_department character varying,
    transporter_company_contact character varying,
    transporter_company_mail character varying,
    transporter_company_phone character varying,
    transporter_number_plate character varying,
    transporter_receipt character varying,
    transporter_validity_limit timestamp without time zone,
    transporter_transport_mode character varying,
    transporter_company_vat_number character varying,
    transporter_custom_info character varying,
    transporter_is_exempted_of_receipt boolean,
    current_transporter_siret character varying,
    next_transporter_siret character varying,
    taken_over_at timestamp without time zone,
    taken_over_by character varying,
    recipient_company_siret character varying,
    recipient_company_name character varying,
    recipient_company_address character varying,
    recipient_company_contact character varying,
    recipient_company_mail character varying,
    recipient_company_phone character varying,
    recipient_is_temp_storage boolean,
    recipient_cap character varying,
    received_at timestamp without time zone,
    received_by character varying,
    processed_at timestamp without time zone,
    processed_by character varying,
    quantity_received double precision,
    quantity_received_type character varying,
    processing_operation_description character varying,
    no_traceability boolean,
    is_accepted boolean,
    next_destination_company_siret character varying,
    next_destination_company_name character varying,
    next_destination_company_address character varying,
    next_destination_company_country character varying,
    next_destination_company_contact character varying,
    next_destination_company_mail character varying,
    next_destination_company_phone character varying,
    next_destination_company_vat_number character varying,
    next_destination_processing_operation character varying,
    broker_company_siret character varying,
    broker_company_name character varying,
    broker_company_address character varying,
    broker_department character varying,
    broker_company_contact character varying,
    broker_company_mail character varying,
    broker_company_phone character varying,
    broker_receipt character varying,
    broker_validity_limit timestamp without time zone,
    trader_company_siret character varying,
    trader_company_name character varying,
    trader_company_address character varying,
    trader_department character varying,
    trader_company_contact character varying,
    trader_company_mail character varying,
    trader_company_phone character varying,
    trader_receipt character varying,
    trader_validity_limit timestamp without time zone,
    eco_organisme_siret character varying,
    eco_organisme_name character varying,
    is_imported_from_paper boolean,
    forwarded_in_id character varying,
    recipient_processing_operation text,
    processing_operation_done text
);


ALTER TABLE dbt_test__audit.not_null_bsdd_id OWNER TO pao;

--
-- Name: relationships_bsdd_owner_id__id__ref_user_; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.relationships_bsdd_owner_id__id__ref_user_ (
    from_field character varying
);


ALTER TABLE dbt_test__audit.relationships_bsdd_owner_id__id__ref_user_ OWNER TO pao;

--
-- Name: source_not_null_raw_zone_gshee_c6db2c99395f498305ba35e49154a1d9; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_gshee_c6db2c99395f498305ba35e49154a1d9 (
    dep_epci character varying,
    siren_epci character varying,
    nom_complet character varying,
    nj_epci2023 character varying,
    fisc_epci2023 character varying,
    nb_com_2023 integer,
    ptot_epci_2023 integer,
    pmun_epci_2023 integer
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_gshee_c6db2c99395f498305ba35e49154a1d9 OWNER TO pao;

--
-- Name: source_not_null_raw_zone_gshee_e221c1b551aaa37983e5475d6a04b85f; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_gshee_e221c1b551aaa37983e5475d6a04b85f (
    siret text,
    raison_sociale text,
    nom_eco_organisme text,
    filiere_dsrep text,
    produits_relevant_filiere_responsabilite_elargie text,
    adresse text,
    code_postal text,
    ville text
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_gshee_e221c1b551aaa37983e5475d6a04b85f OWNER TO pao;

--
-- Name: source_not_null_raw_zone_gsheet_collectivites__SIREN_; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit."source_not_null_raw_zone_gsheet_collectivites__SIREN_" (
    "Région siège" character varying(500),
    "Département siège" character varying(500),
    "Arrondissement siège" character varying(500),
    "Commune siège" character varying(500),
    "SIREN" character varying,
    "Nom du groupement" character varying(500),
    "Nature juridique" character varying(500),
    "Syndicat à la carte" integer,
    "Groupement interdépartemental" integer,
    "Date de création" character varying(500),
    "Date d'effet" character varying(500),
    "Mode de répartition des sièges" character varying(500),
    "Autre mode de répartition des sièges" character varying(2048),
    "Nombre de membres" integer,
    population integer,
    "Nombre de compétences exercées" integer,
    "Mode de financement" character varying(500),
    "DGF Bonifiée" integer,
    dsc integer,
    reom integer,
    "Autre redevance" character varying(500),
    teom integer,
    "Autre taxe" character varying(500),
    "Civilité Président" character varying(500),
    "Prénom Président" character varying(500),
    "Nom Président" character varying(500),
    "Adresse du siège_1" character varying(500),
    "Adresse du siège_2" character varying(500),
    "Adresse du siège_3" character varying(500),
    "Code postal du siège - Ville du siège" character varying(500),
    "Téléphone du siège" character varying(500),
    "Fax du siège" character varying(500),
    "Courriel du siège" character varying(500),
    "Site internet" character varying(500),
    "Adresse annexe_1" character varying(500),
    "Adresse annexe_2" character varying(500),
    "Adresse annexe_3" character varying(500),
    "Code postal annexe - Ville annexe" character varying(500),
    "Téléphone annexe" character varying(500),
    "Fax annexe" character varying(500)
);


ALTER TABLE dbt_test__audit."source_not_null_raw_zone_gsheet_collectivites__SIREN_" OWNER TO pao;

--
-- Name: source_not_null_raw_zone_icpe_etablissements__codeS3ic_; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit."source_not_null_raw_zone_icpe_etablissements__codeS3ic_" (
    "codeS3ic" text,
    "s3icNumeroSiret" text,
    x text,
    y text,
    region text,
    "nomEts" text,
    "codeCommuneEtablissement" text,
    "codePostal" text,
    "etatActivite" text,
    "codeApe" text,
    "nomCommune" text,
    seveso text,
    regime text,
    "prioriteNationale" text,
    ippc text,
    "declarationAnnuelle" text,
    "familleIc" text,
    "baseIdService" text,
    "natureIdService" text,
    adresse1 text,
    adresse2 text,
    "dateInspection" text,
    "indicationSsp" text,
    rayon text,
    "precisionPositionnement" text,
    inserted_at timestamp without time zone
);


ALTER TABLE dbt_test__audit."source_not_null_raw_zone_icpe_etablissements__codeS3ic_" OWNER TO pao;

--
-- Name: source_not_null_raw_zone_icpe_installations_classees__codeS3ic_; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit."source_not_null_raw_zone_icpe_installations_classees__codeS3ic_" (
    "codeS3ic" text,
    id text,
    volume text,
    unite text,
    date_debut_exploitation text,
    date_fin_validite text,
    statut_ic text,
    id_ref_nomencla_ic text,
    inserted_at timestamp without time zone
);


ALTER TABLE dbt_test__audit."source_not_null_raw_zone_icpe_installations_classees__codeS3ic_" OWNER TO pao;

--
-- Name: source_not_null_raw_zone_icpe_nomenclature_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_icpe_nomenclature_id (
    id text,
    rubrique_ic text,
    famille_ic text,
    sfamille_ic text,
    ssfamille_ic text,
    alinea text,
    libellecourt_activite text,
    id_regime text,
    envigueur text,
    ippc text,
    inserted_at timestamp without time zone
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_icpe_nomenclature_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_insee_arrondissement_arr; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_insee_arrondissement_arr (
    arr character varying,
    dep character varying,
    reg character varying,
    cheflieu character varying,
    tncc character varying,
    ncc character varying,
    nccenr character varying,
    libelle character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_insee_arrondissement_arr OWNER TO pao;

--
-- Name: source_not_null_raw_zone_insee_canton_id_canton; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_insee_canton_id_canton (
    id_canton character varying,
    id_departement character varying,
    id_region character varying,
    typct character varying,
    burcentral character varying,
    tncc character varying,
    ncc character varying,
    nccenr character varying,
    libelle character varying,
    actual character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_insee_canton_id_canton OWNER TO pao;

--
-- Name: source_not_null_raw_zone_insee_commune_com; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_insee_commune_com (
    typecom character varying,
    com character varying,
    reg character varying,
    dep character varying,
    ctcd character varying,
    arr character varying,
    tncc character varying,
    ncc character varying,
    nccenr character varying,
    libelle character varying,
    can character varying,
    comparent character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_insee_commune_com OWNER TO pao;

--
-- Name: source_not_null_raw_zone_insee_departement_dep; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_insee_departement_dep (
    dep character varying,
    reg character varying,
    cheflieu character varying,
    tncc character varying,
    ncc character varying,
    nccenr character varying,
    libelle character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_insee_departement_dep OWNER TO pao;

--
-- Name: source_not_null_raw_zone_insee_naf2008_code_sous_classe; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_insee_naf2008_code_sous_classe (
    code_section character varying,
    libelle_section character varying,
    code_division character varying,
    libelle_division character varying,
    code_groupe character varying,
    libelle_groupe character varying,
    code_classe character varying,
    libelle_classe character varying,
    code_sous_classe character varying,
    libelle_sous_classe character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_insee_naf2008_code_sous_classe OWNER TO pao;

--
-- Name: source_not_null_raw_zone_insee_region_reg; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_insee_region_reg (
    reg character varying,
    cheflieu character varying,
    tncc character varying,
    ncc character varying,
    nccenr character varying,
    libelle character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_insee_region_reg OWNER TO pao;

--
-- Name: source_not_null_raw_zone_insee_stock_etablissement_siret; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_insee_stock_etablissement_siret (
    siren character varying,
    nic character varying,
    siret character varying,
    "statutDiffusionEtablissement" character varying,
    "dateCreationEtablissement" character varying,
    "trancheEffectifsEtablissement" character varying,
    "anneeEffectifsEtablissement" character varying,
    "activitePrincipaleRegistreMetiersEtablissement" character varying,
    "dateDernierTraitementEtablissement" character varying,
    "etablissementSiege" character varying,
    "nombrePeriodesEtablissement" character varying,
    "complementAdresseEtablissement" character varying,
    "numeroVoieEtablissement" character varying,
    "indiceRepetitionEtablissement" character varying,
    "typeVoieEtablissement" character varying,
    "libelleVoieEtablissement" character varying,
    "codePostalEtablissement" character varying,
    "libelleCommuneEtablissement" character varying,
    "libelleCommuneEtrangerEtablissement" character varying,
    "distributionSpecialeEtablissement" character varying,
    "codeCommuneEtablissement" character varying,
    "codeCedexEtablissement" character varying,
    "libelleCedexEtablissement" character varying,
    "codePaysEtrangerEtablissement" character varying,
    "libellePaysEtrangerEtablissement" character varying,
    "complementAdresse2Etablissement" character varying,
    "numeroVoie2Etablissement" character varying,
    "indiceRepetition2Etablissement" character varying,
    "typeVoie2Etablissement" character varying,
    "libelleVoie2Etablissement" character varying,
    "codePostal2Etablissement" character varying,
    "libelleCommune2Etablissement" character varying,
    "libelleCommuneEtranger2Etablissement" character varying,
    "distributionSpeciale2Etablissement" character varying,
    "codeCommune2Etablissement" character varying,
    "codeCedex2Etablissement" character varying,
    "libelleCedex2Etablissement" character varying,
    "codePaysEtranger2Etablissement" character varying,
    "libellePaysEtranger2Etablissement" character varying,
    "dateDebut" character varying,
    "etatAdministratifEtablissement" character varying,
    "enseigne1Etablissement" character varying,
    "enseigne2Etablissement" character varying,
    "enseigne3Etablissement" character varying,
    "denominationUsuelleEtablissement" character varying,
    "activitePrincipaleEtablissement" character varying,
    "nomenclatureActivitePrincipaleEtablissement" character varying,
    "caractereEmployeurEtablissement" character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_insee_stock_etablissement_siret OWNER TO pao;

--
-- Name: source_not_null_raw_zone_laposte_hexasmal_code_commune_insee; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_laposte_hexasmal_code_commune_insee (
    code_commune_insee character varying,
    nom_commune character varying,
    code_postal integer,
    ligne_5 character varying,
    "libellé_d_acheminement" character varying,
    coordonnees_gps character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_laposte_hexasmal_code_commune_insee OWNER TO pao;

--
-- Name: source_not_null_raw_zone_laposte_hexasmal_code_postal; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_laposte_hexasmal_code_postal (
    code_commune_insee character varying,
    nom_commune character varying,
    code_postal integer,
    ligne_5 character varying,
    "libellé_d_acheminement" character varying,
    coordonnees_gps character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_laposte_hexasmal_code_postal OWNER TO pao;

--
-- Name: source_not_null_raw_zone_track_09cdde334b15fe84f3eac2ca28cfb02c; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_track_09cdde334b15fe84f3eac2ca28cfb02c (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    authoringcompanyid character varying,
    brokercompanyaddress character varying,
    brokercompanycontact character varying,
    brokercompanymail character varying,
    brokercompanyname character varying,
    brokercompanyphone character varying,
    brokercompanysiret character varying,
    brokerdepartment character varying,
    brokerreceipt character varying,
    brokervaliditylimit timestamp without time zone,
    bsddid character varying,
    comment character varying,
    createdat timestamp without time zone,
    id character varying,
    iscanceled boolean,
    processingoperationdescription character varying,
    processingoperationdone character varying,
    quantityreceived double precision,
    recipientcap character varying,
    status character varying,
    temporarystoragedestinationcap character varying,
    temporarystoragedestinationprocessingoperation character varying,
    temporarystoragetemporarystorerquantityreceived double precision,
    tradercompanyaddress character varying,
    tradercompanycontact character varying,
    tradercompanymail character varying,
    tradercompanyname character varying,
    tradercompanyphone character varying,
    tradercompanysiret character varying,
    traderdepartment character varying,
    traderreceipt character varying,
    tradervaliditylimit timestamp without time zone,
    updatedat timestamp without time zone,
    wastedetailscode character varying,
    wastedetailsname character varying,
    wastedetailspackaginginfos jsonb,
    wastedetailspop boolean
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_track_09cdde334b15fe84f3eac2ca28cfb02c OWNER TO pao;

--
-- Name: source_not_null_raw_zone_track_1e31310293ef1571d6daff9147caada5; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_track_1e31310293ef1571d6daff9147caada5 (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    authoringcompanyid character varying,
    brokercompanyaddress character varying,
    brokercompanycontact character varying,
    brokercompanymail character varying,
    brokercompanyname character varying,
    brokercompanyphone character varying,
    brokercompanysiret character varying,
    brokerdepartment character varying,
    brokerreceipt character varying,
    brokervaliditylimit timestamp without time zone,
    bsddid character varying,
    comment character varying,
    createdat timestamp without time zone,
    id character varying,
    iscanceled boolean,
    processingoperationdescription character varying,
    processingoperationdone character varying,
    quantityreceived double precision,
    recipientcap character varying,
    status character varying,
    temporarystoragedestinationcap character varying,
    temporarystoragedestinationprocessingoperation character varying,
    temporarystoragetemporarystorerquantityreceived double precision,
    tradercompanyaddress character varying,
    tradercompanycontact character varying,
    tradercompanymail character varying,
    tradercompanyname character varying,
    tradercompanyphone character varying,
    tradercompanysiret character varying,
    traderdepartment character varying,
    traderreceipt character varying,
    tradervaliditylimit timestamp without time zone,
    updatedat timestamp without time zone,
    wastedetailscode character varying,
    wastedetailsname character varying,
    wastedetailspackaginginfos jsonb,
    wastedetailspop boolean
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_track_1e31310293ef1571d6daff9147caada5 OWNER TO pao;

--
-- Name: source_not_null_raw_zone_track_255df0119f50dc221975b21069f5bd28; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_track_255df0119f50dc221975b21069f5bd28 (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    agrementnumber character varying,
    department character varying,
    id character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_track_255df0119f50dc221975b21069f5bd28 OWNER TO pao;

--
-- Name: source_not_null_raw_zone_track_63ab2f0d78dc3368dbe1d6cf1f88e50e; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_track_63ab2f0d78dc3368dbe1d6cf1f88e50e (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    authoringcompanyid character varying,
    brokercompanyaddress character varying,
    brokercompanycontact character varying,
    brokercompanymail character varying,
    brokercompanyname character varying,
    brokercompanyphone character varying,
    brokercompanysiret character varying,
    brokerrecepissedepartment character varying,
    brokerrecepissenumber character varying,
    brokerrecepissevaliditylimit timestamp without time zone,
    bsdaid character varying,
    comment character varying,
    createdat timestamp without time zone,
    destinationcap character varying,
    destinationoperationcode character varying,
    destinationoperationdescription character varying,
    destinationreceptionweight double precision,
    emitterpickupsiteaddress character varying,
    emitterpickupsitecity character varying,
    emitterpickupsiteinfos character varying,
    emitterpickupsitename character varying,
    emitterpickupsitepostalcode character varying,
    id character varying,
    packagings jsonb,
    status character varying,
    updatedat timestamp without time zone,
    wastecode character varying,
    wastematerialname character varying,
    wastepop boolean,
    wastesealnumbers jsonb,
    iscanceled boolean
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_track_63ab2f0d78dc3368dbe1d6cf1f88e50e OWNER TO pao;

--
-- Name: source_not_null_raw_zone_track_6e1b6a004536789e15d80393bb047f8e; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_track_6e1b6a004536789e15d80393bb047f8e (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    department character varying,
    id character varying,
    receiptnumber character varying,
    validitylimit timestamp without time zone
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_track_6e1b6a004536789e15d80393bb047f8e OWNER TO pao;

--
-- Name: source_not_null_raw_zone_track_9b63f8033202c8309ca7cf1b3223eab0; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_track_9b63f8033202c8309ca7cf1b3223eab0 (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    companyid character varying,
    id character varying,
    role character varying,
    userid character varying,
    createdat timestamp without time zone
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_track_9b63f8033202c8309ca7cf1b3223eab0 OWNER TO pao;

--
-- Name: source_not_null_raw_zone_track_b92373503a01b7360e390a7d03fdcf03; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_track_b92373503a01b7360e390a7d03fdcf03 (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    department character varying,
    id character varying,
    receiptnumber character varying,
    validitylimit timestamp without time zone
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_track_b92373503a01b7360e390a7d03fdcf03 OWNER TO pao;

--
-- Name: source_not_null_raw_zone_track_cf2521630226b2d5e99f4e4f988cd0fb; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_track_cf2521630226b2d5e99f4e4f988cd0fb (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    authoringcompanyid character varying,
    brokercompanyaddress character varying,
    brokercompanycontact character varying,
    brokercompanymail character varying,
    brokercompanyname character varying,
    brokercompanyphone character varying,
    brokercompanysiret character varying,
    brokerrecepissedepartment character varying,
    brokerrecepissenumber character varying,
    brokerrecepissevaliditylimit timestamp without time zone,
    bsdaid character varying,
    comment character varying,
    createdat timestamp without time zone,
    destinationcap character varying,
    destinationoperationcode character varying,
    destinationoperationdescription character varying,
    destinationreceptionweight double precision,
    emitterpickupsiteaddress character varying,
    emitterpickupsitecity character varying,
    emitterpickupsiteinfos character varying,
    emitterpickupsitename character varying,
    emitterpickupsitepostalcode character varying,
    id character varying,
    packagings jsonb,
    status character varying,
    updatedat timestamp without time zone,
    wastecode character varying,
    wastematerialname character varying,
    wastepop boolean,
    wastesealnumbers jsonb,
    iscanceled boolean
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_track_cf2521630226b2d5e99f4e4f988cd0fb OWNER TO pao;

--
-- Name: source_not_null_raw_zone_track_e40e1d6bf202c5d545692a267d6e7b5d; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_track_e40e1d6bf202c5d545692a267d6e7b5d (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    authoringcompanyid character varying,
    brokercompanyaddress character varying,
    brokercompanycontact character varying,
    brokercompanymail character varying,
    brokercompanyname character varying,
    brokercompanyphone character varying,
    brokercompanysiret character varying,
    brokerdepartment character varying,
    brokerreceipt character varying,
    brokervaliditylimit timestamp without time zone,
    bsddid character varying,
    comment character varying,
    createdat timestamp without time zone,
    id character varying,
    iscanceled boolean,
    processingoperationdescription character varying,
    processingoperationdone character varying,
    quantityreceived double precision,
    recipientcap character varying,
    status character varying,
    temporarystoragedestinationcap character varying,
    temporarystoragedestinationprocessingoperation character varying,
    temporarystoragetemporarystorerquantityreceived double precision,
    tradercompanyaddress character varying,
    tradercompanycontact character varying,
    tradercompanymail character varying,
    tradercompanyname character varying,
    tradercompanyphone character varying,
    tradercompanysiret character varying,
    traderdepartment character varying,
    traderreceipt character varying,
    tradervaliditylimit timestamp without time zone,
    updatedat timestamp without time zone,
    wastedetailscode character varying,
    wastedetailsname character varying,
    wastedetailspackaginginfos jsonb,
    wastedetailspop boolean
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_track_e40e1d6bf202c5d545692a267d6e7b5d OWNER TO pao;

--
-- Name: source_not_null_raw_zone_track_ed05d65f567eba44f163edec990345ab; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_track_ed05d65f567eba44f163edec990345ab (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    department character varying,
    id character varying,
    receiptnumber character varying,
    validitylimit timestamp without time zone
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_track_ed05d65f567eba44f163edec990345ab OWNER TO pao;

--
-- Name: source_not_null_raw_zone_track_f8cfcfdcd26b102ad49f0e2a6b1173a1; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_track_f8cfcfdcd26b102ad49f0e2a6b1173a1 (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    authoringcompanyid character varying,
    brokercompanyaddress character varying,
    brokercompanycontact character varying,
    brokercompanymail character varying,
    brokercompanyname character varying,
    brokercompanyphone character varying,
    brokercompanysiret character varying,
    brokerrecepissedepartment character varying,
    brokerrecepissenumber character varying,
    brokerrecepissevaliditylimit timestamp without time zone,
    bsdaid character varying,
    comment character varying,
    createdat timestamp without time zone,
    destinationcap character varying,
    destinationoperationcode character varying,
    destinationoperationdescription character varying,
    destinationreceptionweight double precision,
    emitterpickupsiteaddress character varying,
    emitterpickupsitecity character varying,
    emitterpickupsiteinfos character varying,
    emitterpickupsitename character varying,
    emitterpickupsitepostalcode character varying,
    id character varying,
    packagings jsonb,
    status character varying,
    updatedat timestamp without time zone,
    wastecode character varying,
    wastematerialname character varying,
    wastepop boolean,
    wastesealnumbers jsonb,
    iscanceled boolean
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_track_f8cfcfdcd26b102ad49f0e2a6b1173a1 OWNER TO pao;

--
-- Name: source_not_null_raw_zone_track_ff1fc44efc7d78a620420083c944a36a; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_track_ff1fc44efc7d78a620420083c944a36a (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    department character varying,
    id character varying,
    receiptnumber character varying,
    validitylimit timestamp without time zone
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_track_ff1fc44efc7d78a620420083c944a36a OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_broker_receipt_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_broker_receipt_raw_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    department character varying,
    id character varying,
    receiptnumber character varying,
    validitylimit timestamp without time zone
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_broker_receipt_raw_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_bsda_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsda_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    brokercompanyaddress character varying,
    brokercompanycontact character varying,
    brokercompanymail character varying,
    brokercompanyname character varying,
    brokercompanyphone character varying,
    brokercompanysiret character varying,
    brokerrecepissedepartment character varying,
    brokerrecepissenumber character varying,
    brokerrecepissevaliditylimit timestamp without time zone,
    createdat timestamp without time zone,
    destinationcap character varying,
    destinationcompanyaddress character varying,
    destinationcompanycontact character varying,
    destinationcompanymail character varying,
    destinationcompanyname character varying,
    destinationcompanyphone character varying,
    destinationcompanysiret character varying,
    destinationcustominfo character varying,
    destinationoperationcode character varying,
    destinationoperationdate timestamp without time zone,
    destinationoperationdescription character varying,
    destinationoperationnextdestinationcap character varying,
    destinationoperationnextdestinationcompanyaddress character varying,
    destinationoperationnextdestinationcompanycontact character varying,
    destinationoperationnextdestinationcompanymail character varying,
    destinationoperationnextdestinationcompanyname character varying,
    destinationoperationnextdestinationcompanyphone character varying,
    destinationoperationnextdestinationcompanysiret character varying,
    destinationoperationnextdestinationcompanyvatnumber character varying,
    destinationoperationnextdestinationplannedoperationcode character varying,
    destinationoperationsignatureauthor character varying,
    destinationoperationsignaturedate timestamp without time zone,
    destinationplannedoperationcode character varying,
    destinationreceptionacceptationstatus character varying,
    destinationreceptiondate timestamp without time zone,
    destinationreceptionrefusalreason character varying,
    destinationreceptionweight double precision,
    ecoorganismename character varying,
    ecoorganismesiret character varying,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emittercustominfo character varying,
    emitteremissionsignatureauthor character varying,
    emitteremissionsignaturedate timestamp without time zone,
    emitterisprivateindividual boolean,
    emitterpickupsiteaddress character varying,
    emitterpickupsitecity character varying,
    emitterpickupsiteinfos character varying,
    emitterpickupsitename character varying,
    emitterpickupsitepostalcode character varying,
    forwardingid character varying,
    groupedinid character varying,
    id character varying,
    isdeleted boolean,
    isdraft boolean,
    packagings jsonb,
    repackagedinid character varying,
    status character varying,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterrecepissedepartment character varying,
    transporterrecepisseisexempted boolean,
    transporterrecepissenumber character varying,
    transporterrecepissevaliditylimit timestamp without time zone,
    transportertransportmode character varying,
    transportertransportplates jsonb,
    transportertransportsignatureauthor character varying,
    transportertransportsignaturedate timestamp without time zone,
    transportertransporttakenoverat timestamp without time zone,
    type character varying,
    updatedat timestamp without time zone,
    wasteadr character varying,
    wastecode character varying,
    wasteconsistence character varying,
    wastefamilycode character varying,
    wastematerialname character varying,
    wastepop boolean,
    wastesealnumbers jsonb,
    weightisestimate boolean,
    weightvalue double precision,
    workercompanyaddress character varying,
    workercompanycontact character varying,
    workercompanymail character varying,
    workercompanyname character varying,
    workercompanyphone character varying,
    workercompanysiret character varying,
    workerisdisabled boolean,
    workerworkhasemitterpapersignature boolean,
    workerworksignatureauthor character varying,
    workerworksignaturedate timestamp without time zone,
    workercertificationcertificationnumber character varying,
    workercertificationhassubsectionfour boolean,
    workercertificationhassubsectionthree boolean,
    workercertificationorganisation character varying,
    workercertificationvaliditylimit timestamp without time zone
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsda_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_bsda_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsda_raw_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    brokercompanyaddress character varying,
    brokercompanycontact character varying,
    brokercompanymail character varying,
    brokercompanyname character varying,
    brokercompanyphone character varying,
    brokercompanysiret character varying,
    brokerrecepissedepartment character varying,
    brokerrecepissenumber character varying,
    brokerrecepissevaliditylimit timestamp without time zone,
    createdat timestamp without time zone,
    destinationcap character varying,
    destinationcompanyaddress character varying,
    destinationcompanycontact character varying,
    destinationcompanymail character varying,
    destinationcompanyname character varying,
    destinationcompanyphone character varying,
    destinationcompanysiret character varying,
    destinationcustominfo character varying,
    destinationoperationcode character varying,
    destinationoperationdate timestamp without time zone,
    destinationoperationdescription character varying,
    destinationoperationnextdestinationcap character varying,
    destinationoperationnextdestinationcompanyaddress character varying,
    destinationoperationnextdestinationcompanycontact character varying,
    destinationoperationnextdestinationcompanymail character varying,
    destinationoperationnextdestinationcompanyname character varying,
    destinationoperationnextdestinationcompanyphone character varying,
    destinationoperationnextdestinationcompanysiret character varying,
    destinationoperationnextdestinationcompanyvatnumber character varying,
    destinationoperationnextdestinationplannedoperationcode character varying,
    destinationoperationsignatureauthor character varying,
    destinationoperationsignaturedate timestamp without time zone,
    destinationplannedoperationcode character varying,
    destinationreceptionacceptationstatus character varying,
    destinationreceptiondate timestamp without time zone,
    destinationreceptionrefusalreason character varying,
    destinationreceptionweight double precision,
    ecoorganismename character varying,
    ecoorganismesiret character varying,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emittercustominfo character varying,
    emitteremissionsignatureauthor character varying,
    emitteremissionsignaturedate timestamp without time zone,
    emitterisprivateindividual boolean,
    emitterpickupsiteaddress character varying,
    emitterpickupsitecity character varying,
    emitterpickupsiteinfos character varying,
    emitterpickupsitename character varying,
    emitterpickupsitepostalcode character varying,
    forwardingid character varying,
    groupedinid character varying,
    id character varying,
    isdeleted boolean,
    isdraft boolean,
    packagings jsonb,
    repackagedinid character varying,
    status character varying,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterrecepissedepartment character varying,
    transporterrecepisseisexempted boolean,
    transporterrecepissenumber character varying,
    transporterrecepissevaliditylimit timestamp without time zone,
    transportertransportmode character varying,
    transportertransportplates jsonb,
    transportertransportsignatureauthor character varying,
    transportertransportsignaturedate timestamp without time zone,
    transportertransporttakenoverat timestamp without time zone,
    type character varying,
    updatedat timestamp without time zone,
    wasteadr character varying,
    wastecode character varying,
    wasteconsistence character varying,
    wastefamilycode character varying,
    wastematerialname character varying,
    wastepop boolean,
    wastesealnumbers jsonb,
    weightisestimate boolean,
    weightvalue double precision,
    workercompanyaddress character varying,
    workercompanycontact character varying,
    workercompanymail character varying,
    workercompanyname character varying,
    workercompanyphone character varying,
    workercompanysiret character varying,
    workerisdisabled boolean,
    workerworkhasemitterpapersignature boolean,
    workerworksignatureauthor character varying,
    workerworksignaturedate timestamp without time zone,
    workercertificationcertificationnumber character varying,
    workercertificationhassubsectionfour boolean,
    workercertificationhassubsectionthree boolean,
    workercertificationorganisation character varying,
    workercertificationvaliditylimit timestamp without time zone,
    intermediariesorgids jsonb
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsda_raw_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_bsdasri_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsdasri_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    createdat timestamp without time zone,
    destinationcompanyaddress character varying,
    destinationcompanycontact character varying,
    destinationcompanymail character varying,
    destinationcompanyname character varying,
    destinationcompanyphone character varying,
    destinationcompanysiret character varying,
    destinationcustominfo character varying,
    destinationoperationcode character varying,
    destinationoperationdate timestamp without time zone,
    destinationoperationsignatureauthor character varying,
    destinationoperationsignaturedate timestamp without time zone,
    destinationreceptionacceptationstatus character varying,
    destinationreceptiondate timestamp without time zone,
    destinationreceptionsignatureauthor character varying,
    destinationreceptionsignaturedate timestamp without time zone,
    destinationreceptionwasterefusalreason character varying,
    destinationreceptionwasterefusedweightvalue double precision,
    destinationreceptionwastevolume double precision,
    destinationreceptionwasteweightvalue double precision,
    destinationwastepackagings jsonb,
    ecoorganismename character varying,
    ecoorganismesiret character varying,
    emissionsignatoryid character varying,
    emittedbyecoorganisme boolean,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emittercustominfo character varying,
    emitteremissionsignatureauthor character varying,
    emitteremissionsignaturedate timestamp without time zone,
    emitterpickupsiteaddress character varying,
    emitterpickupsitecity character varying,
    emitterpickupsiteinfos character varying,
    emitterpickupsitename character varying,
    emitterpickupsitepostalcode character varying,
    emitterwastepackagings jsonb,
    emitterwastevolume double precision,
    emitterwasteweightisestimate boolean,
    emitterwasteweightvalue double precision,
    groupedinid character varying,
    handedovertorecipientat timestamp without time zone,
    id character varying,
    identificationnumbers jsonb,
    isdeleted boolean,
    isdraft boolean,
    isemissiondirecttakenover boolean,
    isemissiontakenoverwithsecretcode boolean,
    operationsignatoryid character varying,
    receptionsignatoryid character varying,
    status character varying,
    synthesizedinid character varying,
    transportsignatoryid character varying,
    transporteracceptationstatus character varying,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterrecepissedepartment character varying,
    transporterrecepissenumber character varying,
    transporterrecepissevaliditylimit timestamp without time zone,
    transportertakenoverat timestamp without time zone,
    transportertransportmode character varying,
    transportertransportplates jsonb,
    transportertransportsignatureauthor character varying,
    transportertransportsignaturedate timestamp without time zone,
    transporterwastepackagings jsonb,
    transporterwasterefusalreason character varying,
    transporterwasterefusedweightvalue double precision,
    transporterwastevolume double precision,
    transporterwasteweightisestimate boolean,
    transporterwasteweightvalue double precision,
    type character varying,
    updatedat timestamp without time zone,
    wasteadr character varying,
    wastecode character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsdasri_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_bsdasri_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsdasri_raw_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    createdat timestamp without time zone,
    destinationcompanyaddress character varying,
    destinationcompanycontact character varying,
    destinationcompanymail character varying,
    destinationcompanyname character varying,
    destinationcompanyphone character varying,
    destinationcompanysiret character varying,
    destinationcustominfo character varying,
    destinationoperationcode character varying,
    destinationoperationdate timestamp without time zone,
    destinationoperationsignatureauthor character varying,
    destinationoperationsignaturedate timestamp without time zone,
    destinationreceptionacceptationstatus character varying,
    destinationreceptiondate timestamp without time zone,
    destinationreceptionsignatureauthor character varying,
    destinationreceptionsignaturedate timestamp without time zone,
    destinationreceptionwasterefusalreason character varying,
    destinationreceptionwasterefusedweightvalue double precision,
    destinationreceptionwastevolume double precision,
    destinationreceptionwasteweightvalue double precision,
    destinationwastepackagings jsonb,
    ecoorganismename character varying,
    ecoorganismesiret character varying,
    emissionsignatoryid character varying,
    emittedbyecoorganisme boolean,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emittercustominfo character varying,
    emitteremissionsignatureauthor character varying,
    emitteremissionsignaturedate timestamp without time zone,
    emitterpickupsiteaddress character varying,
    emitterpickupsitecity character varying,
    emitterpickupsiteinfos character varying,
    emitterpickupsitename character varying,
    emitterpickupsitepostalcode character varying,
    emitterwastepackagings jsonb,
    emitterwastevolume double precision,
    emitterwasteweightisestimate boolean,
    emitterwasteweightvalue double precision,
    groupedinid character varying,
    handedovertorecipientat timestamp without time zone,
    id character varying,
    identificationnumbers jsonb,
    isdeleted boolean,
    isdraft boolean,
    isemissiondirecttakenover boolean,
    isemissiontakenoverwithsecretcode boolean,
    operationsignatoryid character varying,
    receptionsignatoryid character varying,
    status character varying,
    synthesizedinid character varying,
    transportsignatoryid character varying,
    transporteracceptationstatus character varying,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterrecepissedepartment character varying,
    transporterrecepissenumber character varying,
    transporterrecepissevaliditylimit timestamp without time zone,
    transportertakenoverat timestamp without time zone,
    transportertransportmode character varying,
    transportertransportplates jsonb,
    transportertransportsignatureauthor character varying,
    transportertransportsignaturedate timestamp without time zone,
    transporterwastepackagings jsonb,
    transporterwasterefusalreason character varying,
    transporterwasterefusedweightvalue double precision,
    transporterwastevolume double precision,
    transporterwasteweightisestimate boolean,
    transporterwasteweightvalue double precision,
    type character varying,
    updatedat timestamp without time zone,
    wasteadr character varying,
    wastecode character varying,
    synthesisemittersirets jsonb,
    transporterrecepisseisexempted boolean
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsdasri_raw_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_bsdd_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsdd_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    brokercompanyaddress character varying,
    brokercompanycontact character varying,
    brokercompanymail character varying,
    brokercompanyname character varying,
    brokercompanyphone character varying,
    brokercompanysiret character varying,
    brokerdepartment character varying,
    brokerreceipt character varying,
    brokervaliditylimit timestamp without time zone,
    createdat timestamp without time zone,
    currenttransportersiret character varying,
    customid character varying,
    ecoorganismename character varying,
    ecoorganismesiret character varying,
    emittedat timestamp without time zone,
    emittedby character varying,
    emittedbyecoorganisme boolean,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyominumber character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emitterisforeignship boolean,
    emitterisprivateindividual boolean,
    emitterpickupsite character varying,
    emittertype character varying,
    emitterworksiteaddress character varying,
    emitterworksitecity character varying,
    emitterworksiteinfos character varying,
    emitterworksitename character varying,
    emitterworksitepostalcode character varying,
    forwardedinid character varying,
    id character varying,
    isaccepted boolean,
    isdeleted boolean,
    isimportedfrompaper boolean,
    nextdestinationcompanyaddress character varying,
    nextdestinationcompanycontact character varying,
    nextdestinationcompanycountry character varying,
    nextdestinationcompanymail character varying,
    nextdestinationcompanyname character varying,
    nextdestinationcompanyphone character varying,
    nextdestinationcompanysiret character varying,
    nextdestinationprocessingoperation character varying,
    nexttransportersiret character varying,
    notraceability boolean,
    ownerid character varying,
    processedat timestamp without time zone,
    processedby character varying,
    processingoperationdescription character varying,
    processingoperationdone character varying,
    quantitygrouped double precision,
    quantityreceived double precision,
    quantityreceivedtype character varying,
    readableid character varying,
    receivedat timestamp without time zone,
    receivedby character varying,
    recipientcap character varying,
    recipientcompanyaddress character varying,
    recipientcompanycontact character varying,
    recipientcompanymail character varying,
    recipientcompanyname character varying,
    recipientcompanyphone character varying,
    recipientcompanysiret character varying,
    recipientistempstorage boolean,
    recipientprocessingoperation character varying,
    sentat timestamp without time zone,
    sentby character varying,
    signedat timestamp without time zone,
    signedby character varying,
    signedbytransporter boolean,
    status character varying,
    takenoverat timestamp without time zone,
    takenoverby character varying,
    tradercompanyaddress character varying,
    tradercompanycontact character varying,
    tradercompanymail character varying,
    tradercompanyname character varying,
    tradercompanyphone character varying,
    tradercompanysiret character varying,
    traderdepartment character varying,
    traderreceipt character varying,
    tradervaliditylimit timestamp without time zone,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterdepartment character varying,
    transporterisexemptedofreceipt boolean,
    transporternumberplate character varying,
    transporterreceipt character varying,
    transportertransportmode character varying,
    transportervaliditylimit timestamp without time zone,
    updatedat timestamp without time zone,
    wasteacceptationstatus character varying,
    wastedetailsanalysisreferences jsonb,
    wastedetailscode character varying,
    wastedetailsconsistence character varying,
    wastedetailsisdangerous boolean,
    wastedetailslandidentifiers jsonb,
    wastedetailsname character varying,
    wastedetailsonucode character varying,
    wastedetailspackaginginfos jsonb,
    wastedetailsparcelnumbers jsonb,
    wastedetailspop boolean,
    wastedetailsquantity double precision,
    wastedetailsquantitytype character varying,
    wasterefusalreason character varying,
    nextdestinationcompanyvatnumber character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsdd_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_bsdd_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsdd_raw_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    brokercompanyaddress character varying,
    brokercompanycontact character varying,
    brokercompanymail character varying,
    brokercompanyname character varying,
    brokercompanyphone character varying,
    brokercompanysiret character varying,
    brokerdepartment character varying,
    brokerreceipt character varying,
    brokervaliditylimit timestamp without time zone,
    createdat timestamp without time zone,
    currenttransportersiret character varying,
    customid character varying,
    ecoorganismename character varying,
    ecoorganismesiret character varying,
    emittedat timestamp without time zone,
    emittedby character varying,
    emittedbyecoorganisme boolean,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyominumber character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emitterisforeignship boolean,
    emitterisprivateindividual boolean,
    emitterpickupsite character varying,
    emittertype character varying,
    emitterworksiteaddress character varying,
    emitterworksitecity character varying,
    emitterworksiteinfos character varying,
    emitterworksitename character varying,
    emitterworksitepostalcode character varying,
    forwardedinid character varying,
    id character varying,
    isaccepted boolean,
    isdeleted boolean,
    isimportedfrompaper boolean,
    nextdestinationcompanyaddress character varying,
    nextdestinationcompanycontact character varying,
    nextdestinationcompanycountry character varying,
    nextdestinationcompanymail character varying,
    nextdestinationcompanyname character varying,
    nextdestinationcompanyphone character varying,
    nextdestinationcompanysiret character varying,
    nextdestinationprocessingoperation character varying,
    nexttransportersiret character varying,
    notraceability boolean,
    ownerid character varying,
    processedat timestamp without time zone,
    processedby character varying,
    processingoperationdescription character varying,
    processingoperationdone character varying,
    quantitygrouped double precision,
    quantityreceived double precision,
    quantityreceivedtype character varying,
    readableid character varying,
    receivedat timestamp without time zone,
    receivedby character varying,
    recipientcap character varying,
    recipientcompanyaddress character varying,
    recipientcompanycontact character varying,
    recipientcompanymail character varying,
    recipientcompanyname character varying,
    recipientcompanyphone character varying,
    recipientcompanysiret character varying,
    recipientistempstorage boolean,
    recipientprocessingoperation character varying,
    sentat timestamp without time zone,
    sentby character varying,
    signedat timestamp without time zone,
    signedby character varying,
    signedbytransporter boolean,
    status character varying,
    takenoverat timestamp without time zone,
    takenoverby character varying,
    tradercompanyaddress character varying,
    tradercompanycontact character varying,
    tradercompanymail character varying,
    tradercompanyname character varying,
    tradercompanyphone character varying,
    tradercompanysiret character varying,
    traderdepartment character varying,
    traderreceipt character varying,
    tradervaliditylimit timestamp without time zone,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterdepartment character varying,
    transporterisexemptedofreceipt boolean,
    transporternumberplate character varying,
    transporterreceipt character varying,
    transportertransportmode character varying,
    transportervaliditylimit timestamp without time zone,
    updatedat timestamp without time zone,
    wasteacceptationstatus character varying,
    wastedetailsanalysisreferences jsonb,
    wastedetailscode character varying,
    wastedetailsconsistence character varying,
    wastedetailsisdangerous boolean,
    wastedetailslandidentifiers jsonb,
    wastedetailsname character varying,
    wastedetailsonucode character varying,
    wastedetailspackaginginfos jsonb,
    wastedetailsparcelnumbers jsonb,
    wastedetailspop boolean,
    wastedetailsquantity double precision,
    wastedetailsquantitytype character varying,
    wasterefusalreason character varying,
    nextdestinationcompanyvatnumber character varying,
    intermediariessirets jsonb,
    recipientssirets jsonb,
    transporterssirets jsonb,
    nextdestinationnotificationnumber character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsdd_raw_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_bsff_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsff_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    createdat timestamp without time zone,
    destinationcompanyaddress character varying,
    destinationcompanycontact character varying,
    destinationcompanymail character varying,
    destinationcompanyname character varying,
    destinationcompanyphone character varying,
    destinationcompanysiret character varying,
    destinationcustominfo character varying,
    destinationoperationcode character varying,
    destinationoperationnextdestinationcompanyaddress character varying,
    destinationoperationnextdestinationcompanycontact character varying,
    destinationoperationnextdestinationcompanymail character varying,
    destinationoperationnextdestinationcompanyname character varying,
    destinationoperationnextdestinationcompanyphone character varying,
    destinationoperationnextdestinationcompanysiret character varying,
    destinationoperationnextdestinationcompanyvatnumber character varying,
    destinationoperationsignatureauthor character varying,
    destinationoperationsignaturedate timestamp without time zone,
    destinationplannedoperationcode character varying,
    destinationreceptionacceptationstatus character varying,
    destinationreceptiondate timestamp without time zone,
    destinationreceptionrefusalreason character varying,
    destinationreceptionsignatureauthor character varying,
    destinationreceptionsignaturedate timestamp without time zone,
    destinationreceptionweight double precision,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emittercustominfo character varying,
    emitteremissionsignatureauthor character varying,
    emitteremissionsignaturedate timestamp without time zone,
    forwardingid character varying,
    groupedinid character varying,
    id character varying,
    isdeleted boolean,
    isdraft boolean,
    repackagedinid character varying,
    status character varying,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterrecepissedepartment character varying,
    transporterrecepissenumber character varying,
    transporterrecepissevaliditylimit timestamp without time zone,
    transportertransportmode character varying,
    transportertransportplates jsonb,
    transportertransportsignatureauthor character varying,
    transportertransportsignaturedate timestamp without time zone,
    transportertransporttakenoverat timestamp without time zone,
    type character varying,
    updatedat timestamp without time zone,
    wasteadr character varying,
    wastecode character varying,
    wastedescription character varying,
    weightisestimate boolean,
    weightvalue double precision
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsff_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_bsff_packaging_raw_bsffid; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsff_packaging_raw_bsffid (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    acceptationdate timestamp without time zone,
    acceptationrefusalreason character varying,
    acceptationsignatureauthor character varying,
    acceptationsignaturedate timestamp without time zone,
    acceptationstatus character varying,
    acceptationwastecode character varying,
    acceptationwastedescription character varying,
    acceptationweight double precision,
    bsffid character varying,
    id character varying,
    nextpackagingid character varying,
    numero character varying,
    operationcode character varying,
    operationdate timestamp without time zone,
    operationdescription character varying,
    operationnextdestinationcap character varying,
    operationnextdestinationcompanyaddress character varying,
    operationnextdestinationcompanycontact character varying,
    operationnextdestinationcompanymail character varying,
    operationnextdestinationcompanyname character varying,
    operationnextdestinationcompanyphone character varying,
    operationnextdestinationcompanysiret character varying,
    operationnextdestinationcompanyvatnumber character varying,
    operationnextdestinationplannedoperationcode character varying,
    operationnotraceability boolean,
    operationsignatureauthor character varying,
    operationsignaturedate timestamp without time zone,
    other character varying,
    type character varying,
    volume double precision,
    weight double precision,
    emissionnumero character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsff_packaging_raw_bsffid OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_bsff_packaging_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsff_packaging_raw_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    acceptationdate timestamp without time zone,
    acceptationrefusalreason character varying,
    acceptationsignatureauthor character varying,
    acceptationsignaturedate timestamp without time zone,
    acceptationstatus character varying,
    acceptationwastecode character varying,
    acceptationwastedescription character varying,
    acceptationweight double precision,
    bsffid character varying,
    id character varying,
    nextpackagingid character varying,
    numero character varying,
    operationcode character varying,
    operationdate timestamp without time zone,
    operationdescription character varying,
    operationnextdestinationcap character varying,
    operationnextdestinationcompanyaddress character varying,
    operationnextdestinationcompanycontact character varying,
    operationnextdestinationcompanymail character varying,
    operationnextdestinationcompanyname character varying,
    operationnextdestinationcompanyphone character varying,
    operationnextdestinationcompanysiret character varying,
    operationnextdestinationcompanyvatnumber character varying,
    operationnextdestinationplannedoperationcode character varying,
    operationnotraceability boolean,
    operationsignatureauthor character varying,
    operationsignaturedate timestamp without time zone,
    other character varying,
    type character varying,
    volume double precision,
    weight double precision,
    emissionnumero character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsff_packaging_raw_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_bsff_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsff_raw_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    createdat timestamp without time zone,
    destinationcompanyaddress character varying,
    destinationcompanycontact character varying,
    destinationcompanymail character varying,
    destinationcompanyname character varying,
    destinationcompanyphone character varying,
    destinationcompanysiret character varying,
    destinationcustominfo character varying,
    destinationoperationcode character varying,
    destinationoperationnextdestinationcompanyaddress character varying,
    destinationoperationnextdestinationcompanycontact character varying,
    destinationoperationnextdestinationcompanymail character varying,
    destinationoperationnextdestinationcompanyname character varying,
    destinationoperationnextdestinationcompanyphone character varying,
    destinationoperationnextdestinationcompanysiret character varying,
    destinationoperationnextdestinationcompanyvatnumber character varying,
    destinationoperationsignatureauthor character varying,
    destinationoperationsignaturedate timestamp without time zone,
    destinationplannedoperationcode character varying,
    destinationreceptionacceptationstatus character varying,
    destinationreceptiondate timestamp without time zone,
    destinationreceptionrefusalreason character varying,
    destinationreceptionsignatureauthor character varying,
    destinationreceptionsignaturedate timestamp without time zone,
    destinationreceptionweight double precision,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emittercustominfo character varying,
    emitteremissionsignatureauthor character varying,
    emitteremissionsignaturedate timestamp without time zone,
    forwardingid character varying,
    groupedinid character varying,
    id character varying,
    isdeleted boolean,
    isdraft boolean,
    repackagedinid character varying,
    status character varying,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterrecepissedepartment character varying,
    transporterrecepissenumber character varying,
    transporterrecepissevaliditylimit timestamp without time zone,
    transportertransportmode character varying,
    transportertransportplates jsonb,
    transportertransportsignatureauthor character varying,
    transportertransportsignaturedate timestamp without time zone,
    transportertransporttakenoverat timestamp without time zone,
    type character varying,
    updatedat timestamp without time zone,
    wasteadr character varying,
    wastecode character varying,
    wastedescription character varying,
    weightisestimate boolean,
    weightvalue double precision,
    destinationcap character varying,
    detenteurcompanysirets jsonb
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsff_raw_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_bsvhu_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsvhu_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    createdat timestamp without time zone,
    destinationagrementnumber character varying,
    destinationcompanyaddress character varying,
    destinationcompanycontact character varying,
    destinationcompanymail character varying,
    destinationcompanyname character varying,
    destinationcompanyphone character varying,
    destinationcompanysiret character varying,
    destinationcustominfo character varying,
    destinationoperationcode character varying,
    destinationoperationdate timestamp without time zone,
    destinationoperationnextdestinationcompanyaddress character varying,
    destinationoperationnextdestinationcompanycontact character varying,
    destinationoperationnextdestinationcompanymail character varying,
    destinationoperationnextdestinationcompanyname character varying,
    destinationoperationnextdestinationcompanyphone character varying,
    destinationoperationnextdestinationcompanysiret character varying,
    destinationoperationnextdestinationcompanyvatnumber character varying,
    destinationoperationsignatureauthor character varying,
    destinationoperationsignaturedate timestamp without time zone,
    destinationplannedoperationcode character varying,
    destinationreceptionacceptationstatus character varying,
    destinationreceptiondate timestamp without time zone,
    destinationreceptionidentificationnumbers jsonb,
    destinationreceptionidentificationtype character varying,
    destinationreceptionquantity integer,
    destinationreceptionrefusalreason character varying,
    destinationreceptionweight double precision,
    destinationtype character varying,
    emitteragrementnumber character varying,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emittercustominfo character varying,
    emitteremissionsignatureauthor character varying,
    emitteremissionsignaturedate timestamp without time zone,
    id character varying,
    identificationnumbers jsonb,
    identificationtype character varying,
    isdeleted boolean,
    isdraft boolean,
    packaging character varying,
    quantity integer,
    status character varying,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterrecepissedepartment character varying,
    transporterrecepissenumber character varying,
    transporterrecepissevaliditylimit timestamp without time zone,
    transportertransportplates jsonb,
    transportertransportsignatureauthor character varying,
    transportertransportsignaturedate timestamp without time zone,
    transportertransporttakenoverat timestamp without time zone,
    updatedat timestamp without time zone,
    wastecode character varying,
    weightisestimate boolean,
    weightvalue double precision
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsvhu_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_bsvhu_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsvhu_raw_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    createdat timestamp without time zone,
    destinationagrementnumber character varying,
    destinationcompanyaddress character varying,
    destinationcompanycontact character varying,
    destinationcompanymail character varying,
    destinationcompanyname character varying,
    destinationcompanyphone character varying,
    destinationcompanysiret character varying,
    destinationcustominfo character varying,
    destinationoperationcode character varying,
    destinationoperationdate timestamp without time zone,
    destinationoperationnextdestinationcompanyaddress character varying,
    destinationoperationnextdestinationcompanycontact character varying,
    destinationoperationnextdestinationcompanymail character varying,
    destinationoperationnextdestinationcompanyname character varying,
    destinationoperationnextdestinationcompanyphone character varying,
    destinationoperationnextdestinationcompanysiret character varying,
    destinationoperationnextdestinationcompanyvatnumber character varying,
    destinationoperationsignatureauthor character varying,
    destinationoperationsignaturedate timestamp without time zone,
    destinationplannedoperationcode character varying,
    destinationreceptionacceptationstatus character varying,
    destinationreceptiondate timestamp without time zone,
    destinationreceptionidentificationnumbers jsonb,
    destinationreceptionidentificationtype character varying,
    destinationreceptionquantity integer,
    destinationreceptionrefusalreason character varying,
    destinationreceptionweight double precision,
    destinationtype character varying,
    emitteragrementnumber character varying,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emittercustominfo character varying,
    emitteremissionsignatureauthor character varying,
    emitteremissionsignaturedate timestamp without time zone,
    id character varying,
    identificationnumbers jsonb,
    identificationtype character varying,
    isdeleted boolean,
    isdraft boolean,
    packaging character varying,
    quantity integer,
    status character varying,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterrecepissedepartment character varying,
    transporterrecepissenumber character varying,
    transporterrecepissevaliditylimit timestamp without time zone,
    transportertransportplates jsonb,
    transportertransportsignatureauthor character varying,
    transportertransportsignaturedate timestamp without time zone,
    transportertransporttakenoverat timestamp without time zone,
    updatedat timestamp without time zone,
    wastecode character varying,
    weightisestimate boolean,
    weightvalue double precision,
    transporterrecepisseisexempted boolean
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_bsvhu_raw_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_company_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_company_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    address character varying,
    allowbsdasritakeoverwithoutsignature boolean,
    brokerreceiptid character varying,
    codedepartement character varying,
    codenaf character varying,
    companytypes jsonb,
    contact character varying,
    contactemail character varying,
    contactphone character varying,
    createdat timestamp without time zone,
    ecoorganismeagreements jsonb,
    gerepid character varying,
    givenname character varying,
    id character varying,
    latitude double precision,
    longitude double precision,
    name character varying,
    securitycode integer,
    siret character varying,
    traderreceiptid character varying,
    transporterreceiptid character varying,
    updatedat timestamp without time zone,
    vatnumber character varying,
    verificationcode character varying,
    verificationcomment character varying,
    verificationmode character varying,
    verificationstatus character varying,
    verifiedat timestamp without time zone,
    vhuagrementbroyeurid character varying,
    vhuagrementdemolisseurid character varying,
    website character varying,
    workercertificationid character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_company_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_company_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_company_raw_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    address character varying,
    allowbsdasritakeoverwithoutsignature boolean,
    brokerreceiptid character varying,
    codedepartement character varying,
    codenaf character varying,
    companytypes jsonb,
    contact character varying,
    contactemail character varying,
    contactphone character varying,
    createdat timestamp without time zone,
    ecoorganismeagreements jsonb,
    gerepid character varying,
    givenname character varying,
    id character varying,
    latitude double precision,
    longitude double precision,
    name character varying,
    securitycode integer,
    siret character varying,
    traderreceiptid character varying,
    transporterreceiptid character varying,
    updatedat timestamp without time zone,
    vatnumber character varying,
    verificationcode character varying,
    verificationcomment character varying,
    verificationmode character varying,
    verificationstatus character varying,
    verifiedat timestamp without time zone,
    vhuagrementbroyeurid character varying,
    vhuagrementdemolisseurid character varying,
    website character varying,
    workercertificationid character varying,
    orgid character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_company_raw_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_companyassociation_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_companyassociation_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    companyid character varying,
    id character varying,
    role character varying,
    userid character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_companyassociation_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_eco_organisme_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_eco_organisme_raw_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    address character varying,
    handlebsdasri boolean,
    id character varying,
    name character varying,
    siret character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_eco_organisme_raw_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_trader_receipt_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_trader_receipt_raw_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    department character varying,
    id character varying,
    receiptnumber character varying,
    validitylimit timestamp without time zone
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_trader_receipt_raw_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_user_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_user_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    activatedat timestamp without time zone,
    createdat timestamp without time zone,
    email character varying,
    firstassociationdate timestamp without time zone,
    id character varying,
    isactive boolean,
    isadmin boolean,
    isregistrenational boolean,
    name character varying,
    password character varying,
    phone character varying,
    updatedat timestamp without time zone
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_user_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_user_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_user_raw_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    activatedat timestamp without time zone,
    createdat timestamp without time zone,
    email character varying,
    firstassociationdate timestamp without time zone,
    id character varying,
    isactive boolean,
    isadmin boolean,
    isregistrenational boolean,
    name character varying,
    password character varying,
    phone character varying,
    updatedat timestamp without time zone,
    passwordversion integer
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_user_raw_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_trackdechets_vhu_agrement_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_vhu_agrement_raw_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    agrementnumber character varying,
    department character varying,
    id character varying
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_trackdechets_vhu_agrement_raw_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_zammad_groups_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_zammad_groups_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    active boolean,
    assignment_timeout numeric,
    created_at timestamp without time zone,
    created_by_id numeric,
    email_address_id numeric,
    follow_up_assignment boolean,
    follow_up_possible character varying,
    id numeric,
    name character varying,
    note character varying,
    reopen_time_in_days numeric,
    shared_drafts boolean,
    signature_id numeric,
    updated_at timestamp without time zone,
    updated_by_id numeric,
    user_ids jsonb
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_zammad_groups_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_zammad_tags_ticket_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_zammad_tags_ticket_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    tags jsonb,
    ticket_id numeric
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_zammad_tags_ticket_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_zammad_tickets_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_zammad_tickets_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    article_count numeric,
    article_ids jsonb,
    close_at timestamp without time zone,
    close_diff_in_min numeric,
    close_escalation_at timestamp without time zone,
    close_in_min numeric,
    create_article_sender_id numeric,
    create_article_type_id numeric,
    created_at timestamp without time zone,
    created_by_id numeric,
    customer_id numeric,
    escalation_at timestamp without time zone,
    first_response_at timestamp without time zone,
    first_response_diff_in_min numeric,
    first_response_escalation_at timestamp without time zone,
    first_response_in_min numeric,
    group_id numeric,
    id numeric,
    last_close_at timestamp without time zone,
    last_contact_agent_at timestamp without time zone,
    last_contact_at timestamp without time zone,
    last_contact_customer_at timestamp without time zone,
    last_owner_update_at timestamp without time zone,
    note character varying,
    number character varying,
    organization_id numeric,
    owner_id numeric,
    pending_time character varying,
    priority_id numeric,
    state_id numeric,
    ticket_time_accounting_ids jsonb,
    time_unit character varying,
    title character varying,
    type character varying,
    update_diff_in_min numeric,
    update_escalation_at timestamp without time zone,
    update_in_min numeric,
    updated_at timestamp without time zone,
    updated_by_id numeric,
    preferences jsonb
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_zammad_tickets_id OWNER TO pao;

--
-- Name: source_not_null_raw_zone_zammad_users_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_not_null_raw_zone_zammad_users_id (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    active boolean,
    address character varying,
    authorization_ids jsonb,
    city character varying,
    country character varying,
    created_at timestamp without time zone,
    created_by_id numeric,
    department character varying,
    email character varying,
    fax character varying,
    firstname character varying,
    group_ids jsonb,
    id numeric,
    image character varying,
    image_source character varying,
    karma_user_ids jsonb,
    last_login timestamp without time zone,
    lastname character varying,
    login character varying,
    login_failed numeric,
    mobile character varying,
    note character varying,
    organization_id numeric,
    organization_ids jsonb,
    out_of_office boolean,
    out_of_office_end_at timestamp without time zone,
    out_of_office_replacement_id numeric,
    out_of_office_start_at timestamp without time zone,
    phone character varying,
    role_ids jsonb,
    source character varying,
    street character varying,
    updated_at timestamp without time zone,
    updated_by_id numeric,
    verified boolean,
    vip boolean,
    web character varying,
    zip character varying,
    preferences jsonb
);


ALTER TABLE dbt_test__audit.source_not_null_raw_zone_zammad_users_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_gsheet__6583e7a7389217bab3181552ba66d191; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_gsheet__6583e7a7389217bab3181552ba66d191 (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_gsheet__6583e7a7389217bab3181552ba66d191 OWNER TO pao;

--
-- Name: source_unique_raw_zone_gsheet_collectivites__SIREN_; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit."source_unique_raw_zone_gsheet_collectivites__SIREN_" (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit."source_unique_raw_zone_gsheet_collectivites__SIREN_" OWNER TO pao;

--
-- Name: source_unique_raw_zone_icpe_nomenclature_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_icpe_nomenclature_id (
    unique_field text,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_icpe_nomenclature_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_insee_arrondissement_arr; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_insee_arrondissement_arr (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_insee_arrondissement_arr OWNER TO pao;

--
-- Name: source_unique_raw_zone_insee_canton_id_canton; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_insee_canton_id_canton (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_insee_canton_id_canton OWNER TO pao;

--
-- Name: source_unique_raw_zone_insee_commune_com; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_insee_commune_com (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_insee_commune_com OWNER TO pao;

--
-- Name: source_unique_raw_zone_insee_departement_dep; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_insee_departement_dep (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_insee_departement_dep OWNER TO pao;

--
-- Name: source_unique_raw_zone_insee_naf2008_code_sous_classe; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_insee_naf2008_code_sous_classe (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_insee_naf2008_code_sous_classe OWNER TO pao;

--
-- Name: source_unique_raw_zone_insee_region_reg; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_insee_region_reg (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_insee_region_reg OWNER TO pao;

--
-- Name: source_unique_raw_zone_insee_stock_etablissement_siret; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_insee_stock_etablissement_siret (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_insee_stock_etablissement_siret OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackde_402cb208ba650005e3814f3743999ce2; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackde_402cb208ba650005e3814f3743999ce2 (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackde_402cb208ba650005e3814f3743999ce2 OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackde_70c6d83de7b454223952bb82997e911f; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackde_70c6d83de7b454223952bb82997e911f (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackde_70c6d83de7b454223952bb82997e911f OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_broker_receipt_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_broker_receipt_raw_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_broker_receipt_raw_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_bsda_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsda_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsda_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_bsda_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsda_raw_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsda_raw_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_bsdasri_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsdasri_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsdasri_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_bsdasri_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsdasri_raw_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsdasri_raw_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_bsdd_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsdd_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsdd_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_bsdd_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsdd_raw_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsdd_raw_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_bsff_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsff_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsff_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_bsff_packaging_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsff_packaging_raw_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsff_packaging_raw_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_bsff_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsff_raw_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsff_raw_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_bsvhu_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsvhu_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsvhu_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_bsvhu_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsvhu_raw_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_bsvhu_raw_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_company_association_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_company_association_raw_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_company_association_raw_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_company_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_company_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_company_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_company_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_company_raw_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_company_raw_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_companyassociation_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_companyassociation_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_companyassociation_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_eco_organisme_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_eco_organisme_raw_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_eco_organisme_raw_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_trader_receipt_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_trader_receipt_raw_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_trader_receipt_raw_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_transporter_receipt_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_transporter_receipt_raw_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_transporter_receipt_raw_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_user_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_user_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_user_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_user_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_user_raw_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_user_raw_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_trackdechets_vhu_agrement_raw_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_vhu_agrement_raw_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_trackdechets_vhu_agrement_raw_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_zammad_groups_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_zammad_groups_id (
    unique_field numeric,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_zammad_groups_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_zammad_tickets_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_zammad_tickets_id (
    unique_field numeric,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_zammad_tickets_id OWNER TO pao;

--
-- Name: source_unique_raw_zone_zammad_users_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.source_unique_raw_zone_zammad_users_id (
    unique_field numeric,
    n_records bigint
);


ALTER TABLE dbt_test__audit.source_unique_raw_zone_zammad_users_id OWNER TO pao;

--
-- Name: unique_bsdd_id; Type: TABLE; Schema: dbt_test__audit; Owner: pao
--

CREATE TABLE dbt_test__audit.unique_bsdd_id (
    unique_field character varying,
    n_records bigint
);


ALTER TABLE dbt_test__audit.unique_bsdd_id OWNER TO pao;

--
-- Name: elementary_test_results; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.elementary_test_results (
    id text,
    data_issue_id character varying(4096),
    test_execution_id text,
    test_unique_id text,
    model_unique_id text,
    invocation_id character varying(4096),
    detected_at timestamp without time zone,
    database_name character varying(4096),
    schema_name character varying(4096),
    table_name character varying(4096),
    column_name character varying(4096),
    test_type character varying(4096),
    test_sub_type character varying(4096),
    test_results_description text,
    owners character varying(4096),
    tags character varying(4096),
    test_results_query text,
    other character varying(4096),
    test_name text,
    test_params text,
    severity character varying(4096),
    status character varying(4096),
    failures bigint,
    test_short_name character varying(4096),
    test_alias character varying(4096),
    result_rows text
);


ALTER TABLE elementary.elementary_test_results OWNER TO pao;

--
-- Name: alerts_anomaly_detection; Type: VIEW; Schema: elementary; Owner: pao
--

CREATE VIEW elementary.alerts_anomaly_detection AS
 WITH elementary_test_results AS (
         SELECT elementary_test_results.id,
            elementary_test_results.data_issue_id,
            elementary_test_results.test_execution_id,
            elementary_test_results.test_unique_id,
            elementary_test_results.model_unique_id,
            elementary_test_results.invocation_id,
            elementary_test_results.detected_at,
            elementary_test_results.database_name,
            elementary_test_results.schema_name,
            elementary_test_results.table_name,
            elementary_test_results.column_name,
            elementary_test_results.test_type,
            elementary_test_results.test_sub_type,
            elementary_test_results.test_results_description,
            elementary_test_results.owners,
            elementary_test_results.tags,
            elementary_test_results.test_results_query,
            elementary_test_results.other,
            elementary_test_results.test_name,
            elementary_test_results.test_params,
            elementary_test_results.severity,
            elementary_test_results.status,
            elementary_test_results.failures,
            elementary_test_results.test_short_name,
            elementary_test_results.test_alias,
            elementary_test_results.result_rows
           FROM elementary.elementary_test_results
        ), alerts_anomaly_detection AS (
         SELECT elementary_test_results.id AS alert_id,
            elementary_test_results.data_issue_id,
            elementary_test_results.test_execution_id,
            elementary_test_results.test_unique_id,
            elementary_test_results.model_unique_id,
            elementary_test_results.detected_at,
            elementary_test_results.database_name,
            elementary_test_results.schema_name,
            elementary_test_results.table_name,
            elementary_test_results.column_name,
            elementary_test_results.test_type AS alert_type,
            elementary_test_results.test_sub_type AS sub_type,
            elementary_test_results.test_results_description AS alert_description,
            elementary_test_results.owners,
            elementary_test_results.tags,
            elementary_test_results.test_results_query AS alert_results_query,
            elementary_test_results.other,
            elementary_test_results.test_name,
            elementary_test_results.test_short_name,
            elementary_test_results.test_params,
            elementary_test_results.severity,
            elementary_test_results.status,
            elementary_test_results.result_rows
           FROM elementary_test_results
          WHERE (true AND (lower((elementary_test_results.status)::text) <> 'pass'::text) AND (lower((elementary_test_results.status)::text) <> 'skipped'::text) AND ((elementary_test_results.test_type)::text = 'anomaly_detection'::text))
        )
 SELECT alerts_anomaly_detection.alert_id,
    alerts_anomaly_detection.data_issue_id,
    alerts_anomaly_detection.test_execution_id,
    alerts_anomaly_detection.test_unique_id,
    alerts_anomaly_detection.model_unique_id,
    alerts_anomaly_detection.detected_at,
    alerts_anomaly_detection.database_name,
    alerts_anomaly_detection.schema_name,
    alerts_anomaly_detection.table_name,
    alerts_anomaly_detection.column_name,
    alerts_anomaly_detection.alert_type,
    alerts_anomaly_detection.sub_type,
    alerts_anomaly_detection.alert_description,
    alerts_anomaly_detection.owners,
    alerts_anomaly_detection.tags,
    alerts_anomaly_detection.alert_results_query,
    alerts_anomaly_detection.other,
    alerts_anomaly_detection.test_name,
    alerts_anomaly_detection.test_short_name,
    alerts_anomaly_detection.test_params,
    alerts_anomaly_detection.severity,
    alerts_anomaly_detection.status,
    alerts_anomaly_detection.result_rows
   FROM alerts_anomaly_detection;


ALTER TABLE elementary.alerts_anomaly_detection OWNER TO pao;

--
-- Name: dbt_models; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.dbt_models (
    unique_id character varying(4096),
    alias character varying(4096),
    checksum character varying(4096),
    materialization character varying(4096),
    tags text,
    meta text,
    owner character varying(4096),
    database_name character varying(4096),
    schema_name character varying(4096),
    depends_on_macros text,
    depends_on_nodes text,
    description text,
    name character varying(4096),
    package_name character varying(4096),
    original_path text,
    path character varying(4096),
    generated_at character varying(4096),
    metadata_hash character varying(4096)
);


ALTER TABLE elementary.dbt_models OWNER TO pao;

--
-- Name: dbt_run_results; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.dbt_run_results (
    model_execution_id text,
    unique_id text,
    invocation_id character varying(4096),
    generated_at character varying(4096),
    name text,
    message text,
    status character varying(4096),
    resource_type character varying(4096),
    execution_time double precision,
    execute_started_at character varying(4096),
    execute_completed_at character varying(4096),
    compile_started_at character varying(4096),
    compile_completed_at character varying(4096),
    rows_affected bigint,
    full_refresh boolean,
    compiled_code text,
    failures bigint,
    query_id character varying(4096),
    thread_id character varying(4096)
);


ALTER TABLE elementary.dbt_run_results OWNER TO pao;

--
-- Name: dbt_snapshots; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.dbt_snapshots (
    unique_id character varying(4096),
    alias character varying(4096),
    checksum character varying(4096),
    materialization character varying(4096),
    tags text,
    meta text,
    owner character varying(4096),
    database_name character varying(4096),
    schema_name character varying(4096),
    depends_on_macros text,
    depends_on_nodes text,
    description text,
    name character varying(4096),
    package_name character varying(4096),
    original_path text,
    path character varying(4096),
    generated_at character varying(4096),
    metadata_hash character varying(4096)
);


ALTER TABLE elementary.dbt_snapshots OWNER TO pao;

--
-- Name: model_run_results; Type: VIEW; Schema: elementary; Owner: pao
--

CREATE VIEW elementary.model_run_results AS
 WITH dbt_run_results AS (
         SELECT dbt_run_results.model_execution_id,
            dbt_run_results.unique_id,
            dbt_run_results.invocation_id,
            dbt_run_results.generated_at,
            dbt_run_results.name,
            dbt_run_results.message,
            dbt_run_results.status,
            dbt_run_results.resource_type,
            dbt_run_results.execution_time,
            dbt_run_results.execute_started_at,
            dbt_run_results.execute_completed_at,
            dbt_run_results.compile_started_at,
            dbt_run_results.compile_completed_at,
            dbt_run_results.rows_affected,
            dbt_run_results.full_refresh,
            dbt_run_results.compiled_code,
            dbt_run_results.failures,
            dbt_run_results.query_id,
            dbt_run_results.thread_id
           FROM elementary.dbt_run_results
        ), dbt_models AS (
         SELECT dbt_models.unique_id,
            dbt_models.alias,
            dbt_models.checksum,
            dbt_models.materialization,
            dbt_models.tags,
            dbt_models.meta,
            dbt_models.owner,
            dbt_models.database_name,
            dbt_models.schema_name,
            dbt_models.depends_on_macros,
            dbt_models.depends_on_nodes,
            dbt_models.description,
            dbt_models.name,
            dbt_models.package_name,
            dbt_models.original_path,
            dbt_models.path,
            dbt_models.generated_at,
            dbt_models.metadata_hash
           FROM elementary.dbt_models
        )
 SELECT run_results.model_execution_id,
    run_results.unique_id,
    run_results.invocation_id,
    run_results.query_id,
    run_results.name,
    run_results.generated_at,
    run_results.status,
    run_results.full_refresh,
    run_results.message,
    run_results.execution_time,
    run_results.execute_started_at,
    run_results.execute_completed_at,
    run_results.compile_started_at,
    run_results.compile_completed_at,
    run_results.compiled_code,
    run_results.thread_id,
    models.database_name,
    models.schema_name,
    models.materialization,
    models.tags,
    models.package_name,
    models.path,
    models.original_path,
    models.owner,
    models.alias,
    row_number() OVER (PARTITION BY run_results.unique_id ORDER BY run_results.generated_at DESC) AS model_invocation_reverse_index,
        CASE
            WHEN ((first_value(run_results.invocation_id) OVER (PARTITION BY (date_trunc('day'::text, (run_results.generated_at)::timestamp without time zone)) ORDER BY run_results.generated_at ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING))::text = (run_results.invocation_id)::text) THEN true
            ELSE false
        END AS is_the_first_invocation_of_the_day,
        CASE
            WHEN ((last_value(run_results.invocation_id) OVER (PARTITION BY (date_trunc('day'::text, (run_results.generated_at)::timestamp without time zone)) ORDER BY run_results.generated_at ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING))::text = (run_results.invocation_id)::text) THEN true
            ELSE false
        END AS is_the_last_invocation_of_the_day
   FROM (dbt_run_results run_results
     JOIN dbt_models models ON ((run_results.unique_id = (models.unique_id)::text)));


ALTER TABLE elementary.model_run_results OWNER TO pao;

--
-- Name: snapshot_run_results; Type: VIEW; Schema: elementary; Owner: pao
--

CREATE VIEW elementary.snapshot_run_results AS
 WITH dbt_run_results AS (
         SELECT dbt_run_results.model_execution_id,
            dbt_run_results.unique_id,
            dbt_run_results.invocation_id,
            dbt_run_results.generated_at,
            dbt_run_results.name,
            dbt_run_results.message,
            dbt_run_results.status,
            dbt_run_results.resource_type,
            dbt_run_results.execution_time,
            dbt_run_results.execute_started_at,
            dbt_run_results.execute_completed_at,
            dbt_run_results.compile_started_at,
            dbt_run_results.compile_completed_at,
            dbt_run_results.rows_affected,
            dbt_run_results.full_refresh,
            dbt_run_results.compiled_code,
            dbt_run_results.failures,
            dbt_run_results.query_id,
            dbt_run_results.thread_id
           FROM elementary.dbt_run_results
        ), dbt_snapshots AS (
         SELECT dbt_snapshots.unique_id,
            dbt_snapshots.alias,
            dbt_snapshots.checksum,
            dbt_snapshots.materialization,
            dbt_snapshots.tags,
            dbt_snapshots.meta,
            dbt_snapshots.owner,
            dbt_snapshots.database_name,
            dbt_snapshots.schema_name,
            dbt_snapshots.depends_on_macros,
            dbt_snapshots.depends_on_nodes,
            dbt_snapshots.description,
            dbt_snapshots.name,
            dbt_snapshots.package_name,
            dbt_snapshots.original_path,
            dbt_snapshots.path,
            dbt_snapshots.generated_at,
            dbt_snapshots.metadata_hash
           FROM elementary.dbt_snapshots
        )
 SELECT run_results.model_execution_id,
    run_results.unique_id,
    run_results.invocation_id,
    run_results.query_id,
    run_results.name,
    run_results.generated_at,
    run_results.status,
    run_results.full_refresh,
    run_results.message,
    run_results.execution_time,
    run_results.execute_started_at,
    run_results.execute_completed_at,
    run_results.compile_started_at,
    run_results.compile_completed_at,
    run_results.compiled_code,
    run_results.thread_id,
    snapshots.database_name,
    snapshots.schema_name,
    snapshots.materialization,
    snapshots.tags,
    snapshots.package_name,
    snapshots.path,
    snapshots.original_path,
    snapshots.owner,
    snapshots.alias
   FROM (dbt_run_results run_results
     JOIN dbt_snapshots snapshots ON ((run_results.unique_id = (snapshots.unique_id)::text)));


ALTER TABLE elementary.snapshot_run_results OWNER TO pao;

--
-- Name: alerts_dbt_models; Type: VIEW; Schema: elementary; Owner: pao
--

CREATE VIEW elementary.alerts_dbt_models AS
 WITH error_models AS (
         SELECT model_run_results.model_execution_id,
            model_run_results.unique_id,
            model_run_results.invocation_id,
            model_run_results.name,
            model_run_results.generated_at,
            model_run_results.status,
            model_run_results.full_refresh,
            model_run_results.message,
            model_run_results.execution_time,
            model_run_results.execute_started_at,
            model_run_results.execute_completed_at,
            model_run_results.compile_started_at,
            model_run_results.compile_completed_at,
            model_run_results.compiled_code,
            model_run_results.database_name,
            model_run_results.schema_name,
            model_run_results.materialization,
            model_run_results.tags,
            model_run_results.package_name,
            model_run_results.path,
            model_run_results.original_path,
            model_run_results.owner,
            model_run_results.alias
           FROM elementary.model_run_results
        UNION ALL
         SELECT snapshot_run_results.model_execution_id,
            snapshot_run_results.unique_id,
            snapshot_run_results.invocation_id,
            snapshot_run_results.name,
            snapshot_run_results.generated_at,
            snapshot_run_results.status,
            snapshot_run_results.full_refresh,
            snapshot_run_results.message,
            snapshot_run_results.execution_time,
            snapshot_run_results.execute_started_at,
            snapshot_run_results.execute_completed_at,
            snapshot_run_results.compile_started_at,
            snapshot_run_results.compile_completed_at,
            snapshot_run_results.compiled_code,
            snapshot_run_results.database_name,
            snapshot_run_results.schema_name,
            snapshot_run_results.materialization,
            snapshot_run_results.tags,
            snapshot_run_results.package_name,
            snapshot_run_results.path,
            snapshot_run_results.original_path,
            snapshot_run_results.owner,
            snapshot_run_results.alias
           FROM elementary.snapshot_run_results
        )
 SELECT error_models.model_execution_id AS alert_id,
    error_models.unique_id,
    error_models.generated_at AS detected_at,
    error_models.database_name,
    error_models.materialization,
    error_models.path,
    error_models.original_path,
    error_models.schema_name,
    error_models.message,
    error_models.owner AS owners,
    error_models.tags,
    error_models.alias,
    error_models.status,
    error_models.full_refresh
   FROM error_models
  WHERE (true AND (lower((error_models.status)::text) <> 'success'::text) AND (lower((error_models.status)::text) <> 'skipped'::text));


ALTER TABLE elementary.alerts_dbt_models OWNER TO pao;

--
-- Name: dbt_source_freshness_results; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.dbt_source_freshness_results (
    source_freshness_execution_id character varying(4096),
    unique_id character varying(4096),
    max_loaded_at character varying(4096),
    snapshotted_at character varying(4096),
    generated_at character varying(4096),
    max_loaded_at_time_ago_in_s double precision,
    status character varying(4096),
    error character varying(4096),
    compile_started_at character varying(4096),
    compile_completed_at character varying(4096),
    execute_started_at character varying(4096),
    execute_completed_at character varying(4096),
    invocation_id character varying(4096)
);


ALTER TABLE elementary.dbt_source_freshness_results OWNER TO pao;

--
-- Name: dbt_sources; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.dbt_sources (
    unique_id character varying(4096),
    database_name character varying(4096),
    schema_name character varying(4096),
    source_name character varying(4096),
    name character varying(4096),
    identifier character varying(4096),
    loaded_at_field character varying(4096),
    freshness_warn_after character varying(4096),
    freshness_error_after character varying(4096),
    freshness_filter text,
    relation_name character varying(4096),
    tags text,
    meta text,
    owner character varying(4096),
    package_name character varying(4096),
    original_path text,
    path character varying(4096),
    source_description text,
    description text,
    generated_at character varying(4096),
    metadata_hash character varying(4096)
);


ALTER TABLE elementary.dbt_sources OWNER TO pao;

--
-- Name: alerts_dbt_source_freshness; Type: VIEW; Schema: elementary; Owner: pao
--

CREATE VIEW elementary.alerts_dbt_source_freshness AS
 WITH results AS (
         SELECT dbt_source_freshness_results.source_freshness_execution_id,
            dbt_source_freshness_results.unique_id,
            dbt_source_freshness_results.max_loaded_at,
            dbt_source_freshness_results.snapshotted_at,
            dbt_source_freshness_results.generated_at,
            dbt_source_freshness_results.max_loaded_at_time_ago_in_s,
            dbt_source_freshness_results.status,
            dbt_source_freshness_results.error,
            dbt_source_freshness_results.compile_started_at,
            dbt_source_freshness_results.compile_completed_at,
            dbt_source_freshness_results.execute_started_at,
            dbt_source_freshness_results.execute_completed_at,
            dbt_source_freshness_results.invocation_id
           FROM elementary.dbt_source_freshness_results
        ), sources AS (
         SELECT dbt_sources.unique_id,
            dbt_sources.database_name,
            dbt_sources.schema_name,
            dbt_sources.source_name,
            dbt_sources.name,
            dbt_sources.identifier,
            dbt_sources.loaded_at_field,
            dbt_sources.freshness_warn_after,
            dbt_sources.freshness_error_after,
            dbt_sources.freshness_filter,
            dbt_sources.relation_name,
            dbt_sources.tags,
            dbt_sources.meta,
            dbt_sources.owner,
            dbt_sources.package_name,
            dbt_sources.original_path,
            dbt_sources.path,
            dbt_sources.source_description,
            dbt_sources.description,
            dbt_sources.generated_at,
            dbt_sources.metadata_hash
           FROM elementary.dbt_sources
        )
 SELECT results.source_freshness_execution_id AS alert_id,
    results.max_loaded_at,
    results.snapshotted_at,
    results.generated_at AS detected_at,
    results.max_loaded_at_time_ago_in_s,
    results.status,
    results.error,
    sources.unique_id,
    sources.database_name,
    sources.schema_name,
    sources.source_name,
    sources.identifier,
    sources.freshness_error_after,
    sources.freshness_warn_after,
    sources.freshness_filter,
    sources.tags,
    sources.meta,
    sources.owner,
    sources.package_name,
    sources.path
   FROM (results
     JOIN sources ON (((results.unique_id)::text = (sources.unique_id)::text)))
  WHERE (true AND (lower((results.status)::text) <> 'pass'::text));


ALTER TABLE elementary.alerts_dbt_source_freshness OWNER TO pao;

--
-- Name: alerts_dbt_tests; Type: VIEW; Schema: elementary; Owner: pao
--

CREATE VIEW elementary.alerts_dbt_tests AS
 WITH elementary_test_results AS (
         SELECT elementary_test_results.id,
            elementary_test_results.data_issue_id,
            elementary_test_results.test_execution_id,
            elementary_test_results.test_unique_id,
            elementary_test_results.model_unique_id,
            elementary_test_results.invocation_id,
            elementary_test_results.detected_at,
            elementary_test_results.database_name,
            elementary_test_results.schema_name,
            elementary_test_results.table_name,
            elementary_test_results.column_name,
            elementary_test_results.test_type,
            elementary_test_results.test_sub_type,
            elementary_test_results.test_results_description,
            elementary_test_results.owners,
            elementary_test_results.tags,
            elementary_test_results.test_results_query,
            elementary_test_results.other,
            elementary_test_results.test_name,
            elementary_test_results.test_params,
            elementary_test_results.severity,
            elementary_test_results.status,
            elementary_test_results.failures,
            elementary_test_results.test_short_name,
            elementary_test_results.test_alias,
            elementary_test_results.result_rows
           FROM elementary.elementary_test_results
        ), alerts_dbt_tests AS (
         SELECT elementary_test_results.id AS alert_id,
            elementary_test_results.data_issue_id,
            elementary_test_results.test_execution_id,
            elementary_test_results.test_unique_id,
            elementary_test_results.model_unique_id,
            elementary_test_results.detected_at,
            elementary_test_results.database_name,
            elementary_test_results.schema_name,
            elementary_test_results.table_name,
            elementary_test_results.column_name,
            elementary_test_results.test_type AS alert_type,
            elementary_test_results.test_sub_type AS sub_type,
            elementary_test_results.test_results_description AS alert_description,
            elementary_test_results.owners,
            elementary_test_results.tags,
            elementary_test_results.test_results_query AS alert_results_query,
            elementary_test_results.other,
            elementary_test_results.test_name,
            elementary_test_results.test_short_name,
            elementary_test_results.test_params,
            elementary_test_results.severity,
            elementary_test_results.status,
            elementary_test_results.result_rows
           FROM elementary_test_results
          WHERE (true AND (lower((elementary_test_results.status)::text) <> 'pass'::text) AND (lower((elementary_test_results.status)::text) <> 'skipped'::text) AND ((elementary_test_results.test_type)::text = 'dbt_test'::text))
        )
 SELECT alerts_dbt_tests.alert_id,
    alerts_dbt_tests.data_issue_id,
    alerts_dbt_tests.test_execution_id,
    alerts_dbt_tests.test_unique_id,
    alerts_dbt_tests.model_unique_id,
    alerts_dbt_tests.detected_at,
    alerts_dbt_tests.database_name,
    alerts_dbt_tests.schema_name,
    alerts_dbt_tests.table_name,
    alerts_dbt_tests.column_name,
    alerts_dbt_tests.alert_type,
    alerts_dbt_tests.sub_type,
    alerts_dbt_tests.alert_description,
    alerts_dbt_tests.owners,
    alerts_dbt_tests.tags,
    alerts_dbt_tests.alert_results_query,
    alerts_dbt_tests.other,
    alerts_dbt_tests.test_name,
    alerts_dbt_tests.test_short_name,
    alerts_dbt_tests.test_params,
    alerts_dbt_tests.severity,
    alerts_dbt_tests.status,
    alerts_dbt_tests.result_rows
   FROM alerts_dbt_tests;


ALTER TABLE elementary.alerts_dbt_tests OWNER TO pao;

--
-- Name: alerts_schema_changes; Type: VIEW; Schema: elementary; Owner: pao
--

CREATE VIEW elementary.alerts_schema_changes AS
 WITH elementary_test_results AS (
         SELECT elementary_test_results.id,
            elementary_test_results.data_issue_id,
            elementary_test_results.test_execution_id,
            elementary_test_results.test_unique_id,
            elementary_test_results.model_unique_id,
            elementary_test_results.invocation_id,
            elementary_test_results.detected_at,
            elementary_test_results.database_name,
            elementary_test_results.schema_name,
            elementary_test_results.table_name,
            elementary_test_results.column_name,
            elementary_test_results.test_type,
            elementary_test_results.test_sub_type,
            elementary_test_results.test_results_description,
            elementary_test_results.owners,
            elementary_test_results.tags,
            elementary_test_results.test_results_query,
            elementary_test_results.other,
            elementary_test_results.test_name,
            elementary_test_results.test_params,
            elementary_test_results.severity,
            elementary_test_results.status,
            elementary_test_results.failures,
            elementary_test_results.test_short_name,
            elementary_test_results.test_alias,
            elementary_test_results.result_rows
           FROM elementary.elementary_test_results
        ), alerts_schema_changes AS (
         SELECT elementary_test_results.id AS alert_id,
            elementary_test_results.data_issue_id,
            elementary_test_results.test_execution_id,
            elementary_test_results.test_unique_id,
            elementary_test_results.model_unique_id,
            elementary_test_results.detected_at,
            elementary_test_results.database_name,
            elementary_test_results.schema_name,
            elementary_test_results.table_name,
            elementary_test_results.column_name,
            elementary_test_results.test_type AS alert_type,
            elementary_test_results.test_sub_type AS sub_type,
            elementary_test_results.test_results_description AS alert_description,
            elementary_test_results.owners,
            elementary_test_results.tags,
            elementary_test_results.test_results_query AS alert_results_query,
            elementary_test_results.other,
            elementary_test_results.test_name,
            elementary_test_results.test_short_name,
            elementary_test_results.test_params,
            elementary_test_results.severity,
            elementary_test_results.status,
            elementary_test_results.result_rows
           FROM elementary_test_results
          WHERE (true AND (lower((elementary_test_results.status)::text) <> 'pass'::text) AND (lower((elementary_test_results.status)::text) <> 'skipped'::text) AND ((elementary_test_results.test_type)::text = 'schema_change'::text))
        )
 SELECT alerts_schema_changes.alert_id,
    alerts_schema_changes.data_issue_id,
    alerts_schema_changes.test_execution_id,
    alerts_schema_changes.test_unique_id,
    alerts_schema_changes.model_unique_id,
    alerts_schema_changes.detected_at,
    alerts_schema_changes.database_name,
    alerts_schema_changes.schema_name,
    alerts_schema_changes.table_name,
    alerts_schema_changes.column_name,
    alerts_schema_changes.alert_type,
    alerts_schema_changes.sub_type,
    alerts_schema_changes.alert_description,
    alerts_schema_changes.owners,
    alerts_schema_changes.tags,
    alerts_schema_changes.alert_results_query,
    alerts_schema_changes.other,
    alerts_schema_changes.test_name,
    alerts_schema_changes.test_short_name,
    alerts_schema_changes.test_params,
    alerts_schema_changes.severity,
    alerts_schema_changes.status,
    alerts_schema_changes.result_rows
   FROM alerts_schema_changes;


ALTER TABLE elementary.alerts_schema_changes OWNER TO pao;

--
-- Name: data_monitoring_metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.data_monitoring_metrics (
    id character varying(4096),
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours integer,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.data_monitoring_metrics OWNER TO pao;

--
-- Name: dbt_exposures; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.dbt_exposures (
    unique_id character varying(4096),
    name character varying(4096),
    maturity character varying(4096),
    type character varying(4096),
    owner_email character varying(4096),
    owner_name character varying(4096),
    url text,
    depends_on_macros text,
    depends_on_nodes text,
    description text,
    tags text,
    meta text,
    package_name character varying(4096),
    original_path text,
    path character varying(4096),
    generated_at character varying(4096),
    metadata_hash character varying(4096)
);


ALTER TABLE elementary.dbt_exposures OWNER TO pao;

--
-- Name: dbt_metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.dbt_metrics (
    unique_id character varying(4096),
    name character varying(4096),
    label character varying(4096),
    model character varying(4096),
    type character varying(4096),
    sql text,
    "timestamp" character varying(4096),
    filters text,
    time_grains text,
    dimensions text,
    depends_on_macros text,
    depends_on_nodes text,
    description text,
    tags text,
    meta text,
    package_name character varying(4096),
    original_path text,
    path character varying(4096),
    generated_at character varying(4096),
    metadata_hash character varying(4096)
);


ALTER TABLE elementary.dbt_metrics OWNER TO pao;

--
-- Name: dbt_seeds; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.dbt_seeds (
    unique_id character varying(4096),
    alias character varying(4096),
    checksum character varying(4096),
    tags text,
    meta text,
    owner character varying(4096),
    database_name character varying(4096),
    schema_name character varying(4096),
    description text,
    name character varying(4096),
    package_name character varying(4096),
    original_path text,
    path character varying(4096),
    generated_at character varying(4096),
    metadata_hash character varying(4096)
);


ALTER TABLE elementary.dbt_seeds OWNER TO pao;

--
-- Name: dbt_tests; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.dbt_tests (
    unique_id character varying(4096),
    database_name character varying(4096),
    schema_name character varying(4096),
    name character varying(4096),
    short_name character varying(4096),
    alias character varying(4096),
    test_column_name character varying(4096),
    severity character varying(4096),
    warn_if character varying(4096),
    error_if character varying(4096),
    test_params text,
    test_namespace character varying(4096),
    tags text,
    model_tags text,
    model_owners text,
    meta text,
    depends_on_macros text,
    depends_on_nodes text,
    parent_model_unique_id character varying(4096),
    description text,
    package_name character varying(4096),
    type character varying(4096),
    original_path text,
    path character varying(4096),
    generated_at character varying(4096),
    metadata_hash character varying(4096)
);


ALTER TABLE elementary.dbt_tests OWNER TO pao;

--
-- Name: dbt_artifacts_hashes; Type: VIEW; Schema: elementary; Owner: pao
--

CREATE VIEW elementary.dbt_artifacts_hashes AS
 SELECT 'dbt_models'::text AS artifacts_model,
    dbt_models.metadata_hash
   FROM elementary.dbt_models
UNION ALL
 SELECT 'dbt_tests'::text AS artifacts_model,
    dbt_tests.metadata_hash
   FROM elementary.dbt_tests
UNION ALL
 SELECT 'dbt_sources'::text AS artifacts_model,
    dbt_sources.metadata_hash
   FROM elementary.dbt_sources
UNION ALL
 SELECT 'dbt_snapshots'::text AS artifacts_model,
    dbt_snapshots.metadata_hash
   FROM elementary.dbt_snapshots
UNION ALL
 SELECT 'dbt_metrics'::text AS artifacts_model,
    dbt_metrics.metadata_hash
   FROM elementary.dbt_metrics
UNION ALL
 SELECT 'dbt_exposures'::text AS artifacts_model,
    dbt_exposures.metadata_hash
   FROM elementary.dbt_exposures
UNION ALL
 SELECT 'dbt_seeds'::text AS artifacts_model,
    dbt_seeds.metadata_hash
   FROM elementary.dbt_seeds
  ORDER BY 2;


ALTER TABLE elementary.dbt_artifacts_hashes OWNER TO pao;

--
-- Name: dbt_invocations; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.dbt_invocations (
    invocation_id text,
    job_id text,
    job_name text,
    job_run_id text,
    run_started_at character varying(4096),
    run_completed_at character varying(4096),
    generated_at character varying(4096),
    command character varying(4096),
    dbt_version character varying(4096),
    elementary_version character varying(4096),
    full_refresh boolean,
    invocation_vars text,
    vars text,
    target_name character varying(4096),
    target_database character varying(4096),
    target_schema character varying(4096),
    target_profile_name character varying(4096),
    threads integer,
    selected text,
    yaml_selector text,
    project_id character varying(4096),
    project_name character varying(4096),
    env character varying(4096),
    env_id character varying(4096),
    cause_category character varying(4096),
    cause text,
    pull_request_id character varying(4096),
    git_sha character varying(4096),
    orchestrator character varying(4096),
    dbt_user character varying(4096)
);


ALTER TABLE elementary.dbt_invocations OWNER TO pao;

--
-- Name: filtered_information_schema_columns; Type: VIEW; Schema: elementary; Owner: pao
--

CREATE VIEW elementary.filtered_information_schema_columns AS
 WITH filtered_information_schema_columns AS (
         SELECT upper((((((columns.table_catalog)::text || '.'::text) || (columns.table_schema)::text) || '.'::text) || (columns.table_name)::text)) AS full_table_name,
            upper((columns.table_catalog)::text) AS database_name,
            upper((columns.table_schema)::text) AS schema_name,
            upper((columns.table_name)::text) AS table_name,
            upper((columns.column_name)::text) AS column_name,
            columns.data_type
           FROM information_schema.columns
          WHERE (upper((columns.table_schema)::text) = upper('raw_zone_trackdechets'::text))
        UNION ALL
         SELECT upper((((((columns.table_catalog)::text || '.'::text) || (columns.table_schema)::text) || '.'::text) || (columns.table_name)::text)) AS full_table_name,
            upper((columns.table_catalog)::text) AS database_name,
            upper((columns.table_schema)::text) AS schema_name,
            upper((columns.table_name)::text) AS table_name,
            upper((columns.column_name)::text) AS column_name,
            columns.data_type
           FROM information_schema.columns
          WHERE (upper((columns.table_schema)::text) = upper('trusted_zone_trackdechets'::text))
        )
 SELECT filtered_information_schema_columns.full_table_name,
    filtered_information_schema_columns.database_name,
    filtered_information_schema_columns.schema_name,
    filtered_information_schema_columns.table_name,
    filtered_information_schema_columns.column_name,
    filtered_information_schema_columns.data_type
   FROM filtered_information_schema_columns
  WHERE (filtered_information_schema_columns.full_table_name IS NOT NULL);


ALTER TABLE elementary.filtered_information_schema_columns OWNER TO pao;

--
-- Name: filtered_information_schema_tables; Type: VIEW; Schema: elementary; Owner: pao
--

CREATE VIEW elementary.filtered_information_schema_tables AS
 WITH filtered_information_schema_tables AS (
         WITH empty_table AS (
                 SELECT 'dummy_string'::character varying(4096) AS full_table_name,
                    'dummy_string'::character varying(4096) AS full_schema_name,
                    'dummy_string'::character varying(4096) AS database_name,
                    'dummy_string'::character varying(4096) AS schema_name,
                    'dummy_string'::character varying(4096) AS table_name
                )
         SELECT empty_table.full_table_name,
            empty_table.full_schema_name,
            empty_table.database_name,
            empty_table.schema_name,
            empty_table.table_name
           FROM empty_table
          WHERE (1 = 0)
        )
 SELECT filtered_information_schema_tables.full_table_name,
    filtered_information_schema_tables.full_schema_name,
    filtered_information_schema_tables.database_name,
    filtered_information_schema_tables.schema_name,
    filtered_information_schema_tables.table_name
   FROM filtered_information_schema_tables
  WHERE (filtered_information_schema_tables.schema_name IS NOT NULL);


ALTER TABLE elementary.filtered_information_schema_tables OWNER TO pao;

--
-- Name: job_run_results; Type: VIEW; Schema: elementary; Owner: pao
--

CREATE VIEW elementary.job_run_results AS
 WITH jobs AS (
         SELECT dbt_invocations.job_name,
            dbt_invocations.job_id,
            dbt_invocations.job_run_id,
            min((dbt_invocations.run_started_at)::timestamp without time zone) AS job_run_started_at,
            max((dbt_invocations.run_completed_at)::timestamp without time zone) AS job_run_completed_at,
            ((((((((((((max((dbt_invocations.run_completed_at)::timestamp without time zone))::date - (min((dbt_invocations.run_started_at)::timestamp without time zone))::date) * 24))::double precision + date_part('hour'::text, max((dbt_invocations.run_completed_at)::timestamp without time zone))) - date_part('hour'::text, min((dbt_invocations.run_started_at)::timestamp without time zone))) * (60)::double precision) + date_part('minute'::text, max((dbt_invocations.run_completed_at)::timestamp without time zone))) - date_part('minute'::text, min((dbt_invocations.run_started_at)::timestamp without time zone))) * (60)::double precision) + floor(date_part('second'::text, max((dbt_invocations.run_completed_at)::timestamp without time zone)))) - floor(date_part('second'::text, min((dbt_invocations.run_started_at)::timestamp without time zone)))) AS job_run_execution_time
           FROM elementary.dbt_invocations
          WHERE (dbt_invocations.job_id IS NOT NULL)
          GROUP BY dbt_invocations.job_name, dbt_invocations.job_id, dbt_invocations.job_run_id
        )
 SELECT jobs.job_name AS name,
    jobs.job_id AS id,
    jobs.job_run_id AS run_id,
    jobs.job_run_started_at AS run_started_at,
    jobs.job_run_completed_at AS run_completed_at,
    jobs.job_run_execution_time AS run_execution_time
   FROM jobs;


ALTER TABLE elementary.job_run_results OWNER TO pao;

--
-- Name: metadata; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.metadata (
    dbt_pkg_version text
);


ALTER TABLE elementary.metadata OWNER TO pao;

--
-- Name: metrics_anomaly_score; Type: VIEW; Schema: elementary; Owner: pao
--

CREATE VIEW elementary.metrics_anomaly_score AS
 WITH data_monitoring_metrics AS (
         SELECT data_monitoring_metrics.id,
            data_monitoring_metrics.full_table_name,
            data_monitoring_metrics.column_name,
            data_monitoring_metrics.metric_name,
            data_monitoring_metrics.metric_value,
            data_monitoring_metrics.source_value,
            data_monitoring_metrics.bucket_start,
            data_monitoring_metrics.bucket_end,
            data_monitoring_metrics.bucket_duration_hours,
            data_monitoring_metrics.updated_at,
            data_monitoring_metrics.dimension,
            data_monitoring_metrics.dimension_value,
            data_monitoring_metrics.metric_properties
           FROM elementary.data_monitoring_metrics
        ), time_window_aggregation AS (
         SELECT data_monitoring_metrics.id,
            data_monitoring_metrics.full_table_name,
            data_monitoring_metrics.column_name,
            data_monitoring_metrics.dimension,
            data_monitoring_metrics.dimension_value,
            data_monitoring_metrics.metric_name,
            data_monitoring_metrics.metric_value,
            data_monitoring_metrics.source_value,
            data_monitoring_metrics.bucket_start,
            data_monitoring_metrics.bucket_end,
            data_monitoring_metrics.bucket_duration_hours,
            data_monitoring_metrics.updated_at,
            avg(data_monitoring_metrics.metric_value) OVER (PARTITION BY data_monitoring_metrics.metric_name, data_monitoring_metrics.full_table_name, data_monitoring_metrics.column_name ORDER BY data_monitoring_metrics.bucket_start ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS training_avg,
            stddev(data_monitoring_metrics.metric_value) OVER (PARTITION BY data_monitoring_metrics.metric_name, data_monitoring_metrics.full_table_name, data_monitoring_metrics.column_name ORDER BY data_monitoring_metrics.bucket_start ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS training_stddev,
            count(data_monitoring_metrics.metric_value) OVER (PARTITION BY data_monitoring_metrics.metric_name, data_monitoring_metrics.full_table_name, data_monitoring_metrics.column_name ORDER BY data_monitoring_metrics.bucket_start ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS training_set_size,
            last_value(data_monitoring_metrics.bucket_end) OVER (PARTITION BY data_monitoring_metrics.metric_name, data_monitoring_metrics.full_table_name, data_monitoring_metrics.column_name ORDER BY data_monitoring_metrics.bucket_start ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS training_end,
            first_value(data_monitoring_metrics.bucket_end) OVER (PARTITION BY data_monitoring_metrics.metric_name, data_monitoring_metrics.full_table_name, data_monitoring_metrics.column_name ORDER BY data_monitoring_metrics.bucket_start ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS training_start
           FROM data_monitoring_metrics
          GROUP BY data_monitoring_metrics.id, data_monitoring_metrics.full_table_name, data_monitoring_metrics.column_name, data_monitoring_metrics.dimension, data_monitoring_metrics.dimension_value, data_monitoring_metrics.metric_name, data_monitoring_metrics.metric_value, data_monitoring_metrics.source_value, data_monitoring_metrics.bucket_start, data_monitoring_metrics.bucket_end, data_monitoring_metrics.bucket_duration_hours, data_monitoring_metrics.updated_at
        ), metrics_anomaly_score AS (
         SELECT time_window_aggregation.id,
            time_window_aggregation.full_table_name,
            time_window_aggregation.column_name,
            time_window_aggregation.dimension,
            time_window_aggregation.dimension_value,
            time_window_aggregation.metric_name,
                CASE
                    WHEN (time_window_aggregation.training_stddev IS NULL) THEN NULL::double precision
                    WHEN (time_window_aggregation.training_stddev = (0)::double precision) THEN (0)::double precision
                    ELSE ((time_window_aggregation.metric_value - time_window_aggregation.training_avg) / time_window_aggregation.training_stddev)
                END AS anomaly_score,
            time_window_aggregation.metric_value AS latest_metric_value,
            time_window_aggregation.bucket_start,
            time_window_aggregation.bucket_end,
            time_window_aggregation.training_avg,
            time_window_aggregation.training_stddev,
            time_window_aggregation.training_start,
            time_window_aggregation.training_end,
            time_window_aggregation.training_set_size,
            max(time_window_aggregation.updated_at) AS updated_at
           FROM time_window_aggregation
          WHERE ((time_window_aggregation.metric_value IS NOT NULL) AND (time_window_aggregation.training_avg IS NOT NULL) AND (time_window_aggregation.training_set_size >= 14) AND (time_window_aggregation.bucket_end >= (date_trunc('day'::text, (CURRENT_TIMESTAMP)::timestamp without time zone) + (('-7'::integer)::double precision * '1 day'::interval))))
          GROUP BY time_window_aggregation.id, time_window_aggregation.full_table_name, time_window_aggregation.column_name, time_window_aggregation.dimension, time_window_aggregation.dimension_value, time_window_aggregation.metric_name,
                CASE
                    WHEN (time_window_aggregation.training_stddev IS NULL) THEN NULL::double precision
                    WHEN (time_window_aggregation.training_stddev = (0)::double precision) THEN (0)::double precision
                    ELSE ((time_window_aggregation.metric_value - time_window_aggregation.training_avg) / time_window_aggregation.training_stddev)
                END, time_window_aggregation.metric_value, time_window_aggregation.bucket_start, time_window_aggregation.bucket_end, time_window_aggregation.training_avg, time_window_aggregation.training_stddev, time_window_aggregation.training_start, time_window_aggregation.training_end, time_window_aggregation.training_set_size
          ORDER BY time_window_aggregation.bucket_end DESC
        ), final AS (
         SELECT metrics_anomaly_score.id,
            metrics_anomaly_score.full_table_name,
            metrics_anomaly_score.column_name,
            metrics_anomaly_score.dimension,
            metrics_anomaly_score.dimension_value,
            metrics_anomaly_score.metric_name,
            metrics_anomaly_score.anomaly_score,
            metrics_anomaly_score.latest_metric_value,
            metrics_anomaly_score.bucket_start,
            metrics_anomaly_score.bucket_end,
            metrics_anomaly_score.training_avg,
            metrics_anomaly_score.training_stddev,
            metrics_anomaly_score.training_start,
            metrics_anomaly_score.training_end,
            metrics_anomaly_score.training_set_size,
            metrics_anomaly_score.updated_at,
                CASE
                    WHEN (abs(metrics_anomaly_score.anomaly_score) > (3)::double precision) THEN true
                    ELSE false
                END AS is_anomaly
           FROM metrics_anomaly_score
        )
 SELECT final.id,
    final.full_table_name,
    final.column_name,
    final.dimension,
    final.dimension_value,
    final.metric_name,
    final.anomaly_score,
    final.latest_metric_value,
    final.bucket_start,
    final.bucket_end,
    final.training_avg,
    final.training_stddev,
    final.training_start,
    final.training_end,
    final.training_set_size,
    final.updated_at,
    final.is_anomaly
   FROM final;


ALTER TABLE elementary.metrics_anomaly_score OWNER TO pao;

--
-- Name: monitors_runs; Type: VIEW; Schema: elementary; Owner: pao
--

CREATE VIEW elementary.monitors_runs AS
 WITH data_monitoring_metrics AS (
         SELECT data_monitoring_metrics.id,
            data_monitoring_metrics.full_table_name,
            data_monitoring_metrics.column_name,
            data_monitoring_metrics.metric_name,
            data_monitoring_metrics.metric_value,
            data_monitoring_metrics.source_value,
            data_monitoring_metrics.bucket_start,
            data_monitoring_metrics.bucket_end,
            data_monitoring_metrics.bucket_duration_hours,
            data_monitoring_metrics.updated_at,
            data_monitoring_metrics.dimension,
            data_monitoring_metrics.dimension_value,
            data_monitoring_metrics.metric_properties
           FROM elementary.data_monitoring_metrics
        ), max_bucket_end AS (
         SELECT data_monitoring_metrics.full_table_name,
            data_monitoring_metrics.column_name,
            data_monitoring_metrics.metric_name,
            data_monitoring_metrics.metric_properties,
            max(data_monitoring_metrics.bucket_end) AS last_bucket_end
           FROM data_monitoring_metrics
          GROUP BY data_monitoring_metrics.full_table_name, data_monitoring_metrics.column_name, data_monitoring_metrics.metric_name, data_monitoring_metrics.metric_properties
        )
 SELECT max_bucket_end.full_table_name,
    max_bucket_end.column_name,
    max_bucket_end.metric_name,
    max_bucket_end.metric_properties,
    max_bucket_end.last_bucket_end
   FROM max_bucket_end;


ALTER TABLE elementary.monitors_runs OWNER TO pao;

--
-- Name: schema_columns_snapshot; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.schema_columns_snapshot (
    column_state_id character varying(4096),
    full_column_name character varying(4096),
    full_table_name character varying(4096),
    column_name character varying(4096),
    data_type character varying(4096),
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.schema_columns_snapshot OWNER TO pao;

--
-- Name: test_0481b5c15c_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_0481b5c15c_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_0481b5c15c_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_0481b5c15c_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_0481b5c15c_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_0481b5c15c_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_0545095140_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_0545095140_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_0545095140_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_0545095140_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_0545095140_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_0545095140_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_0afbcd422e_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_0afbcd422e_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_0afbcd422e_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_0afbcd422e_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_0afbcd422e_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_0afbcd422e_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_0fecaf0abc_elementary_column_anomalies_bsd__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_0fecaf0abc_elementary_column_anomalies_bsd__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_0fecaf0abc_elementary_column_anomalies_bsd__anomaly_scores OWNER TO pao;

--
-- Name: test_0fecaf0abc_elementary_column_anomalies_bsdd_max_l__metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_0fecaf0abc_elementary_column_anomalies_bsdd_max_l__metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_0fecaf0abc_elementary_column_anomalies_bsdd_max_l__metrics OWNER TO pao;

--
-- Name: test_120cf321ce_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_120cf321ce_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_120cf321ce_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_120cf321ce_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_120cf321ce_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_120cf321ce_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_1631cbc843_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_1631cbc843_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_1631cbc843_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_1631cbc843_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_1631cbc843_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_1631cbc843_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_1a77f02e39_elementary_table_anomalies_bsda__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_1a77f02e39_elementary_table_anomalies_bsda__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_1a77f02e39_elementary_table_anomalies_bsda__anomaly_scores OWNER TO pao;

--
-- Name: test_1a77f02e39_elementary_table_anomalies_bsda_row_co__metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_1a77f02e39_elementary_table_anomalies_bsda_row_co__metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_1a77f02e39_elementary_table_anomalies_bsda_row_co__metrics OWNER TO pao;

--
-- Name: test_1bb16412a3_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_1bb16412a3_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_1bb16412a3_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_1bb16412a3_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_1bb16412a3_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_1bb16412a3_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_1f1ed6cf33_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_1f1ed6cf33_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_1f1ed6cf33_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_1f1ed6cf33_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_1f1ed6cf33_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_1f1ed6cf33_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_213dec4ec0_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_213dec4ec0_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_213dec4ec0_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_213dec4ec0_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_213dec4ec0_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_213dec4ec0_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_2d42e0399c_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_2d42e0399c_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_2d42e0399c_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_2d42e0399c_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_2d42e0399c_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_2d42e0399c_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_2d8d210c2d_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_2d8d210c2d_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_2d8d210c2d_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_2d8d210c2d_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_2d8d210c2d_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_2d8d210c2d_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_3249df89bd_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_3249df89bd_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_3249df89bd_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_3249df89bd_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_3249df89bd_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_3249df89bd_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_357c6eb732_elementary_schema_change__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_357c6eb732_elementary_schema_change__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_357c6eb732_elementary_schema_change__schema_changes_alerts OWNER TO pao;

--
-- Name: test_357c6eb732_elementary_schema_changes_bsdas__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_357c6eb732_elementary_schema_changes_bsdas__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_357c6eb732_elementary_schema_changes_bsdas__schema_changes OWNER TO pao;

--
-- Name: test_3928eecfaa_elementary_dimension_anomalies___anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_3928eecfaa_elementary_dimension_anomalies___anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying
);


ALTER TABLE elementary.test_3928eecfaa_elementary_dimension_anomalies___anomaly_scores OWNER TO pao;

--
-- Name: test_3928eecfaa_elementary_dimension_anomalies_bsdasri__metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_3928eecfaa_elementary_dimension_anomalies_bsdasri__metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying,
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_3928eecfaa_elementary_dimension_anomalies_bsdasri__metrics OWNER TO pao;

--
-- Name: test_392e31eaf1_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_392e31eaf1_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_392e31eaf1_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_392e31eaf1_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_392e31eaf1_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_392e31eaf1_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_406ebf7211_elementary_dimension_anomalies___anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_406ebf7211_elementary_dimension_anomalies___anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying
);


ALTER TABLE elementary.test_406ebf7211_elementary_dimension_anomalies___anomaly_scores OWNER TO pao;

--
-- Name: test_406ebf7211_elementary_dimension_anomalies_bsdd_st__metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_406ebf7211_elementary_dimension_anomalies_bsdd_st__metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying,
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_406ebf7211_elementary_dimension_anomalies_bsdd_st__metrics OWNER TO pao;

--
-- Name: test_45eb2c837b_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_45eb2c837b_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_45eb2c837b_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_45eb2c837b_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_45eb2c837b_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_45eb2c837b_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_4eab820eea_elementary_schema_change__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_4eab820eea_elementary_schema_change__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_4eab820eea_elementary_schema_change__schema_changes_alerts OWNER TO pao;

--
-- Name: test_4eab820eea_elementary_schema_changes_bsdd___schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_4eab820eea_elementary_schema_changes_bsdd___schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_4eab820eea_elementary_schema_changes_bsdd___schema_changes OWNER TO pao;

--
-- Name: test_4f911abe18_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_4f911abe18_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_4f911abe18_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_4f911abe18_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_4f911abe18_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_4f911abe18_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_4fe46651f2_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_4fe46651f2_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_4fe46651f2_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_4fe46651f2_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_4fe46651f2_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_4fe46651f2_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_51e1955847_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_51e1955847_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_51e1955847_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_51e1955847_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_51e1955847_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_51e1955847_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_542c87076a_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_542c87076a_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_542c87076a_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_542c87076a_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_542c87076a_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_542c87076a_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_63fe1eda6c_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_63fe1eda6c_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_63fe1eda6c_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_63fe1eda6c_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_63fe1eda6c_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_63fe1eda6c_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_66f99df885_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_66f99df885_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_66f99df885_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_66f99df885_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_66f99df885_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_66f99df885_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_6aa082592c_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_6aa082592c_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_6aa082592c_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_6aa082592c_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_6aa082592c_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_6aa082592c_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_72c47d7e40_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_72c47d7e40_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_72c47d7e40_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_72c47d7e40_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_72c47d7e40_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_72c47d7e40_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_74b3c1cc53_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_74b3c1cc53_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_74b3c1cc53_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_74b3c1cc53_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_74b3c1cc53_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_74b3c1cc53_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_74fc01e3ee_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_74fc01e3ee_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_74fc01e3ee_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_74fc01e3ee_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_74fc01e3ee_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_74fc01e3ee_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_781076e5a8_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_781076e5a8_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_781076e5a8_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_781076e5a8_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_781076e5a8_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_781076e5a8_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_890c31425d_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_890c31425d_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_890c31425d_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_890c31425d_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_890c31425d_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_890c31425d_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_8d4f4c71f6_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_8d4f4c71f6_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_8d4f4c71f6_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_8d4f4c71f6_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_8d4f4c71f6_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_8d4f4c71f6_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_93b62605c2_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_93b62605c2_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_93b62605c2_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_93b62605c2_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_93b62605c2_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_93b62605c2_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_96b58abbac_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_96b58abbac_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_96b58abbac_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_96b58abbac_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_96b58abbac_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_96b58abbac_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_987d70a2ca_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_987d70a2ca_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_987d70a2ca_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_987d70a2ca_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_987d70a2ca_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_987d70a2ca_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_9a0a390199_elementary_schema_change__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_9a0a390199_elementary_schema_change__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_9a0a390199_elementary_schema_change__schema_changes_alerts OWNER TO pao;

--
-- Name: test_9a0a390199_elementary_schema_changes_bsda___schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_9a0a390199_elementary_schema_changes_bsda___schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_9a0a390199_elementary_schema_changes_bsda___schema_changes OWNER TO pao;

--
-- Name: test_9a7ca17390_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_9a7ca17390_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_9a7ca17390_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_9a7ca17390_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_9a7ca17390_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_9a7ca17390_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_a5fd4cab01_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_a5fd4cab01_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_a5fd4cab01_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_a5fd4cab01_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_a5fd4cab01_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_a5fd4cab01_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_a7645c41f7_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_a7645c41f7_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_a7645c41f7_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_a7645c41f7_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_a7645c41f7_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_a7645c41f7_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_baf14b07a5_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_baf14b07a5_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_baf14b07a5_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_baf14b07a5_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_baf14b07a5_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_baf14b07a5_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_c048c83e46_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_c048c83e46_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_c048c83e46_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_c048c83e46_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_c048c83e46_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_c048c83e46_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_c1d86f6621_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_c1d86f6621_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_c1d86f6621_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_c1d86f6621_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_c1d86f6621_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_c1d86f6621_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_c5d519418f_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_c5d519418f_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_c5d519418f_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_c5d519418f_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_c5d519418f_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_c5d519418f_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_c9498206b4_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_c9498206b4_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_c9498206b4_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_c9498206b4_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_c9498206b4_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_c9498206b4_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_d008f99e48_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_d008f99e48_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_d008f99e48_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_d008f99e48_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_d008f99e48_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_d008f99e48_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_db4e54a62e_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_db4e54a62e_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_db4e54a62e_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_db4e54a62e_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_db4e54a62e_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_db4e54a62e_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_dbca41b85f_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_dbca41b85f_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_dbca41b85f_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_dbca41b85f_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_dbca41b85f_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_dbca41b85f_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_dc6207feaa_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_dc6207feaa_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_dc6207feaa_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_dc6207feaa_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_dc6207feaa_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_dc6207feaa_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_ddd3a0020c_elementary_table_anomalies_bsdd__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_ddd3a0020c_elementary_table_anomalies_bsdd__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_ddd3a0020c_elementary_table_anomalies_bsdd__anomaly_scores OWNER TO pao;

--
-- Name: test_ddd3a0020c_elementary_table_anomalies_bsdd_row_co__metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_ddd3a0020c_elementary_table_anomalies_bsdd_row_co__metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_ddd3a0020c_elementary_table_anomalies_bsdd_row_co__metrics OWNER TO pao;

--
-- Name: test_e08d1caba4_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_e08d1caba4_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_e08d1caba4_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_e08d1caba4_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_e08d1caba4_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_e08d1caba4_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_e2fd347abb_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_e2fd347abb_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_e2fd347abb_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_e2fd347abb_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_e2fd347abb_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_e2fd347abb_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_e337aa1698_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_e337aa1698_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_e337aa1698_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_e337aa1698_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_e337aa1698_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_e337aa1698_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_e4b2a15d9c_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_e4b2a15d9c_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_e4b2a15d9c_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_e4b2a15d9c_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_e4b2a15d9c_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_e4b2a15d9c_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_e587b1bb59_elementary_dimension_anomalies___anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_e587b1bb59_elementary_dimension_anomalies___anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying
);


ALTER TABLE elementary.test_e587b1bb59_elementary_dimension_anomalies___anomaly_scores OWNER TO pao;

--
-- Name: test_e587b1bb59_elementary_dimension_anomalies_bsda_st__metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_e587b1bb59_elementary_dimension_anomalies_bsda_st__metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying,
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_e587b1bb59_elementary_dimension_anomalies_bsda_st__metrics OWNER TO pao;

--
-- Name: test_e6f99b5594_elementary_table_anomalies_bsda__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_e6f99b5594_elementary_table_anomalies_bsda__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_e6f99b5594_elementary_table_anomalies_bsda__anomaly_scores OWNER TO pao;

--
-- Name: test_e6f99b5594_elementary_table_anomalies_bsdasri_row__metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_e6f99b5594_elementary_table_anomalies_bsdasri_row__metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_e6f99b5594_elementary_table_anomalies_bsdasri_row__metrics OWNER TO pao;

--
-- Name: test_eb8235898f_elementary_source_schema__schema_changes_alerts; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_eb8235898f_elementary_source_schema__schema_changes_alerts (
    id text COLLATE pg_catalog."C",
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    data_issue_id text COLLATE pg_catalog."C",
    detected_at timestamp without time zone,
    database_name text COLLATE pg_catalog."C",
    schema_name text COLLATE pg_catalog."C",
    table_name text COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    test_type text,
    test_sub_type text,
    test_results_description text COLLATE pg_catalog."C"
);


ALTER TABLE elementary.test_eb8235898f_elementary_source_schema__schema_changes_alerts OWNER TO pao;

--
-- Name: test_eb8235898f_elementary_source_schema_change__schema_changes; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_eb8235898f_elementary_source_schema_change__schema_changes (
    column_state_id character varying(4096) COLLATE pg_catalog."C",
    full_column_name character varying(4096) COLLATE pg_catalog."C",
    full_table_name character varying(4096) COLLATE pg_catalog."C",
    column_name character varying(4096) COLLATE pg_catalog."C",
    data_type character varying(4096) COLLATE pg_catalog."C",
    is_new boolean,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_eb8235898f_elementary_source_schema_change__schema_changes OWNER TO pao;

--
-- Name: test_f7be3f8274_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_f7be3f8274_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_f7be3f8274_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_f7be3f8274_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_f7be3f8274_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_f7be3f8274_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_fe018f58b6_elementary_source_table_anomali__anomaly_scores; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_fe018f58b6_elementary_source_table_anomali__anomaly_scores (
    id text,
    metric_id character varying,
    test_execution_id character varying(4096),
    test_unique_id character varying(4096),
    detected_at timestamp without time zone,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    anomaly_score double precision,
    anomaly_score_threshold integer,
    anomalous_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    metric_value double precision,
    min_metric_value double precision,
    max_metric_value double precision,
    training_avg double precision,
    training_stddev double precision,
    training_set_size bigint,
    training_start timestamp without time zone,
    training_end timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096)
);


ALTER TABLE elementary.test_fe018f58b6_elementary_source_table_anomali__anomaly_scores OWNER TO pao;

--
-- Name: test_fe018f58b6_elementary_source_table_anomalies_raw___metrics; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_fe018f58b6_elementary_source_table_anomalies_raw___metrics (
    id text,
    full_table_name character varying(4096),
    column_name character varying(4096),
    metric_name character varying(4096),
    metric_value double precision,
    source_value character varying(4096),
    bucket_start timestamp without time zone,
    bucket_end timestamp without time zone,
    bucket_duration_hours double precision,
    updated_at timestamp without time zone,
    dimension character varying(4096),
    dimension_value character varying(4096),
    metric_properties character varying(4096)
);


ALTER TABLE elementary.test_fe018f58b6_elementary_source_table_anomalies_raw___metrics OWNER TO pao;

--
-- Name: test_result_rows; Type: TABLE; Schema: elementary; Owner: pao
--

CREATE TABLE elementary.test_result_rows (
    elementary_test_results_id text,
    result_row text,
    detected_at timestamp without time zone
);


ALTER TABLE elementary.test_result_rows OWNER TO pao;

--
-- Name: codes_operations_traitements; Type: TABLE; Schema: raw_zone; Owner: pao
--

CREATE TABLE raw_zone.codes_operations_traitements (
    code character varying(8),
    description character varying(256)
);


ALTER TABLE raw_zone.codes_operations_traitements OWNER TO pao;

--
-- Name: laposte_hexasmal; Type: TABLE; Schema: raw_zone; Owner: pao
--

CREATE TABLE raw_zone.laposte_hexasmal (
    code_commune_insee character varying,
    nom_commune character varying,
    code_postal integer,
    ligne_5 character varying,
    "libellé_d_acheminement" character varying,
    coordonnees_gps character varying
);


ALTER TABLE raw_zone.laposte_hexasmal OWNER TO pao;

--
-- Name: collectivites_compentence_dechets; Type: TABLE; Schema: raw_zone_gsheet; Owner: pao
--

CREATE TABLE raw_zone_gsheet.collectivites_compentence_dechets (
    dep_epci character varying,
    siren_epci character varying,
    nom_complet character varying,
    nj_epci2023 character varying,
    fisc_epci2023 character varying,
    nb_com_2023 integer,
    ptot_epci_2023 integer,
    pmun_epci_2023 integer
);


ALTER TABLE raw_zone_gsheet.collectivites_compentence_dechets OWNER TO pao;

--
-- Name: coordonnees-epci-fp-2022-last; Type: TABLE; Schema: raw_zone_gsheet; Owner: pao
--

CREATE TABLE raw_zone_gsheet."coordonnees-epci-fp-2022-last" (
    "Région siège" character varying(500),
    "Département siège" character varying(500),
    "Arrondissement siège" character varying(500),
    "Commune siège" character varying(500),
    "SIREN" character varying,
    "Nom du groupement" character varying(500),
    "Nature juridique" character varying(500),
    "Syndicat à la carte" integer,
    "Groupement interdépartemental" integer,
    "Date de création" character varying(500),
    "Date d'effet" character varying(500),
    "Mode de répartition des sièges" character varying(500),
    "Autre mode de répartition des sièges" character varying(2048),
    "Nombre de membres" integer,
    population integer,
    "Nombre de compétences exercées" integer,
    "Mode de financement" character varying(500),
    "DGF Bonifiée" integer,
    dsc integer,
    reom integer,
    "Autre redevance" character varying(500),
    teom integer,
    "Autre taxe" character varying(500),
    "Civilité Président" character varying(500),
    "Prénom Président" character varying(500),
    "Nom Président" character varying(500),
    "Adresse du siège_1" character varying(500),
    "Adresse du siège_2" character varying(500),
    "Adresse du siège_3" character varying(500),
    "Code postal du siège - Ville du siège" character varying(500),
    "Téléphone du siège" character varying(500),
    "Fax du siège" character varying(500),
    "Courriel du siège" character varying(500),
    "Site internet" character varying(500),
    "Adresse annexe_1" character varying(500),
    "Adresse annexe_2" character varying(500),
    "Adresse annexe_3" character varying(500),
    "Code postal annexe - Ville annexe" character varying(500),
    "Téléphone annexe" character varying(500),
    "Fax annexe" character varying(500)
);


ALTER TABLE raw_zone_gsheet."coordonnees-epci-fp-2022-last" OWNER TO pao;

--
-- Name: eco_organismes_agrees_2022; Type: TABLE; Schema: raw_zone_gsheet; Owner: pao
--

CREATE TABLE raw_zone_gsheet.eco_organismes_agrees_2022 (
    siret text,
    raison_sociale text,
    nom_eco_organisme text,
    filiere_dsrep text,
    produits_relevant_filiere_responsabilite_elargie text,
    adresse text,
    code_postal text,
    ville text
);


ALTER TABLE raw_zone_gsheet.eco_organismes_agrees_2022 OWNER TO pao;

--
-- Name: gerep_2016_2017_producteurs; Type: TABLE; Schema: raw_zone_gsheet; Owner: pao
--

CREATE TABLE raw_zone_gsheet.gerep_2016_2017_producteurs (
    annee character varying,
    code_etablissement character varying,
    nom_etablissement character varying,
    adresse_site_exploitation character varying,
    code_postal_etablissement character varying,
    commune character varying,
    code_insee character varying,
    code_ape character varying,
    numero_siret character varying,
    nom_contact character varying,
    fonction_contact character varying,
    tel_contact character varying,
    mail_contact character varying,
    code_dechet_produit character varying,
    dechet_produit character varying
);


ALTER TABLE raw_zone_gsheet.gerep_2016_2017_producteurs OWNER TO pao;

--
-- Name: gerep_2016_2017_traiteurs; Type: TABLE; Schema: raw_zone_gsheet; Owner: pao
--

CREATE TABLE raw_zone_gsheet.gerep_2016_2017_traiteurs (
    annee character varying,
    code_etablissement character varying,
    nom_etablissement character varying,
    adresse_site_exploitation character varying,
    code_postal_etablissement character varying,
    commune character varying,
    code_insee character varying,
    numero_siret character varying,
    code_ape character varying,
    nom_contact character varying,
    tel_contact character varying,
    fonction_contact character varying,
    mail_contact character varying,
    code_dechet_traite character varying,
    dechet_traite character varying
);


ALTER TABLE raw_zone_gsheet.gerep_2016_2017_traiteurs OWNER TO pao;

--
-- Name: ic_etablissement; Type: TABLE; Schema: raw_zone_icpe; Owner: pao
--

CREATE TABLE raw_zone_icpe.ic_etablissement (
    "codeS3ic" text,
    "s3icNumeroSiret" text,
    x text,
    y text,
    region text,
    "nomEts" text,
    "codeCommuneEtablissement" text,
    "codePostal" text,
    "etatActivite" text,
    "codeApe" text,
    "nomCommune" text,
    seveso text,
    regime text,
    "prioriteNationale" text,
    ippc text,
    "declarationAnnuelle" text,
    "familleIc" text,
    "baseIdService" text,
    "natureIdService" text,
    adresse1 text,
    adresse2 text,
    "dateInspection" text,
    "indicationSsp" text,
    rayon text,
    "precisionPositionnement" text,
    inserted_at timestamp without time zone
);


ALTER TABLE raw_zone_icpe.ic_etablissement OWNER TO pao;

--
-- Name: ic_installation_classee; Type: TABLE; Schema: raw_zone_icpe; Owner: pao
--

CREATE TABLE raw_zone_icpe.ic_installation_classee (
    "codeS3ic" text,
    id text,
    volume text,
    unite text,
    date_debut_exploitation text,
    date_fin_validite text,
    statut_ic text,
    id_ref_nomencla_ic text,
    inserted_at timestamp without time zone
);


ALTER TABLE raw_zone_icpe.ic_installation_classee OWNER TO pao;

--
-- Name: ic_ref_nomenclature_ic; Type: TABLE; Schema: raw_zone_icpe; Owner: pao
--

CREATE TABLE raw_zone_icpe.ic_ref_nomenclature_ic (
    id text,
    rubrique_ic text,
    famille_ic text,
    sfamille_ic text,
    ssfamille_ic text,
    alinea text,
    libellecourt_activite text,
    id_regime text,
    envigueur text,
    ippc text,
    inserted_at timestamp without time zone
);


ALTER TABLE raw_zone_icpe.ic_ref_nomenclature_ic OWNER TO pao;

--
-- Name: arrondissement; Type: TABLE; Schema: raw_zone_insee; Owner: pao
--

CREATE TABLE raw_zone_insee.arrondissement (
    arr character varying,
    dep character varying,
    reg character varying,
    cheflieu character varying,
    tncc character varying,
    ncc character varying,
    nccenr character varying,
    libelle character varying
);


ALTER TABLE raw_zone_insee.arrondissement OWNER TO pao;

--
-- Name: canton; Type: TABLE; Schema: raw_zone_insee; Owner: pao
--

CREATE TABLE raw_zone_insee.canton (
    id_canton character varying,
    id_departement character varying,
    id_region character varying,
    typct character varying,
    burcentral character varying,
    tncc character varying,
    ncc character varying,
    nccenr character varying,
    libelle character varying,
    actual character varying
);


ALTER TABLE raw_zone_insee.canton OWNER TO pao;

--
-- Name: commune; Type: TABLE; Schema: raw_zone_insee; Owner: pao
--

CREATE TABLE raw_zone_insee.commune (
    typecom character varying,
    com character varying,
    reg character varying,
    dep character varying,
    ctcd character varying,
    arr character varying,
    tncc character varying,
    ncc character varying,
    nccenr character varying,
    libelle character varying,
    can character varying,
    comparent character varying
);


ALTER TABLE raw_zone_insee.commune OWNER TO pao;

--
-- Name: departement; Type: TABLE; Schema: raw_zone_insee; Owner: pao
--

CREATE TABLE raw_zone_insee.departement (
    dep character varying,
    reg character varying,
    cheflieu character varying,
    tncc character varying,
    ncc character varying,
    nccenr character varying,
    libelle character varying
);


ALTER TABLE raw_zone_insee.departement OWNER TO pao;

--
-- Name: naf2008; Type: TABLE; Schema: raw_zone_insee; Owner: pao
--

CREATE TABLE raw_zone_insee.naf2008 (
    code_section character varying,
    libelle_section character varying,
    code_division character varying,
    libelle_division character varying,
    code_groupe character varying,
    libelle_groupe character varying,
    code_classe character varying,
    libelle_classe character varying,
    code_sous_classe character varying,
    libelle_sous_classe character varying
);


ALTER TABLE raw_zone_insee.naf2008 OWNER TO pao;

--
-- Name: pays; Type: TABLE; Schema: raw_zone_insee; Owner: pao
--

CREATE TABLE raw_zone_insee.pays (
    cog character varying,
    actual character varying,
    capay character varying,
    crpay character varying,
    ani character varying,
    libcog character varying,
    libenr character varying,
    ancnom character varying,
    codeiso2 character varying,
    codeiso3 character varying,
    codenum3 character varying
);


ALTER TABLE raw_zone_insee.pays OWNER TO pao;

--
-- Name: region; Type: TABLE; Schema: raw_zone_insee; Owner: pao
--

CREATE TABLE raw_zone_insee.region (
    reg character varying,
    cheflieu character varying,
    tncc character varying,
    ncc character varying,
    nccenr character varying,
    libelle character varying
);


ALTER TABLE raw_zone_insee.region OWNER TO pao;

--
-- Name: stock_etablissement; Type: TABLE; Schema: raw_zone_insee; Owner: pao
--

CREATE TABLE raw_zone_insee.stock_etablissement (
    siren character varying,
    nic character varying,
    siret character varying,
    "statutDiffusionEtablissement" character varying,
    "dateCreationEtablissement" character varying,
    "trancheEffectifsEtablissement" character varying,
    "anneeEffectifsEtablissement" character varying,
    "activitePrincipaleRegistreMetiersEtablissement" character varying,
    "dateDernierTraitementEtablissement" character varying,
    "etablissementSiege" character varying,
    "nombrePeriodesEtablissement" character varying,
    "complementAdresseEtablissement" character varying,
    "numeroVoieEtablissement" character varying,
    "indiceRepetitionEtablissement" character varying,
    "typeVoieEtablissement" character varying,
    "libelleVoieEtablissement" character varying,
    "codePostalEtablissement" character varying,
    "libelleCommuneEtablissement" character varying,
    "libelleCommuneEtrangerEtablissement" character varying,
    "distributionSpecialeEtablissement" character varying,
    "codeCommuneEtablissement" character varying,
    "codeCedexEtablissement" character varying,
    "libelleCedexEtablissement" character varying,
    "codePaysEtrangerEtablissement" character varying,
    "libellePaysEtrangerEtablissement" character varying,
    "complementAdresse2Etablissement" character varying,
    "numeroVoie2Etablissement" character varying,
    "indiceRepetition2Etablissement" character varying,
    "typeVoie2Etablissement" character varying,
    "libelleVoie2Etablissement" character varying,
    "codePostal2Etablissement" character varying,
    "libelleCommune2Etablissement" character varying,
    "libelleCommuneEtranger2Etablissement" character varying,
    "distributionSpeciale2Etablissement" character varying,
    "codeCommune2Etablissement" character varying,
    "codeCedex2Etablissement" character varying,
    "libelleCedex2Etablissement" character varying,
    "codePaysEtranger2Etablissement" character varying,
    "libellePaysEtranger2Etablissement" character varying,
    "dateDebut" character varying,
    "etatAdministratifEtablissement" character varying,
    "enseigne1Etablissement" character varying,
    "enseigne2Etablissement" character varying,
    "enseigne3Etablissement" character varying,
    "denominationUsuelleEtablissement" character varying,
    "activitePrincipaleEtablissement" character varying,
    "nomenclatureActivitePrincipaleEtablissement" character varying,
    "caractereEmployeurEtablissement" character varying
);


ALTER TABLE raw_zone_insee.stock_etablissement OWNER TO pao;

--
-- Name: brokerreceipt; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.brokerreceipt (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    department character varying,
    id character varying NOT NULL,
    receiptnumber character varying,
    validitylimit timestamp without time zone
);


ALTER TABLE raw_zone_trackdechets.brokerreceipt OWNER TO pao;

--
-- Name: bsda; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.bsda (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    brokercompanyaddress character varying,
    brokercompanycontact character varying,
    brokercompanymail character varying,
    brokercompanyname character varying,
    brokercompanyphone character varying,
    brokercompanysiret character varying,
    brokerrecepissedepartment character varying,
    brokerrecepissenumber character varying,
    brokerrecepissevaliditylimit timestamp without time zone,
    createdat timestamp without time zone,
    destinationcap character varying,
    destinationcompanyaddress character varying,
    destinationcompanycontact character varying,
    destinationcompanymail character varying,
    destinationcompanyname character varying,
    destinationcompanyphone character varying,
    destinationcompanysiret character varying,
    destinationcustominfo character varying,
    destinationoperationcode character varying,
    destinationoperationdate timestamp without time zone,
    destinationoperationdescription character varying,
    destinationoperationnextdestinationcap character varying,
    destinationoperationnextdestinationcompanyaddress character varying,
    destinationoperationnextdestinationcompanycontact character varying,
    destinationoperationnextdestinationcompanymail character varying,
    destinationoperationnextdestinationcompanyname character varying,
    destinationoperationnextdestinationcompanyphone character varying,
    destinationoperationnextdestinationcompanysiret character varying,
    destinationoperationnextdestinationcompanyvatnumber character varying,
    destinationoperationnextdestinationplannedoperationcode character varying,
    destinationoperationsignatureauthor character varying,
    destinationoperationsignaturedate timestamp without time zone,
    destinationplannedoperationcode character varying,
    destinationreceptionacceptationstatus character varying,
    destinationreceptiondate timestamp without time zone,
    destinationreceptionrefusalreason character varying,
    destinationreceptionweight double precision,
    ecoorganismename character varying,
    ecoorganismesiret character varying,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emittercustominfo character varying,
    emitteremissionsignatureauthor character varying,
    emitteremissionsignaturedate timestamp without time zone,
    emitterisprivateindividual boolean,
    emitterpickupsiteaddress character varying,
    emitterpickupsitecity character varying,
    emitterpickupsiteinfos character varying,
    emitterpickupsitename character varying,
    emitterpickupsitepostalcode character varying,
    forwardingid character varying,
    groupedinid character varying,
    id character varying NOT NULL,
    isdeleted boolean,
    isdraft boolean,
    packagings jsonb,
    repackagedinid character varying,
    status character varying,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterrecepissedepartment character varying,
    transporterrecepisseisexempted boolean,
    transporterrecepissenumber character varying,
    transporterrecepissevaliditylimit timestamp without time zone,
    transportertransportmode character varying,
    transportertransportplates jsonb,
    transportertransportsignatureauthor character varying,
    transportertransportsignaturedate timestamp without time zone,
    transportertransporttakenoverat timestamp without time zone,
    type character varying,
    updatedat timestamp without time zone,
    wasteadr character varying,
    wastecode character varying,
    wasteconsistence character varying,
    wastefamilycode character varying,
    wastematerialname character varying,
    wastepop boolean,
    wastesealnumbers jsonb,
    weightisestimate boolean,
    weightvalue double precision,
    workercompanyaddress character varying,
    workercompanycontact character varying,
    workercompanymail character varying,
    workercompanyname character varying,
    workercompanyphone character varying,
    workercompanysiret character varying,
    workerisdisabled boolean,
    workerworkhasemitterpapersignature boolean,
    workerworksignatureauthor character varying,
    workerworksignaturedate timestamp without time zone,
    workercertificationcertificationnumber character varying,
    workercertificationhassubsectionfour boolean,
    workercertificationhassubsectionthree boolean,
    workercertificationorganisation character varying,
    workercertificationvaliditylimit timestamp without time zone,
    intermediariesorgids jsonb
);


ALTER TABLE raw_zone_trackdechets.bsda OWNER TO pao;

--
-- Name: bsdarevisionrequest; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.bsdarevisionrequest (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    authoringcompanyid character varying,
    brokercompanyaddress character varying,
    brokercompanycontact character varying,
    brokercompanymail character varying,
    brokercompanyname character varying,
    brokercompanyphone character varying,
    brokercompanysiret character varying,
    brokerrecepissedepartment character varying,
    brokerrecepissenumber character varying,
    brokerrecepissevaliditylimit timestamp without time zone,
    bsdaid character varying,
    comment character varying,
    createdat timestamp without time zone,
    destinationcap character varying,
    destinationoperationcode character varying,
    destinationoperationdescription character varying,
    destinationreceptionweight double precision,
    emitterpickupsiteaddress character varying,
    emitterpickupsitecity character varying,
    emitterpickupsiteinfos character varying,
    emitterpickupsitename character varying,
    emitterpickupsitepostalcode character varying,
    id character varying NOT NULL,
    packagings jsonb,
    status character varying,
    updatedat timestamp without time zone,
    wastecode character varying,
    wastematerialname character varying,
    wastepop boolean,
    wastesealnumbers jsonb,
    iscanceled boolean
);


ALTER TABLE raw_zone_trackdechets.bsdarevisionrequest OWNER TO pao;

--
-- Name: bsdasri; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.bsdasri (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    createdat timestamp without time zone,
    destinationcompanyaddress character varying,
    destinationcompanycontact character varying,
    destinationcompanymail character varying,
    destinationcompanyname character varying,
    destinationcompanyphone character varying,
    destinationcompanysiret character varying,
    destinationcustominfo character varying,
    destinationoperationcode character varying,
    destinationoperationdate timestamp without time zone,
    destinationoperationsignatureauthor character varying,
    destinationoperationsignaturedate timestamp without time zone,
    destinationreceptionacceptationstatus character varying,
    destinationreceptiondate timestamp without time zone,
    destinationreceptionsignatureauthor character varying,
    destinationreceptionsignaturedate timestamp without time zone,
    destinationreceptionwasterefusalreason character varying,
    destinationreceptionwasterefusedweightvalue double precision,
    destinationreceptionwastevolume double precision,
    destinationreceptionwasteweightvalue double precision,
    destinationwastepackagings jsonb,
    ecoorganismename character varying,
    ecoorganismesiret character varying,
    emissionsignatoryid character varying,
    emittedbyecoorganisme boolean,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emittercustominfo character varying,
    emitteremissionsignatureauthor character varying,
    emitteremissionsignaturedate timestamp without time zone,
    emitterpickupsiteaddress character varying,
    emitterpickupsitecity character varying,
    emitterpickupsiteinfos character varying,
    emitterpickupsitename character varying,
    emitterpickupsitepostalcode character varying,
    emitterwastepackagings jsonb,
    emitterwastevolume double precision,
    emitterwasteweightisestimate boolean,
    emitterwasteweightvalue double precision,
    groupedinid character varying,
    handedovertorecipientat timestamp without time zone,
    id character varying NOT NULL,
    identificationnumbers jsonb,
    isdeleted boolean,
    isdraft boolean,
    isemissiondirecttakenover boolean,
    isemissiontakenoverwithsecretcode boolean,
    operationsignatoryid character varying,
    receptionsignatoryid character varying,
    status character varying,
    synthesizedinid character varying,
    transportsignatoryid character varying,
    transporteracceptationstatus character varying,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterrecepissedepartment character varying,
    transporterrecepissenumber character varying,
    transporterrecepissevaliditylimit timestamp without time zone,
    transportertakenoverat timestamp without time zone,
    transportertransportmode character varying,
    transportertransportplates jsonb,
    transportertransportsignatureauthor character varying,
    transportertransportsignaturedate timestamp without time zone,
    transporterwastepackagings jsonb,
    transporterwasterefusalreason character varying,
    transporterwasterefusedweightvalue double precision,
    transporterwastevolume double precision,
    transporterwasteweightisestimate boolean,
    transporterwasteweightvalue double precision,
    type character varying,
    updatedat timestamp without time zone,
    wasteadr character varying,
    wastecode character varying,
    synthesisemittersirets jsonb,
    transporterrecepisseisexempted boolean
);


ALTER TABLE raw_zone_trackdechets.bsdasri OWNER TO pao;

--
-- Name: bsddrevisionrequest; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.bsddrevisionrequest (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    authoringcompanyid character varying,
    brokercompanyaddress character varying,
    brokercompanycontact character varying,
    brokercompanymail character varying,
    brokercompanyname character varying,
    brokercompanyphone character varying,
    brokercompanysiret character varying,
    brokerdepartment character varying,
    brokerreceipt character varying,
    brokervaliditylimit timestamp without time zone,
    bsddid character varying,
    comment character varying,
    createdat timestamp without time zone,
    id character varying NOT NULL,
    iscanceled boolean,
    processingoperationdescription character varying,
    processingoperationdone character varying,
    quantityreceived double precision,
    recipientcap character varying,
    status character varying,
    temporarystoragedestinationcap character varying,
    temporarystoragedestinationprocessingoperation character varying,
    temporarystoragetemporarystorerquantityreceived double precision,
    tradercompanyaddress character varying,
    tradercompanycontact character varying,
    tradercompanymail character varying,
    tradercompanyname character varying,
    tradercompanyphone character varying,
    tradercompanysiret character varying,
    traderdepartment character varying,
    traderreceipt character varying,
    tradervaliditylimit timestamp without time zone,
    updatedat timestamp without time zone,
    wastedetailscode character varying,
    wastedetailsname character varying,
    wastedetailspackaginginfos jsonb,
    wastedetailspop boolean
);


ALTER TABLE raw_zone_trackdechets.bsddrevisionrequest OWNER TO pao;

--
-- Name: bsff; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.bsff (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    createdat timestamp without time zone,
    destinationcompanyaddress character varying,
    destinationcompanycontact character varying,
    destinationcompanymail character varying,
    destinationcompanyname character varying,
    destinationcompanyphone character varying,
    destinationcompanysiret character varying,
    destinationcustominfo character varying,
    destinationoperationcode character varying,
    destinationoperationnextdestinationcompanyaddress character varying,
    destinationoperationnextdestinationcompanycontact character varying,
    destinationoperationnextdestinationcompanymail character varying,
    destinationoperationnextdestinationcompanyname character varying,
    destinationoperationnextdestinationcompanyphone character varying,
    destinationoperationnextdestinationcompanysiret character varying,
    destinationoperationnextdestinationcompanyvatnumber character varying,
    destinationoperationsignatureauthor character varying,
    destinationoperationsignaturedate timestamp without time zone,
    destinationplannedoperationcode character varying,
    destinationreceptionacceptationstatus character varying,
    destinationreceptiondate timestamp without time zone,
    destinationreceptionrefusalreason character varying,
    destinationreceptionsignatureauthor character varying,
    destinationreceptionsignaturedate timestamp without time zone,
    destinationreceptionweight double precision,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emittercustominfo character varying,
    emitteremissionsignatureauthor character varying,
    emitteremissionsignaturedate timestamp without time zone,
    forwardingid character varying,
    groupedinid character varying,
    id character varying NOT NULL,
    isdeleted boolean,
    isdraft boolean,
    repackagedinid character varying,
    status character varying,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterrecepissedepartment character varying,
    transporterrecepissenumber character varying,
    transporterrecepissevaliditylimit timestamp without time zone,
    transportertransportmode character varying,
    transportertransportplates jsonb,
    transportertransportsignatureauthor character varying,
    transportertransportsignaturedate timestamp without time zone,
    transportertransporttakenoverat timestamp without time zone,
    type character varying,
    updatedat timestamp without time zone,
    wasteadr character varying,
    wastecode character varying,
    wastedescription character varying,
    weightisestimate boolean,
    weightvalue double precision,
    destinationcap character varying,
    detenteurcompanysirets jsonb
);


ALTER TABLE raw_zone_trackdechets.bsff OWNER TO pao;

--
-- Name: bsffpackaging; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.bsffpackaging (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    acceptationdate timestamp without time zone,
    acceptationrefusalreason character varying,
    acceptationsignatureauthor character varying,
    acceptationsignaturedate timestamp without time zone,
    acceptationstatus character varying,
    acceptationwastecode character varying,
    acceptationwastedescription character varying,
    acceptationweight double precision,
    bsffid character varying,
    id character varying NOT NULL,
    nextpackagingid character varying,
    numero character varying,
    operationcode character varying,
    operationdate timestamp without time zone,
    operationdescription character varying,
    operationnextdestinationcap character varying,
    operationnextdestinationcompanyaddress character varying,
    operationnextdestinationcompanycontact character varying,
    operationnextdestinationcompanymail character varying,
    operationnextdestinationcompanyname character varying,
    operationnextdestinationcompanyphone character varying,
    operationnextdestinationcompanysiret character varying,
    operationnextdestinationcompanyvatnumber character varying,
    operationnextdestinationplannedoperationcode character varying,
    operationnotraceability boolean,
    operationsignatureauthor character varying,
    operationsignaturedate timestamp without time zone,
    other character varying,
    type character varying,
    volume double precision,
    weight double precision,
    emissionnumero character varying
);


ALTER TABLE raw_zone_trackdechets.bsffpackaging OWNER TO pao;

--
-- Name: bsvhu; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.bsvhu (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    createdat timestamp without time zone,
    destinationagrementnumber character varying,
    destinationcompanyaddress character varying,
    destinationcompanycontact character varying,
    destinationcompanymail character varying,
    destinationcompanyname character varying,
    destinationcompanyphone character varying,
    destinationcompanysiret character varying,
    destinationcustominfo character varying,
    destinationoperationcode character varying,
    destinationoperationdate timestamp without time zone,
    destinationoperationnextdestinationcompanyaddress character varying,
    destinationoperationnextdestinationcompanycontact character varying,
    destinationoperationnextdestinationcompanymail character varying,
    destinationoperationnextdestinationcompanyname character varying,
    destinationoperationnextdestinationcompanyphone character varying,
    destinationoperationnextdestinationcompanysiret character varying,
    destinationoperationnextdestinationcompanyvatnumber character varying,
    destinationoperationsignatureauthor character varying,
    destinationoperationsignaturedate timestamp without time zone,
    destinationplannedoperationcode character varying,
    destinationreceptionacceptationstatus character varying,
    destinationreceptiondate timestamp without time zone,
    destinationreceptionidentificationnumbers jsonb,
    destinationreceptionidentificationtype character varying,
    destinationreceptionquantity integer,
    destinationreceptionrefusalreason character varying,
    destinationreceptionweight double precision,
    destinationtype character varying,
    emitteragrementnumber character varying,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emittercustominfo character varying,
    emitteremissionsignatureauthor character varying,
    emitteremissionsignaturedate timestamp without time zone,
    id character varying NOT NULL,
    identificationnumbers jsonb,
    identificationtype character varying,
    isdeleted boolean,
    isdraft boolean,
    packaging character varying,
    quantity integer,
    status character varying,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterrecepissedepartment character varying,
    transporterrecepissenumber character varying,
    transporterrecepissevaliditylimit timestamp without time zone,
    transportertransportplates jsonb,
    transportertransportsignatureauthor character varying,
    transportertransportsignaturedate timestamp without time zone,
    transportertransporttakenoverat timestamp without time zone,
    updatedat timestamp without time zone,
    wastecode character varying,
    weightisestimate boolean,
    weightvalue double precision,
    transporterrecepisseisexempted boolean
);


ALTER TABLE raw_zone_trackdechets.bsvhu OWNER TO pao;

--
-- Name: company; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.company (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    address character varying,
    allowbsdasritakeoverwithoutsignature boolean,
    brokerreceiptid character varying,
    codedepartement character varying,
    codenaf character varying,
    companytypes jsonb,
    contact character varying,
    contactemail character varying,
    contactphone character varying,
    createdat timestamp without time zone,
    ecoorganismeagreements jsonb,
    gerepid character varying,
    givenname character varying,
    id character varying NOT NULL,
    latitude double precision,
    longitude double precision,
    name character varying,
    securitycode integer,
    siret character varying,
    traderreceiptid character varying,
    transporterreceiptid character varying,
    updatedat timestamp without time zone,
    vatnumber character varying,
    verificationcode character varying,
    verificationcomment character varying,
    verificationmode character varying,
    verificationstatus character varying,
    verifiedat timestamp without time zone,
    vhuagrementbroyeurid character varying,
    vhuagrementdemolisseurid character varying,
    website character varying,
    workercertificationid character varying,
    orgid character varying
);


ALTER TABLE raw_zone_trackdechets.company OWNER TO pao;

--
-- Name: companyassociation; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.companyassociation (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    companyid character varying,
    id character varying NOT NULL,
    role character varying,
    userid character varying,
    createdat timestamp without time zone
);


ALTER TABLE raw_zone_trackdechets.companyassociation OWNER TO pao;

--
-- Name: ecoorganisme; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.ecoorganisme (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    address character varying,
    handlebsdasri boolean,
    id character varying NOT NULL,
    name character varying,
    siret character varying
);


ALTER TABLE raw_zone_trackdechets.ecoorganisme OWNER TO pao;

--
-- Name: form; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.form (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    brokercompanyaddress character varying,
    brokercompanycontact character varying,
    brokercompanymail character varying,
    brokercompanyname character varying,
    brokercompanyphone character varying,
    brokercompanysiret character varying,
    brokerdepartment character varying,
    brokerreceipt character varying,
    brokervaliditylimit timestamp without time zone,
    createdat timestamp without time zone,
    currenttransportersiret character varying,
    customid character varying,
    ecoorganismename character varying,
    ecoorganismesiret character varying,
    emittedat timestamp without time zone,
    emittedby character varying,
    emittedbyecoorganisme boolean,
    emittercompanyaddress character varying,
    emittercompanycontact character varying,
    emittercompanymail character varying,
    emittercompanyname character varying,
    emittercompanyominumber character varying,
    emittercompanyphone character varying,
    emittercompanysiret character varying,
    emitterisforeignship boolean,
    emitterisprivateindividual boolean,
    emitterpickupsite character varying,
    emittertype character varying,
    emitterworksiteaddress character varying,
    emitterworksitecity character varying,
    emitterworksiteinfos character varying,
    emitterworksitename character varying,
    emitterworksitepostalcode character varying,
    forwardedinid character varying,
    id character varying NOT NULL,
    isaccepted boolean,
    isdeleted boolean,
    isimportedfrompaper boolean,
    nextdestinationcompanyaddress character varying,
    nextdestinationcompanycontact character varying,
    nextdestinationcompanycountry character varying,
    nextdestinationcompanymail character varying,
    nextdestinationcompanyname character varying,
    nextdestinationcompanyphone character varying,
    nextdestinationcompanysiret character varying,
    nextdestinationprocessingoperation character varying,
    nexttransportersiret character varying,
    notraceability boolean,
    ownerid character varying,
    processedat timestamp without time zone,
    processedby character varying,
    processingoperationdescription character varying,
    processingoperationdone character varying,
    quantitygrouped double precision,
    quantityreceived double precision,
    quantityreceivedtype character varying,
    readableid character varying,
    receivedat timestamp without time zone,
    receivedby character varying,
    recipientcap character varying,
    recipientcompanyaddress character varying,
    recipientcompanycontact character varying,
    recipientcompanymail character varying,
    recipientcompanyname character varying,
    recipientcompanyphone character varying,
    recipientcompanysiret character varying,
    recipientistempstorage boolean,
    recipientprocessingoperation character varying,
    sentat timestamp without time zone,
    sentby character varying,
    signedat timestamp without time zone,
    signedby character varying,
    signedbytransporter boolean,
    status character varying,
    takenoverat timestamp without time zone,
    takenoverby character varying,
    tradercompanyaddress character varying,
    tradercompanycontact character varying,
    tradercompanymail character varying,
    tradercompanyname character varying,
    tradercompanyphone character varying,
    tradercompanysiret character varying,
    traderdepartment character varying,
    traderreceipt character varying,
    tradervaliditylimit timestamp without time zone,
    transportercompanyaddress character varying,
    transportercompanycontact character varying,
    transportercompanymail character varying,
    transportercompanyname character varying,
    transportercompanyphone character varying,
    transportercompanysiret character varying,
    transportercompanyvatnumber character varying,
    transportercustominfo character varying,
    transporterdepartment character varying,
    transporterisexemptedofreceipt boolean,
    transporternumberplate character varying,
    transporterreceipt character varying,
    transportertransportmode character varying,
    transportervaliditylimit timestamp without time zone,
    updatedat timestamp without time zone,
    wasteacceptationstatus character varying,
    wastedetailsanalysisreferences jsonb,
    wastedetailscode character varying,
    wastedetailsconsistence character varying,
    wastedetailsisdangerous boolean,
    wastedetailslandidentifiers jsonb,
    wastedetailsname character varying,
    wastedetailsonucode character varying,
    wastedetailspackaginginfos jsonb,
    wastedetailsparcelnumbers jsonb,
    wastedetailspop boolean,
    wastedetailsquantity double precision,
    wastedetailsquantitytype character varying,
    wasterefusalreason character varying,
    nextdestinationcompanyvatnumber character varying,
    intermediariessirets jsonb,
    recipientssirets jsonb,
    transporterssirets jsonb,
    nextdestinationnotificationnumber character varying
);


ALTER TABLE raw_zone_trackdechets.form OWNER TO pao;

--
-- Name: traderreceipt; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.traderreceipt (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    department character varying,
    id character varying NOT NULL,
    receiptnumber character varying,
    validitylimit timestamp without time zone
);


ALTER TABLE raw_zone_trackdechets.traderreceipt OWNER TO pao;

--
-- Name: transporterreceipt; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.transporterreceipt (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    department character varying,
    id character varying NOT NULL,
    receiptnumber character varying,
    validitylimit timestamp without time zone
);


ALTER TABLE raw_zone_trackdechets.transporterreceipt OWNER TO pao;

--
-- Name: user; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets."user" (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    activatedat timestamp without time zone,
    createdat timestamp without time zone,
    email character varying,
    firstassociationdate timestamp without time zone,
    id character varying NOT NULL,
    isactive boolean,
    isadmin boolean,
    isregistrenational boolean,
    name character varying,
    password character varying,
    phone character varying,
    updatedat timestamp without time zone,
    passwordversion integer
);


ALTER TABLE raw_zone_trackdechets."user" OWNER TO pao;

--
-- Name: vhuagrement; Type: TABLE; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE TABLE raw_zone_trackdechets.vhuagrement (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    agrementnumber character varying,
    department character varying,
    id character varying NOT NULL
);


ALTER TABLE raw_zone_trackdechets.vhuagrement OWNER TO pao;

--
-- Name: groups; Type: TABLE; Schema: raw_zone_zammad; Owner: pao
--

CREATE TABLE raw_zone_zammad.groups (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    active boolean,
    assignment_timeout numeric,
    created_at timestamp without time zone,
    created_by_id numeric,
    email_address_id numeric,
    follow_up_assignment boolean,
    follow_up_possible character varying,
    id numeric NOT NULL,
    name character varying,
    note character varying,
    reopen_time_in_days numeric,
    shared_drafts boolean,
    signature_id numeric,
    updated_at timestamp without time zone,
    updated_by_id numeric,
    user_ids jsonb
);


ALTER TABLE raw_zone_zammad.groups OWNER TO pao;

--
-- Name: organizations; Type: TABLE; Schema: raw_zone_zammad; Owner: pao
--

CREATE TABLE raw_zone_zammad.organizations (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    active boolean,
    created_at timestamp without time zone,
    created_by_id numeric,
    domain character varying,
    domain_assignment boolean,
    id numeric NOT NULL,
    member_ids jsonb,
    name character varying,
    note character varying,
    secondary_member_ids jsonb,
    shared boolean,
    updated_at timestamp without time zone,
    updated_by_id numeric
);


ALTER TABLE raw_zone_zammad.organizations OWNER TO pao;

--
-- Name: tags; Type: TABLE; Schema: raw_zone_zammad; Owner: pao
--

CREATE TABLE raw_zone_zammad.tags (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    tags jsonb,
    ticket_id numeric NOT NULL
);


ALTER TABLE raw_zone_zammad.tags OWNER TO pao;

--
-- Name: tickets; Type: TABLE; Schema: raw_zone_zammad; Owner: pao
--

CREATE TABLE raw_zone_zammad.tickets (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    article_count numeric,
    article_ids jsonb,
    close_at timestamp without time zone,
    close_diff_in_min numeric,
    close_escalation_at timestamp without time zone,
    close_in_min numeric,
    create_article_sender_id numeric,
    create_article_type_id numeric,
    created_at timestamp without time zone,
    created_by_id numeric,
    customer_id numeric,
    escalation_at timestamp without time zone,
    first_response_at timestamp without time zone,
    first_response_diff_in_min numeric,
    first_response_escalation_at timestamp without time zone,
    first_response_in_min numeric,
    group_id numeric,
    id numeric NOT NULL,
    last_close_at timestamp without time zone,
    last_contact_agent_at timestamp without time zone,
    last_contact_at timestamp without time zone,
    last_contact_customer_at timestamp without time zone,
    last_owner_update_at timestamp without time zone,
    note character varying,
    number character varying,
    organization_id numeric,
    owner_id numeric,
    pending_time character varying,
    priority_id numeric,
    state_id numeric,
    ticket_time_accounting_ids jsonb,
    time_unit character varying,
    title character varying,
    type character varying,
    update_diff_in_min numeric,
    update_escalation_at timestamp without time zone,
    update_in_min numeric,
    updated_at timestamp without time zone,
    updated_by_id numeric,
    preferences jsonb
);


ALTER TABLE raw_zone_zammad.tickets OWNER TO pao;

--
-- Name: users; Type: TABLE; Schema: raw_zone_zammad; Owner: pao
--

CREATE TABLE raw_zone_zammad.users (
    _sdc_batched_at timestamp without time zone,
    _sdc_deleted_at character varying,
    _sdc_extracted_at timestamp without time zone,
    active boolean,
    address character varying,
    authorization_ids jsonb,
    city character varying,
    country character varying,
    created_at timestamp without time zone,
    created_by_id numeric,
    department character varying,
    email character varying,
    fax character varying,
    firstname character varying,
    group_ids jsonb,
    id numeric NOT NULL,
    image character varying,
    image_source character varying,
    karma_user_ids jsonb,
    last_login timestamp without time zone,
    lastname character varying,
    login character varying,
    login_failed numeric,
    mobile character varying,
    note character varying,
    organization_id numeric,
    organization_ids jsonb,
    out_of_office boolean,
    out_of_office_end_at timestamp without time zone,
    out_of_office_replacement_id numeric,
    out_of_office_start_at timestamp without time zone,
    phone character varying,
    role_ids jsonb,
    source character varying,
    street character varying,
    updated_at timestamp without time zone,
    updated_by_id numeric,
    verified boolean,
    vip boolean,
    web character varying,
    zip character varying,
    preferences jsonb
);


ALTER TABLE raw_zone_zammad.users OWNER TO pao;

--
-- Name: re_data_monitored; Type: TABLE; Schema: re; Owner: pao
--

CREATE TABLE re.re_data_monitored (
    name text,
    schema text,
    database text,
    time_filter text,
    metrics_groups text,
    additional_metrics text,
    metrics text,
    columns text,
    anomaly_detector text,
    owners text,
    selected boolean
);


ALTER TABLE re.re_data_monitored OWNER TO pao;

--
-- Name: re_data_selected; Type: VIEW; Schema: re; Owner: pao
--

CREATE VIEW re.re_data_selected AS
 SELECT re_data_monitored.name,
    re_data_monitored.schema,
    re_data_monitored.database,
    re_data_monitored.time_filter,
    re_data_monitored.metrics,
    re_data_monitored.columns,
    re_data_monitored.anomaly_detector,
    re_data_monitored.owners
   FROM re.re_data_monitored
  WHERE (re_data_monitored.selected = true);


ALTER TABLE re.re_data_selected OWNER TO pao;

--
-- Name: re_data_z_score; Type: TABLE; Schema: re; Owner: pao
--

CREATE TABLE re.re_data_z_score (
    id text,
    table_name text,
    column_name text,
    metric text,
    z_score_value double precision,
    modified_z_score_value double precision,
    last_value double precision,
    last_avg double precision,
    last_median double precision,
    last_stddev double precision,
    last_median_absolute_deviation double precision,
    last_mean_absolute_deviation double precision,
    last_iqr double precision,
    last_first_quartile double precision,
    last_third_quartile double precision,
    time_window_end timestamp without time zone,
    interval_length_sec integer,
    computed_on timestamp without time zone
);


ALTER TABLE re.re_data_z_score OWNER TO pao;

--
-- Name: re_data_anomalies; Type: VIEW; Schema: re; Owner: pao
--

CREATE VIEW re.re_data_anomalies AS
 SELECT z.id,
    z.table_name,
    z.column_name,
    z.metric,
    z.z_score_value,
    z.modified_z_score_value,
    m.anomaly_detector,
    z.last_value,
    z.last_avg,
    z.last_median,
    z.last_stddev,
    z.last_median_absolute_deviation,
    z.last_mean_absolute_deviation,
    z.last_iqr,
    (z.last_first_quartile - ((((m.anomaly_detector)::json ->> 'whisker_boundary_multiplier'::text))::double precision * z.last_iqr)) AS lower_bound,
    (z.last_third_quartile + ((((m.anomaly_detector)::json ->> 'whisker_boundary_multiplier'::text))::double precision * z.last_iqr)) AS upper_bound,
    z.last_first_quartile,
    z.last_third_quartile,
    z.time_window_end,
    z.interval_length_sec,
    z.computed_on,
    (((((
        CASE
            WHEN (z.column_name <> ''::text) THEN (((z.metric || '('::text) || z.column_name) || ')'::text)
            ELSE z.metric
        END || ' is '::text) || btrim(to_char(abs((((z.last_value - z.last_avg) / NULLIF(z.last_avg, (0)::double precision)) * (100.0)::double precision)), '9999999999999999990D00'::text))) || '% '::text) ||
        CASE
            WHEN (z.last_value > z.last_avg) THEN 'greater than'::text
            WHEN (z.last_value = z.last_avg) THEN 'equal to'::text
            ELSE 'less than'::text
        END) || ' average.'::text) AS message,
        CASE
            WHEN (z.metric = 'freshness'::text) THEN (btrim(to_char((z.last_value / (3600)::double precision), '9999999999999999990D00'::text)) || ' hours'::text)
            WHEN (z.metric ~ 'percent'::text) THEN (btrim(to_char(z.last_value, '9999999999999999990D00'::text)) || '%'::text)
            WHEN (z.metric ~ 'count'::text) THEN (z.last_value)::text
            ELSE btrim(to_char(z.last_value, '9999999999999999990D00'::text))
        END AS last_value_text
   FROM (re.re_data_z_score z
     LEFT JOIN re.re_data_selected m ON (((split_part(regexp_replace(z.table_name, '(")|(`)'::text, ''::text, 'g'::text), '.'::text, 1) = m.database) AND (split_part(regexp_replace(z.table_name, '(")|(`)'::text, ''::text, 'g'::text), '.'::text, 2) = m.schema) AND (split_part(regexp_replace(z.table_name, '(")|(`)'::text, ''::text, 'g'::text), '.'::text, 3) = m.name))))
  WHERE
        CASE
            WHEN (((m.anomaly_detector)::json ->> 'name'::text) = 'z_score'::text) THEN (abs(z.z_score_value) > (((m.anomaly_detector)::json ->> 'threshold'::text))::double precision)
            WHEN (((m.anomaly_detector)::json ->> 'name'::text) = 'modified_z_score'::text) THEN (abs(z.modified_z_score_value) > (((m.anomaly_detector)::json ->> 'threshold'::text))::double precision)
            WHEN (((m.anomaly_detector)::json ->> 'name'::text) = 'boxplot'::text) THEN ((z.last_value < (z.last_first_quartile - ((((m.anomaly_detector)::json ->> 'whisker_boundary_multiplier'::text))::double precision * z.last_iqr))) OR (z.last_value > (z.last_third_quartile + ((((m.anomaly_detector)::json ->> 'whisker_boundary_multiplier'::text))::double precision * z.last_iqr))))
            ELSE false
        END;


ALTER TABLE re.re_data_anomalies OWNER TO pao;

--
-- Name: re_data_schema_changes; Type: TABLE; Schema: re; Owner: pao
--

CREATE TABLE re.re_data_schema_changes (
    id text,
    table_name text,
    operation text,
    column_name text,
    data_type text,
    is_nullable boolean,
    prev_column_name text,
    prev_data_type text,
    prev_is_nullable boolean,
    detected_time timestamp without time zone
);


ALTER TABLE re.re_data_schema_changes OWNER TO pao;

--
-- Name: re_data_test_history; Type: TABLE; Schema: re; Owner: pao
--

CREATE TABLE re.re_data_test_history (
    table_name text,
    column_name text,
    test_name text,
    status text,
    execution_time double precision,
    message text,
    failures_count double precision,
    failures_json text,
    failures_table text,
    severity text,
    compiled_sql text,
    run_at timestamp without time zone
);


ALTER TABLE re.re_data_test_history OWNER TO pao;

--
-- Name: re_data_alerts; Type: VIEW; Schema: re; Owner: pao
--

CREATE VIEW re.re_data_alerts AS
 SELECT 'anomaly'::text AS type,
    regexp_replace(re_data_anomalies.table_name, '(")|(`)'::text, ''::text, 'g'::text) AS model,
    re_data_anomalies.message,
    re_data_anomalies.last_value_text AS value,
    re_data_anomalies.time_window_end
   FROM re.re_data_anomalies
UNION ALL
 SELECT 'schema_change'::text AS type,
    regexp_replace(re_data_schema_changes.table_name, '(")|(`)'::text, ''::text, 'g'::text) AS model,
        CASE
            WHEN (re_data_schema_changes.operation = 'column_added'::text) THEN (((('column '::text || re_data_schema_changes.column_name) || ' of type '::text) || re_data_schema_changes.data_type) || ' was added.'::text)
            WHEN (re_data_schema_changes.operation = 'column_removed'::text) THEN (((('column '::text || re_data_schema_changes.prev_column_name) || ' of type '::text) || re_data_schema_changes.prev_data_type) || ' was removed.'::text)
            WHEN (re_data_schema_changes.operation = 'type_change'::text) THEN (((((re_data_schema_changes.column_name || ' column data type was changed from '::text) || re_data_schema_changes.prev_data_type) || ' to '::text) || re_data_schema_changes.data_type) || '.'::text)
            ELSE ''::text
        END AS message,
    ''::text AS value,
    re_data_schema_changes.detected_time AS time_window_end
   FROM re.re_data_schema_changes
UNION ALL
 SELECT 'test'::text AS type,
    re_data_test_history.table_name AS model,
        CASE
            WHEN (re_data_test_history.column_name IS NULL) THEN (('Test '::text || re_data_test_history.test_name) || ' failed.'::text)
            ELSE (((('Test '::text || re_data_test_history.test_name) || ' failed for column '::text) || re_data_test_history.column_name) || '.'::text)
        END AS message,
    re_data_test_history.status AS value,
    re_data_test_history.run_at AS time_window_end
   FROM re.re_data_test_history
  WHERE ((re_data_test_history.status = 'Fail'::text) OR (re_data_test_history.status = 'Error'::text));


ALTER TABLE re.re_data_alerts OWNER TO pao;

--
-- Name: re_data_base_metrics; Type: TABLE; Schema: re; Owner: pao
--

CREATE TABLE re.re_data_base_metrics (
    id text,
    table_name text,
    column_name text,
    metric text,
    value double precision,
    time_window_start timestamp without time zone,
    time_window_end timestamp without time zone,
    interval_length_sec integer,
    computed_on timestamp without time zone
);


ALTER TABLE re.re_data_base_metrics OWNER TO pao;

--
-- Name: re_data_columns; Type: TABLE; Schema: re; Owner: pao
--

CREATE TABLE re.re_data_columns (
    name text,
    schema text,
    database text,
    column_name text,
    data_type text,
    is_nullable boolean,
    time_filter text,
    computed_on timestamp without time zone
);


ALTER TABLE re.re_data_columns OWNER TO pao;

--
-- Name: re_data_columns_over_time; Type: TABLE; Schema: re; Owner: pao
--

CREATE TABLE re.re_data_columns_over_time (
    id text,
    table_name text,
    column_name text,
    data_type text,
    is_nullable boolean,
    detected_time timestamp without time zone
);


ALTER TABLE re.re_data_columns_over_time OWNER TO pao;

--
-- Name: re_data_last_metrics; Type: VIEW; Schema: re; Owner: pao
--

CREATE VIEW re.re_data_last_metrics AS
 SELECT re_data_base_metrics.table_name,
    re_data_base_metrics.column_name,
    re_data_base_metrics.metric,
    re_data_base_metrics.value AS last_value,
    re_data_base_metrics.interval_length_sec,
    re_data_base_metrics.computed_on
   FROM re.re_data_base_metrics
  WHERE (re_data_base_metrics.time_window_end = '2023-02-17 00:00:00'::timestamp without time zone);


ALTER TABLE re.re_data_last_metrics OWNER TO pao;

--
-- Name: re_data_last_stats; Type: VIEW; Schema: re; Owner: pao
--

CREATE VIEW re.re_data_last_stats AS
 WITH median_value AS (
         SELECT DISTINCT re_data_base_metrics.table_name,
            re_data_base_metrics.column_name,
            re_data_base_metrics.metric,
            re_data_base_metrics.interval_length_sec,
            avg(re_data_base_metrics.value) AS last_avg,
            percentile_cont((0.25)::double precision) WITHIN GROUP (ORDER BY re_data_base_metrics.value) AS last_first_quartile,
            percentile_cont((0.5)::double precision) WITHIN GROUP (ORDER BY re_data_base_metrics.value) AS last_median,
            percentile_cont((0.75)::double precision) WITHIN GROUP (ORDER BY re_data_base_metrics.value) AS last_third_quartile
           FROM re.re_data_base_metrics
          WHERE ((re_data_base_metrics.time_window_end > ('2023-02-16 00:00:00'::timestamp without time zone - '30 days'::interval)) AND (re_data_base_metrics.time_window_end <= '2023-02-17 00:00:00'::timestamp without time zone))
          GROUP BY re_data_base_metrics.table_name, re_data_base_metrics.column_name, re_data_base_metrics.metric, re_data_base_metrics.interval_length_sec
        ), abs_deviation AS (
         SELECT s_1.table_name,
            s_1.column_name,
            s_1.metric,
            s_1.interval_length_sec,
            abs((s_1.value - mv_1.last_avg)) AS absolute_deviation_from_mean,
            abs((s_1.value - mv_1.last_median)) AS absolute_deviation_from_median
           FROM (re.re_data_base_metrics s_1
             LEFT JOIN median_value mv_1 ON (((s_1.table_name = mv_1.table_name) AND (s_1.column_name = mv_1.column_name) AND (s_1.metric = mv_1.metric) AND (s_1.interval_length_sec = mv_1.interval_length_sec))))
          WHERE ((s_1.time_window_end > ('2023-02-16 00:00:00'::timestamp without time zone - '30 days'::interval)) AND (s_1.time_window_end <= '2023-02-17 00:00:00'::timestamp without time zone))
        ), median_abs_deviation AS (
         SELECT DISTINCT abs_deviation.table_name,
            abs_deviation.column_name,
            abs_deviation.metric,
            abs_deviation.interval_length_sec,
            avg(abs_deviation.absolute_deviation_from_mean) AS mean_absolute_deviation,
            percentile_cont((0.5)::double precision) WITHIN GROUP (ORDER BY abs_deviation.absolute_deviation_from_median) AS median_absolute_deviation
           FROM abs_deviation
          GROUP BY abs_deviation.table_name, abs_deviation.column_name, abs_deviation.metric, abs_deviation.interval_length_sec
        ), stats AS (
         SELECT re_data_base_metrics.table_name,
            re_data_base_metrics.column_name,
            re_data_base_metrics.metric,
            stddev(re_data_base_metrics.value) AS last_stddev,
            max(re_data_base_metrics.time_window_end) AS last_metric_time,
            re_data_base_metrics.interval_length_sec,
            max(re_data_base_metrics.computed_on) AS computed_on
           FROM re.re_data_base_metrics
          WHERE ((re_data_base_metrics.time_window_end > ('2023-02-16 00:00:00'::timestamp without time zone - '30 days'::interval)) AND (re_data_base_metrics.time_window_end <= '2023-02-17 00:00:00'::timestamp without time zone))
          GROUP BY re_data_base_metrics.table_name, re_data_base_metrics.column_name, re_data_base_metrics.metric, re_data_base_metrics.interval_length_sec
        )
 SELECT s.table_name,
    s.column_name,
    s.metric,
    mv.last_avg,
    s.last_stddev,
    s.last_metric_time,
    s.interval_length_sec,
    s.computed_on,
    mv.last_median,
    mv.last_first_quartile,
    mv.last_third_quartile,
    md.median_absolute_deviation AS last_median_absolute_deviation,
    md.mean_absolute_deviation AS last_mean_absolute_deviation
   FROM ((stats s
     LEFT JOIN median_value mv ON (((s.table_name = mv.table_name) AND (s.column_name = mv.column_name) AND (s.metric = mv.metric) AND (s.interval_length_sec = mv.interval_length_sec))))
     LEFT JOIN median_abs_deviation md ON (((s.table_name = md.table_name) AND (s.column_name = md.column_name) AND (s.metric = md.metric) AND (s.interval_length_sec = md.interval_length_sec))));


ALTER TABLE re.re_data_last_stats OWNER TO pao;

--
-- Name: re_data_metrics; Type: VIEW; Schema: re; Owner: pao
--

CREATE VIEW re.re_data_metrics AS
 SELECT re_data_base_metrics.id,
    re_data_base_metrics.table_name,
    re_data_base_metrics.column_name,
    re_data_base_metrics.metric,
    re_data_base_metrics.value,
    re_data_base_metrics.time_window_start,
    re_data_base_metrics.time_window_end,
    re_data_base_metrics.interval_length_sec,
    re_data_base_metrics.computed_on
   FROM re.re_data_base_metrics;


ALTER TABLE re.re_data_metrics OWNER TO pao;

--
-- Name: re_data_table_samples; Type: TABLE; Schema: re; Owner: pao
--

CREATE TABLE re.re_data_table_samples (
    table_name text,
    sample_data text,
    sampled_on timestamp without time zone
);


ALTER TABLE re.re_data_table_samples OWNER TO pao;

--
-- Name: re_data_test_runs; Type: VIEW; Schema: re; Owner: pao
--

CREATE VIEW re.re_data_test_runs AS
 SELECT sum(
        CASE
            WHEN (re_data_test_history.status = 'Fail'::text) THEN 1
            ELSE 0
        END) AS failed,
    sum(
        CASE
            WHEN (re_data_test_history.status = 'Pass'::text) THEN 1
            ELSE 0
        END) AS passed,
    re_data_test_history.run_at
   FROM re.re_data_test_history
  GROUP BY re_data_test_history.run_at
  ORDER BY re_data_test_history.run_at DESC;


ALTER TABLE re.re_data_test_runs OWNER TO pao;

--
-- Name: re_data_last_base_metrics_part0; Type: TABLE; Schema: re_internal; Owner: pao
--

CREATE TABLE re_internal.re_data_last_base_metrics_part0 (
    table_name text,
    column_name text,
    metric text,
    value double precision
);


ALTER TABLE re_internal.re_data_last_base_metrics_part0 OWNER TO pao;

--
-- Name: re_data_last_base_metrics_part1; Type: TABLE; Schema: re_internal; Owner: pao
--

CREATE TABLE re_internal.re_data_last_base_metrics_part1 (
    table_name text,
    column_name text,
    metric text,
    value double precision
);


ALTER TABLE re_internal.re_data_last_base_metrics_part1 OWNER TO pao;

--
-- Name: re_data_last_base_metrics_part2; Type: TABLE; Schema: re_internal; Owner: pao
--

CREATE TABLE re_internal.re_data_last_base_metrics_part2 (
    table_name text,
    column_name text,
    metric text,
    value double precision
);


ALTER TABLE re_internal.re_data_last_base_metrics_part2 OWNER TO pao;

--
-- Name: re_data_last_base_metrics_part3; Type: TABLE; Schema: re_internal; Owner: pao
--

CREATE TABLE re_internal.re_data_last_base_metrics_part3 (
    table_name text,
    column_name text,
    metric text,
    value double precision
);


ALTER TABLE re_internal.re_data_last_base_metrics_part3 OWNER TO pao;

--
-- Name: re_data_last_base_metrics_thread0; Type: TABLE; Schema: re_internal; Owner: pao
--

CREATE TABLE re_internal.re_data_last_base_metrics_thread0 (
    table_name text,
    column_name text,
    metric text,
    value double precision
);


ALTER TABLE re_internal.re_data_last_base_metrics_thread0 OWNER TO pao;

--
-- Name: re_data_last_base_metrics_thread1; Type: TABLE; Schema: re_internal; Owner: pao
--

CREATE TABLE re_internal.re_data_last_base_metrics_thread1 (
    table_name text,
    column_name text,
    metric text,
    value double precision
);


ALTER TABLE re_internal.re_data_last_base_metrics_thread1 OWNER TO pao;

--
-- Name: re_data_last_base_metrics_thread2; Type: TABLE; Schema: re_internal; Owner: pao
--

CREATE TABLE re_internal.re_data_last_base_metrics_thread2 (
    table_name text,
    column_name text,
    metric text,
    value double precision
);


ALTER TABLE re_internal.re_data_last_base_metrics_thread2 OWNER TO pao;

--
-- Name: re_data_last_base_metrics_thread3; Type: TABLE; Schema: re_internal; Owner: pao
--

CREATE TABLE re_internal.re_data_last_base_metrics_thread3 (
    table_name text,
    column_name text,
    metric text,
    value double precision
);


ALTER TABLE re_internal.re_data_last_base_metrics_thread3 OWNER TO pao;

--
-- Name: re_data_last_table_samples; Type: TABLE; Schema: re_internal; Owner: pao
--

CREATE TABLE re_internal.re_data_last_table_samples (
    table_name text,
    sample_data text
);


ALTER TABLE re_internal.re_data_last_table_samples OWNER TO pao;

--
-- Name: re_data_last_table_samples_part; Type: TABLE; Schema: re_internal; Owner: pao
--

CREATE TABLE re_internal.re_data_last_table_samples_part (
    table_name text,
    sample_data text
);


ALTER TABLE re_internal.re_data_last_table_samples_part OWNER TO pao;

--
-- Name: re_data_run_started_at; Type: TABLE; Schema: re_internal; Owner: pao
--

CREATE TABLE re_internal.re_data_run_started_at (
    run_started_at numeric
);


ALTER TABLE re_internal.re_data_run_started_at OWNER TO pao;

--
-- Name: bordereaux_counts_by_siret; Type: TABLE; Schema: refined_zone_analytics; Owner: pao
--

CREATE TABLE refined_zone_analytics.bordereaux_counts_by_siret (
    siret character varying,
    num_bsdd_emitter bigint,
    num_bsda_emitter bigint,
    num_bsff_emitter bigint,
    num_bsdasri_emitter bigint,
    num_bsvhu_emitter bigint,
    num_bsdd_destination bigint,
    num_bsda_destination bigint,
    num_bsff_destination bigint,
    num_bsdasri_destination bigint,
    num_bsvhu_destination bigint,
    total_bordereaux bigint
);


ALTER TABLE refined_zone_analytics.bordereaux_counts_by_siret OWNER TO pao;

--
-- Name: etablissements_inscrits_par_departements; Type: TABLE; Schema: refined_zone_analytics; Owner: pao
--

CREATE TABLE refined_zone_analytics.etablissements_inscrits_par_departements (
    dep character varying,
    num_etabs bigint
);


ALTER TABLE refined_zone_analytics.etablissements_inscrits_par_departements OWNER TO pao;

--
-- Name: etablissements_par_departements; Type: TABLE; Schema: refined_zone_analytics; Owner: pao
--

CREATE TABLE refined_zone_analytics.etablissements_par_departements (
    dep character varying,
    num_etabs bigint
);


ALTER TABLE refined_zone_analytics.etablissements_par_departements OWNER TO pao;

--
-- Name: identification_eco_organismes; Type: TABLE; Schema: refined_zone_analytics; Owner: pao
--

CREATE TABLE refined_zone_analytics.identification_eco_organismes (
    inscrit_sur_td boolean,
    eco_organisme_agree boolean,
    dans_table_eo boolean,
    "a_entré_un_agrément_eo" boolean,
    a_choisi_profil_eo boolean,
    "visé_dans_bsdd" boolean,
    "visé_dans_bsda" boolean,
    "visé_dans_bsdasri" boolean,
    siret character varying,
    nom text,
    admin_name character varying,
    admin_email character varying
);


ALTER TABLE refined_zone_analytics.identification_eco_organismes OWNER TO pao;

--
-- Name: moulinette_dechetteries; Type: TABLE; Schema: refined_zone_analytics; Owner: pao
--

CREATE TABLE refined_zone_analytics.moulinette_dechetteries (
    siret character varying,
    "Nom de l'établissement" text,
    "Profils de l'établissement" text,
    "E-mail de contact de l'établissement" text,
    "E-mail de l'admin de l'établissement" text,
    num_bsdd_destinataire bigint,
    num_bsda_destinataire bigint,
    num_bsff_destinataire bigint,
    num_bsdasri_destinataire bigint,
    num_bsvhu_destinataire bigint,
    num_bsdd_emetteur bigint,
    num_bsda_emetteur bigint,
    num_bsff_emetteur bigint,
    num_bsdasri_emetteur bigint,
    num_bsvhu_emetteur bigint,
    total_bordereaux bigint
);


ALTER TABLE refined_zone_analytics.moulinette_dechetteries OWNER TO pao;

--
-- Name: prop_dep_etabs_inscrits; Type: VIEW; Schema: refined_zone_analytics; Owner: pao
--

CREATE VIEW refined_zone_analytics.prop_dep_etabs_inscrits AS
 SELECT td.dep,
    ((100)::double precision * ((td.num_etabs)::double precision / (sirene.num_etabs)::double precision)) AS prop_etab_inscrits_td_sur_sirene
   FROM (refined_zone_analytics.etablissements_inscrits_par_departements td
     JOIN refined_zone_analytics.etablissements_par_departements sirene ON (((td.dep)::text = (sirene.dep)::text)));


ALTER TABLE refined_zone_analytics.prop_dep_etabs_inscrits OWNER TO pao;

--
-- Name: transporters_without_receipt; Type: TABLE; Schema: refined_zone_analytics; Owner: pao
--

CREATE TABLE refined_zone_analytics.transporters_without_receipt (
    transporter_company_siret character varying
);


ALTER TABLE refined_zone_analytics.transporters_without_receipt OWNER TO pao;

--
-- Name: bsda_enriched; Type: TABLE; Schema: refined_zone_enriched; Owner: pao
--

CREATE TABLE refined_zone_enriched.bsda_enriched (
    id character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    status character varying,
    type character varying,
    is_deleted boolean,
    is_draft boolean,
    waste_code character varying,
    waste_family_code character varying,
    waste_pop boolean,
    waste_consistence character varying,
    waste_material_name character varying,
    waste_adr character varying,
    waste_seal_numbers jsonb,
    weight_is_estimate boolean,
    packagings jsonb,
    repackaged_in_id character varying,
    emitter_company_siret character varying,
    emitter_company_name character varying,
    emitter_company_address character varying,
    emitter_company_contact character varying,
    emitter_company_mail character varying,
    emitter_company_phone character varying,
    emitter_custom_info character varying,
    emitter_emission_signature_author character varying,
    emitter_emission_signature_date timestamp without time zone,
    emitter_isprivate_individual boolean,
    emitter_pickup_site_name character varying,
    emitter_pickup_site_address character varying,
    emitter_pickup_site_postal_code character varying,
    emitter_pickup_site_city character varying,
    emitter_pickup_site_infos character varying,
    worker_company_siret character varying,
    worker_company_name character varying,
    worker_company_address character varying,
    worker_company_contact character varying,
    worker_company_phone character varying,
    worker_company_mail character varying,
    worker_certification_organisation character varying,
    worker_certification_certification_number character varying,
    worker_certification_has_subsection_three boolean,
    worker_certification_has_subsection_four boolean,
    worker_certificationvalidity_limit timestamp without time zone,
    worker_work_has_emitter_paper_signature boolean,
    worker_work_signature_author character varying,
    worker_work_signature_date timestamp without time zone,
    worker_is_disabled boolean,
    transporter_company_siret character varying,
    transporter_company_name character varying,
    transporter_company_address character varying,
    transporter_recepisse_department character varying,
    transporter_company_contact character varying,
    transporter_company_mail character varying,
    transporter_company_phone character varying,
    transporter_company_vat_number character varying,
    transporter_custom_info character varying,
    transporter_recepisse_is_exempted boolean,
    transporter_recepisse_number character varying,
    transporter_recepisse_validity_limit timestamp without time zone,
    transporter_transport_mode character varying,
    transporter_transport_plates jsonb,
    transporter_transport_signature_author character varying,
    transporter_transport_signature_date timestamp without time zone,
    transporter_transport_taken_over_at timestamp without time zone,
    destination_company_siret character varying,
    destination_company_name character varying,
    destination_company_address character varying,
    destination_company_contact character varying,
    destination_company_mail character varying,
    destination_company_phone character varying,
    destination_custom_info character varying,
    destination_reception_date timestamp without time zone,
    destination_cap character varying,
    destination_reception_acceptation_status character varying,
    destination_operation_date timestamp without time zone,
    destination_operation_description character varying,
    destination_operation_signature_author character varying,
    destination_operation_signature_date timestamp without time zone,
    destination_reception_refusal_reason character varying,
    eco_organisme_siret character varying,
    eco_organisme_name character varying,
    destination_operation_next_destination_company_siret character varying,
    destination_operation_next_destination_company_name character varying,
    destination_operation_next_destination_company_address character varying,
    destination_operation_next_destination_company_contact character varying,
    destination_operation_next_destination_company_mail character varying,
    destination_operation_next_destination_company_phone character varying,
    destination_operation_next_destination_company_vat_number character varying,
    destination_operation_next_destination_cap character varying,
    destination_operation_next_destination_planned_operation_code character varying,
    broker_company_address character varying,
    broker_company_contact character varying,
    broker_company_mail character varying,
    broker_company_name character varying,
    broker_company_phone character varying,
    broker_company_siret character varying,
    broker_recepisse_department character varying,
    broker_recepisse_number character varying,
    broker_recepisse_validity_limit timestamp without time zone,
    forwarding_id character varying,
    grouped_in_id character varying,
    destination_planned_operation_code text,
    destination_operation_code text,
    weight_value double precision,
    destination_reception_weight double precision,
    emitter_commune character varying,
    emitter_departement character varying,
    emitter_region integer,
    emitter_latitude double precision,
    emitter_longitude double precision,
    emitter_naf character varying,
    destination_commune character varying,
    destination_departement character varying,
    destination_region integer,
    destination_latitude double precision,
    destination_longitude double precision,
    destination_naf character varying
);


ALTER TABLE refined_zone_enriched.bsda_enriched OWNER TO pao;

--
-- Name: bsdasri_enriched; Type: TABLE; Schema: refined_zone_enriched; Owner: pao
--

CREATE TABLE refined_zone_enriched.bsdasri_enriched (
    id character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    status character varying,
    type character varying,
    is_deleted boolean,
    is_draft boolean,
    waste_adr character varying,
    waste_code character varying,
    identification_numbers jsonb,
    emitter_company_siret character varying,
    emitter_company_name character varying,
    emitter_company_address character varying,
    emitter_company_contact character varying,
    emitter_company_mail character varying,
    emitter_company_phone character varying,
    emitter_custom_info character varying,
    emitter_pickup_sitename character varying,
    emitter_pickup_site_address character varying,
    emitter_pickup_site_postal_code character varying,
    emitter_pickup_site_city character varying,
    emitter_pickup_site_infos character varying,
    emitter_emission_signature_date timestamp without time zone,
    emitter_emission_signature_author character varying,
    emitted_by_eco_organisme boolean,
    emitter_waste_volume double precision,
    emitter_waste_weight_value double precision,
    emitter_waste_weight_is_estimate boolean,
    emitter_waste_packagings jsonb,
    emission_signatory_id character varying,
    is_emission_direct_taken_over boolean,
    is_emission_taken_over_with_secret_code boolean,
    transporter_company_siret character varying,
    transporter_company_name character varying,
    transporter_company_address character varying,
    transporter_company_contact character varying,
    transporter_company_mail character varying,
    transporter_company_phone character varying,
    transporter_company_vat_number character varying,
    transporter_custom_info character varying,
    transport_signatory_id character varying,
    transporter_recepisse_number character varying,
    transporter_recepisse_department character varying,
    transporter_recepisse_validity_limit timestamp without time zone,
    transporter_transport_mode character varying,
    transporter_transport_plates jsonb,
    transporter_acceptation_status character varying,
    transporter_taken_over_at timestamp without time zone,
    transporter_transport_signature_date timestamp without time zone,
    transporter_transport_signature_author character varying,
    transporter_waste_volume double precision,
    transporter_waste_weight_is_estimate boolean,
    transporter_waste_packagings jsonb,
    transporter_waste_refusal_reason character varying,
    transporter_waste_refused_weight_value double precision,
    destination_company_siret character varying,
    destination_company_name character varying,
    destination_company_address character varying,
    destination_company_contact character varying,
    destination_company_mail character varying,
    destination_company_phone character varying,
    destination_custom_info character varying,
    destination_reception_date timestamp without time zone,
    destination_reception_signature_date timestamp without time zone,
    destination_reception_signature_author character varying,
    destination_waste_packagings jsonb,
    destination_reception_waste_volume double precision,
    destination_reception_waste_refusal_reason character varying,
    reception_signatory_id character varying,
    destination_operation_date timestamp without time zone,
    destination_operation_code character varying,
    destination_operation_signature_date timestamp without time zone,
    destination_operation_signature_author character varying,
    operation_signatory_id character varying,
    destination_reception_acceptation_status character varying,
    handed_over_to_recipient_at timestamp without time zone,
    eco_organisme_siret character varying,
    eco_organisme_name character varying,
    grouped_in_id character varying,
    synthesized_in_id character varying,
    transporter_waste_weight_value double precision,
    destination_reception_waste_weight_value double precision,
    destination_reception_waste_refused_weight_value double precision,
    emitter_commune character varying,
    emitter_departement character varying,
    emitter_region integer,
    emitter_latitude double precision,
    emitter_longitude double precision,
    emitter_naf character varying,
    destination_commune character varying,
    destination_departement character varying,
    destination_region integer,
    destination_latitude double precision,
    destination_longitude double precision,
    destination_naf character varying
);


ALTER TABLE refined_zone_enriched.bsdasri_enriched OWNER TO pao;

--
-- Name: bsdd_enriched; Type: TABLE; Schema: refined_zone_enriched; Owner: pao
--

CREATE TABLE refined_zone_enriched.bsdd_enriched (
    id character varying,
    custom_id character varying,
    readable_id character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    status character varying,
    is_deleted boolean,
    owner_id character varying,
    waste_details_code character varying,
    waste_details_name character varying,
    waste_details_pop boolean,
    waste_details_is_dangerous boolean,
    waste_details_onu_code character varying,
    waste_details_quantity double precision,
    waste_details_quantity_type character varying,
    waste_details_consistence character varying,
    waste_details_packaging_infos jsonb,
    waste_details_analysis_references jsonb,
    waste_details_land_identifiers jsonb,
    waste_details_parcel_numbers jsonb,
    waste_acceptation_status character varying,
    waste_refusal_reason character varying,
    emitter_company_siret character varying,
    emitter_company_name character varying,
    emitter_type character varying,
    emitter_company_address character varying,
    emitter_company_contact character varying,
    emitter_company_mail character varying,
    emitter_company_phone character varying,
    emitter_is_foreignship boolean,
    emitter_company_omi_number character varying,
    emitter_is_private_individual boolean,
    emitter_pickup_site character varying,
    emitter_worksite_name character varying,
    emitter_worksite_address character varying,
    emitter_worksite_postal_code character varying,
    emitter_worksite_city character varying,
    emitter_worksite_infos character varying,
    emitted_by_eco_organisme boolean,
    emitted_at timestamp without time zone,
    emitted_by character varying,
    signed_at timestamp without time zone,
    signed_by character varying,
    signed_by_transporter boolean,
    sent_at timestamp without time zone,
    sent_by character varying,
    transporter_company_siret character varying,
    transporter_company_name character varying,
    transporter_company_address character varying,
    transporter_department character varying,
    transporter_company_contact character varying,
    transporter_company_mail character varying,
    transporter_company_phone character varying,
    transporter_number_plate character varying,
    transporter_receipt character varying,
    transporter_validity_limit timestamp without time zone,
    transporter_transport_mode character varying,
    transporter_company_vat_number character varying,
    transporter_custom_info character varying,
    transporter_is_exempted_of_receipt boolean,
    current_transporter_siret character varying,
    next_transporter_siret character varying,
    taken_over_at timestamp without time zone,
    taken_over_by character varying,
    recipient_company_siret character varying,
    recipient_company_name character varying,
    recipient_company_address character varying,
    recipient_company_contact character varying,
    recipient_company_mail character varying,
    recipient_company_phone character varying,
    recipient_is_temp_storage boolean,
    recipient_cap character varying,
    received_at timestamp without time zone,
    received_by character varying,
    processed_at timestamp without time zone,
    processed_by character varying,
    quantity_received double precision,
    quantity_received_type character varying,
    processing_operation_description character varying,
    no_traceability boolean,
    is_accepted boolean,
    next_destination_company_siret character varying,
    next_destination_company_name character varying,
    next_destination_company_address character varying,
    next_destination_company_country character varying,
    next_destination_company_contact character varying,
    next_destination_company_mail character varying,
    next_destination_company_phone character varying,
    next_destination_company_vat_number character varying,
    next_destination_processing_operation character varying,
    broker_company_siret character varying,
    broker_company_name character varying,
    broker_company_address character varying,
    broker_department character varying,
    broker_company_contact character varying,
    broker_company_mail character varying,
    broker_company_phone character varying,
    broker_receipt character varying,
    broker_validity_limit timestamp without time zone,
    trader_company_siret character varying,
    trader_company_name character varying,
    trader_company_address character varying,
    trader_department character varying,
    trader_company_contact character varying,
    trader_company_mail character varying,
    trader_company_phone character varying,
    trader_receipt character varying,
    trader_validity_limit timestamp without time zone,
    eco_organisme_siret character varying,
    eco_organisme_name character varying,
    is_imported_from_paper boolean,
    forwarded_in_id character varying,
    recipient_processing_operation text,
    processing_operation_done text,
    emitter_commune character varying,
    emitter_departement character varying,
    emitter_region integer,
    emitter_latitude double precision,
    emitter_longitude double precision,
    emitter_naf character varying,
    recipient_commune character varying,
    recipient_departement character varying,
    recipient_region integer,
    recipient_latitude double precision,
    recipient_longitude double precision,
    recipient_naf character varying
);


ALTER TABLE refined_zone_enriched.bsdd_enriched OWNER TO pao;

--
-- Name: bsff_enriched; Type: TABLE; Schema: refined_zone_enriched; Owner: pao
--

CREATE TABLE refined_zone_enriched.bsff_enriched (
    id character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    is_deleted boolean,
    is_draft boolean,
    status character varying,
    type character varying,
    waste_code character varying,
    waste_description character varying,
    waste_adr character varying,
    weight_is_estimate boolean,
    emitter_company_siret character varying,
    emitter_company_name character varying,
    emitter_company_address character varying,
    emitter_company_contact character varying,
    emitter_company_mail character varying,
    emitter_company_phone character varying,
    emitter_custom_info character varying,
    emitter_emission_signature_date timestamp without time zone,
    emitter_emission_signature_author character varying,
    transporter_company_address character varying,
    transporter_company_contact character varying,
    transporter_company_mail character varying,
    transporter_company_name character varying,
    transporter_company_phone character varying,
    transporter_company_siret character varying,
    transporter_company_vat_number character varying,
    transporter_custom_info character varying,
    transporter_recepisse_department character varying,
    transporter_recepisse_number character varying,
    transporter_recepisse_validity_limit timestamp without time zone,
    transporter_transport_mode character varying,
    transporter_transport_plates jsonb,
    transporter_transport_signature_author character varying,
    transporter_transport_signature_date timestamp without time zone,
    transporter_transport_taken_over_at timestamp without time zone,
    destination_company_siret character varying,
    destination_company_address character varying,
    destination_company_contact character varying,
    destination_company_mail character varying,
    destination_company_name character varying,
    destination_company_phone character varying,
    destination_custom_info character varying,
    destination_reception_date timestamp without time zone,
    destination_reception_signature_date timestamp without time zone,
    destination_reception_signature_author character varying,
    destination_reception_acceptation_status character varying,
    destination_reception_refusal_reason character varying,
    destination_planned_operation_code character varying,
    destination_operation_code character varying,
    destination_operation_signature_date timestamp without time zone,
    destination_operation_signature_author character varying,
    destination_operation_next_destination_company_siret character varying,
    destination_operation_next_destination_company_name character varying,
    destination_operation_next_destination_company_address character varying,
    destination_operation_next_destination_company_contact character varying,
    destination_operation_next_destination_company_mail character varying,
    destination_operation_next_destination_company_phone character varying,
    destination_operation_next_destination_company_vat_number character varying,
    forwarding_id character varying,
    grouped_in_id character varying,
    repackaged_in_id character varying,
    weight_value double precision,
    destination_reception_weight double precision,
    emitter_commune character varying,
    emitter_departement character varying,
    emitter_region integer,
    emitter_latitude double precision,
    emitter_longitude double precision,
    emitter_naf character varying,
    destination_commune character varying,
    destination_departement character varying,
    destination_region integer,
    destination_latitude double precision,
    destination_longitude double precision,
    destination_naf character varying
);


ALTER TABLE refined_zone_enriched.bsff_enriched OWNER TO pao;

--
-- Name: bsvhu_enriched; Type: TABLE; Schema: refined_zone_enriched; Owner: pao
--

CREATE TABLE refined_zone_enriched.bsvhu_enriched (
    id character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    is_deleted boolean,
    is_draft boolean,
    status character varying,
    waste_code character varying,
    quantity integer,
    weight_is_estimate boolean,
    packaging character varying,
    emitter_company_siret character varying,
    emitter_company_name character varying,
    emitter_company_address character varying,
    emitter_company_contact character varying,
    emitter_company_mail character varying,
    emitter_company_phone character varying,
    emitter_custom_info character varying,
    emitter_agrement_number character varying,
    emitter_emission_signature_date timestamp without time zone,
    emitter_emission_signature_author character varying,
    transporter_company_siret character varying,
    transporter_company_name character varying,
    transporter_company_address character varying,
    transporter_company_contact character varying,
    transporter_company_mail character varying,
    transporter_company_phone character varying,
    transporter_custom_info character varying,
    transporter_company_vat_number character varying,
    transporter_recepisse_number character varying,
    transporter_recepisse_department character varying,
    transporter_recepisse_validity_limit timestamp without time zone,
    transporter_transport_plates jsonb,
    transporter_transport_taken_over_at timestamp without time zone,
    transporter_transport_signature_date timestamp without time zone,
    transporter_transport_signature_author character varying,
    destination_company_siret character varying,
    destination_company_name character varying,
    destination_company_address character varying,
    destination_company_contact character varying,
    destination_company_mail character varying,
    destination_company_phone character varying,
    destination_custom_info character varying,
    destination_agrement_number character varying,
    destination_reception_date timestamp without time zone,
    destination_reception_quantity integer,
    destination_reception_identification_numbers jsonb,
    destination_reception_identification_type character varying,
    destination_reception_acceptation_status character varying,
    destination_reception_refusal_reason character varying,
    destination_operation_date timestamp without time zone,
    destination_operation_signature_date timestamp without time zone,
    destination_operation_signature_author character varying,
    destination_type character varying,
    destination_operation_next_destination_company_siret character varying,
    destination_operation_next_destination_company_name character varying,
    destination_operation_next_destination_company_address character varying,
    destination_operation_next_destination_company_contact character varying,
    destination_operation_next_destination_company_mail character varying,
    destination_operation_next_destination_company_phone character varying,
    destination_operation_next_destination_company_vat_number character varying,
    identification_numbers jsonb,
    identification_type character varying,
    destination_planned_operation_code text,
    destination_operation_code text,
    weight_value double precision,
    destination_reception_weight double precision,
    emitter_commune character varying,
    emitter_departement character varying,
    emitter_region integer,
    emitter_latitude double precision,
    emitter_longitude double precision,
    emitter_naf character varying,
    destination_commune character varying,
    destination_departement character varying,
    destination_region integer,
    destination_latitude double precision,
    destination_longitude double precision,
    destination_naf character varying
);


ALTER TABLE refined_zone_enriched.bsvhu_enriched OWNER TO pao;

--
-- Name: bordereaux_enriched; Type: VIEW; Schema: refined_zone_enriched; Owner: pao
--

CREATE VIEW refined_zone_enriched.bordereaux_enriched AS
 SELECT 'BSDD'::text AS _bs_type,
    bsdd_enriched.id,
    bsdd_enriched.created_at,
    bsdd_enriched.taken_over_at,
    bsdd_enriched.received_at,
    bsdd_enriched.processed_at,
    bsdd_enriched.status,
    bsdd_enriched.quantity_received,
    bsdd_enriched.processing_operation_done AS processing_operation,
    bsdd_enriched.waste_details_code AS waste_code,
    bsdd_enriched.waste_details_pop AS waste_pop,
    bsdd_enriched.waste_details_is_dangerous AS waste_is_dangerous,
    bsdd_enriched.emitter_company_siret,
    bsdd_enriched.emitter_company_name,
    bsdd_enriched.emitter_company_address,
    bsdd_enriched.emitter_commune,
    bsdd_enriched.emitter_departement,
    bsdd_enriched.emitter_region,
    bsdd_enriched.emitter_naf,
    bsdd_enriched.transporter_company_siret,
    bsdd_enriched.transporter_company_name,
    bsdd_enriched.recipient_company_siret AS destination_company_siret,
    bsdd_enriched.recipient_company_name AS destination_company_name,
    bsdd_enriched.recipient_company_address AS destination_company_address,
    bsdd_enriched.recipient_commune AS destination_commune,
    bsdd_enriched.recipient_departement AS destination_departement,
    bsdd_enriched.recipient_region AS destination_region,
    bsdd_enriched.recipient_naf AS destination_naf
   FROM refined_zone_enriched.bsdd_enriched
  WHERE (NOT bsdd_enriched.is_deleted)
UNION ALL
 SELECT 'BSDA'::text AS _bs_type,
    bsda_enriched.id,
    bsda_enriched.created_at,
    bsda_enriched.transporter_transport_taken_over_at AS taken_over_at,
    bsda_enriched.destination_reception_date AS received_at,
    bsda_enriched.destination_operation_date AS processed_at,
    bsda_enriched.status,
    bsda_enriched.destination_reception_weight AS quantity_received,
    bsda_enriched.destination_operation_code AS processing_operation,
    bsda_enriched.waste_code,
    bsda_enriched.waste_pop,
    NULL::boolean AS waste_is_dangerous,
    bsda_enriched.emitter_company_siret,
    bsda_enriched.emitter_company_name,
    bsda_enriched.emitter_company_address,
    bsda_enriched.emitter_commune,
    bsda_enriched.emitter_departement,
    bsda_enriched.emitter_region,
    bsda_enriched.emitter_naf,
    bsda_enriched.transporter_company_siret,
    bsda_enriched.transporter_company_name,
    bsda_enriched.destination_company_siret,
    bsda_enriched.destination_company_name,
    bsda_enriched.destination_company_address,
    bsda_enriched.destination_commune,
    bsda_enriched.destination_departement,
    bsda_enriched.destination_region,
    bsda_enriched.destination_naf
   FROM refined_zone_enriched.bsda_enriched
  WHERE (NOT bsda_enriched.is_deleted)
UNION ALL
 SELECT 'BSFF'::text AS _bs_type,
    bsff_enriched.id,
    bsff_enriched.created_at,
    bsff_enriched.transporter_transport_taken_over_at AS taken_over_at,
    bsff_enriched.destination_reception_date AS received_at,
    bsff_enriched.destination_operation_signature_date AS processed_at,
    bsff_enriched.status,
    bsff_enriched.destination_reception_weight AS quantity_received,
    bsff_enriched.destination_operation_code AS processing_operation,
    bsff_enriched.waste_code,
    NULL::boolean AS waste_pop,
    NULL::boolean AS waste_is_dangerous,
    bsff_enriched.emitter_company_siret,
    bsff_enriched.emitter_company_name,
    bsff_enriched.emitter_company_address,
    bsff_enriched.emitter_commune,
    bsff_enriched.emitter_departement,
    bsff_enriched.emitter_region,
    bsff_enriched.emitter_naf,
    bsff_enriched.transporter_company_siret,
    bsff_enriched.transporter_company_name,
    bsff_enriched.destination_company_siret,
    bsff_enriched.destination_company_name,
    bsff_enriched.destination_company_address,
    bsff_enriched.destination_commune,
    bsff_enriched.destination_departement,
    bsff_enriched.destination_region,
    bsff_enriched.destination_naf
   FROM refined_zone_enriched.bsff_enriched
  WHERE (NOT bsff_enriched.is_deleted)
UNION ALL
 SELECT 'BSDASRI'::text AS _bs_type,
    bsdasri_enriched.id,
    bsdasri_enriched.created_at,
    bsdasri_enriched.transporter_taken_over_at AS taken_over_at,
    bsdasri_enriched.destination_reception_date AS received_at,
    bsdasri_enriched.destination_operation_date AS processed_at,
    bsdasri_enriched.status,
    bsdasri_enriched.destination_reception_waste_weight_value AS quantity_received,
    bsdasri_enriched.destination_operation_code AS processing_operation,
    bsdasri_enriched.waste_code,
    NULL::boolean AS waste_pop,
    NULL::boolean AS waste_is_dangerous,
    bsdasri_enriched.emitter_company_siret,
    bsdasri_enriched.emitter_company_name,
    bsdasri_enriched.emitter_company_address,
    bsdasri_enriched.emitter_commune,
    bsdasri_enriched.emitter_departement,
    bsdasri_enriched.emitter_region,
    bsdasri_enriched.emitter_naf,
    bsdasri_enriched.transporter_company_siret,
    bsdasri_enriched.transporter_company_name,
    bsdasri_enriched.destination_company_siret,
    bsdasri_enriched.destination_company_name,
    bsdasri_enriched.destination_company_address,
    bsdasri_enriched.destination_commune,
    bsdasri_enriched.destination_departement,
    bsdasri_enriched.destination_region,
    bsdasri_enriched.destination_naf
   FROM refined_zone_enriched.bsdasri_enriched
  WHERE (NOT bsdasri_enriched.is_deleted)
UNION ALL
 SELECT 'BSVHU'::text AS _bs_type,
    bsvhu_enriched.id,
    bsvhu_enriched.created_at,
    bsvhu_enriched.transporter_transport_taken_over_at AS taken_over_at,
    bsvhu_enriched.destination_reception_date AS received_at,
    bsvhu_enriched.destination_operation_date AS processed_at,
    bsvhu_enriched.status,
    bsvhu_enriched.destination_reception_weight AS quantity_received,
    bsvhu_enriched.destination_operation_code AS processing_operation,
    bsvhu_enriched.waste_code,
    NULL::boolean AS waste_pop,
    NULL::boolean AS waste_is_dangerous,
    bsvhu_enriched.emitter_company_siret,
    bsvhu_enriched.emitter_company_name,
    bsvhu_enriched.emitter_company_address,
    bsvhu_enriched.emitter_commune,
    bsvhu_enriched.emitter_departement,
    bsvhu_enriched.emitter_region,
    bsvhu_enriched.emitter_naf,
    bsvhu_enriched.transporter_company_siret,
    bsvhu_enriched.transporter_company_name,
    bsvhu_enriched.destination_company_siret,
    bsvhu_enriched.destination_company_name,
    bsvhu_enriched.destination_company_address,
    bsvhu_enriched.destination_commune,
    bsvhu_enriched.destination_departement,
    bsvhu_enriched.destination_region,
    bsvhu_enriched.destination_naf
   FROM refined_zone_enriched.bsvhu_enriched
  WHERE (NOT bsvhu_enriched.is_deleted);


ALTER TABLE refined_zone_enriched.bordereaux_enriched OWNER TO pao;

--
-- Name: company_enriched; Type: TABLE; Schema: refined_zone_enriched; Owner: pao
--

CREATE TABLE refined_zone_enriched.company_enriched (
    id character varying,
    siret character varying,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    security_code integer,
    name character varying,
    gerep_id character varying,
    code_naf character varying,
    given_name character varying,
    contact_email character varying,
    contact_phone character varying,
    website character varying,
    transporter_receipt_id character varying,
    trader_receipt_id character varying,
    eco_organisme_agreements jsonb,
    company_types jsonb,
    address character varying,
    latitude double precision,
    longitude double precision,
    broker_receipt_id character varying,
    verification_code character varying,
    verification_status character varying,
    verification_mode character varying,
    verification_comment character varying,
    verified_at timestamp without time zone,
    vhu_agrement_demolisseur_id character varying,
    vhu_agrement_broyeur_id character varying,
    allow_bsdasri_take_over_without_signature boolean,
    vat_number character varying,
    contact character varying,
    code_departement character varying,
    worker_certification_id character varying,
    code_section character varying,
    libelle_section character varying,
    code_division character varying,
    libelle_division character varying,
    code_groupe character varying,
    libelle_groupe character varying,
    code_classe character varying,
    libelle_classe character varying,
    code_sous_classe character varying,
    libelle_sous_classe character varying,
    etat_administratif_etablissement character varying,
    code_commune_insee character varying,
    code_departement_insee text,
    code_region_insee integer
);


ALTER TABLE refined_zone_enriched.company_enriched OWNER TO pao;

--
-- Name: icpe_siretise; Type: TABLE; Schema: refined_zone_icpe; Owner: pao
--

CREATE TABLE refined_zone_icpe.icpe_siretise (
    inserted_at timestamp without time zone,
    code_s3ic text,
    id_nomenclature text,
    date_debut_exploitation date,
    date_fin_validite date,
    volume double precision,
    unite text,
    statut_ic boolean,
    rubrique text,
    alinea text,
    libelle_court_activite text,
    en_vigueur boolean,
    id_regime text,
    siret_icpe text,
    nom_etablissement_icpe text,
    siret_gerep character varying,
    etat_administratif_etablissement character varying,
    rubrique_alinea text,
    siret_clean text,
    inscrit_sur_td boolean
);


ALTER TABLE refined_zone_icpe.icpe_siretise OWNER TO pao;

--
-- Name: icpe_stats_rubriques_alinea; Type: TABLE; Schema: refined_zone_icpe; Owner: pao
--

CREATE TABLE refined_zone_icpe.icpe_stats_rubriques_alinea (
    inserted_at timestamp without time zone,
    rubrique text,
    alinea text,
    "Nombre d'installations classées" bigint,
    "Nombre d'établissements aprés siretisation" bigint,
    "Nombre d'établissements actifs aprés siretisation" bigint,
    "Nombre d'établissements actifs aprés siretisation et inscrits" bigint,
    "Pourcentage d'établissements inscrits sur TD" bigint
);


ALTER TABLE refined_zone_icpe.icpe_stats_rubriques_alinea OWNER TO pao;

--
-- Name: reconciliation_exutoires_georisques_td; Type: TABLE; Schema: refined_zone_icpe; Owner: pao
--

CREATE TABLE refined_zone_icpe.reconciliation_exutoires_georisques_td (
    inscrit_sur_trackdechets boolean,
    siret text,
    nom_etablissement text,
    codes_s3ic text[],
    rubriques_autorises text[],
    num_bsdd bigint,
    tonnage_bsdd double precision,
    operations_effectues_bsdd text[],
    num_bsda bigint,
    tonnage_bsda double precision,
    operations_effectues_bsda text[],
    num_bsff bigint,
    volume_contenant_bsff double precision,
    tonnage_contenant_bsff double precision,
    tonnage_accepte_contenant_bsff double precision,
    operations_effectues_bsff character varying[]
);


ALTER TABLE refined_zone_icpe.reconciliation_exutoires_georisques_td OWNER TO pao;

--
-- Name: annual_quantity_processed_by_bordereaux_type; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.annual_quantity_processed_by_bordereaux_type (
    _bs_type text,
    year_of_processing double precision,
    quantity_processed double precision
);


ALTER TABLE refined_zone_stats_publiques.annual_quantity_processed_by_bordereaux_type OWNER TO pao;

--
-- Name: annual_quantity_processed_by_processing_operation; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.annual_quantity_processed_by_processing_operation (
    processing_operation text,
    year_of_processing double precision,
    quantity_processed double precision
);


ALTER TABLE refined_zone_stats_publiques.annual_quantity_processed_by_processing_operation OWNER TO pao;

--
-- Name: annual_quantity_processed_by_processing_type; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.annual_quantity_processed_by_processing_type (
    year_of_processing double precision,
    operation_type text,
    quantity_processed double precision
);


ALTER TABLE refined_zone_stats_publiques.annual_quantity_processed_by_processing_type OWNER TO pao;

--
-- Name: bsda_created_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsda_created_by_week (
    week timestamp without time zone,
    created bigint,
    quantity_tracked double precision
);


ALTER TABLE refined_zone_stats_publiques.bsda_created_by_week OWNER TO pao;

--
-- Name: bsda_emitted_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsda_emitted_by_week (
    week timestamp without time zone,
    emitted bigint,
    quantity_emitted double precision
);


ALTER TABLE refined_zone_stats_publiques.bsda_emitted_by_week OWNER TO pao;

--
-- Name: bsda_processed_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsda_processed_by_week (
    week timestamp without time zone,
    processed bigint,
    quantity_processed double precision,
    processed_non_final_operation bigint,
    processed_final_operation bigint,
    quantity_processed_non_final_operation double precision,
    quantity_processed_final_operation double precision
);


ALTER TABLE refined_zone_stats_publiques.bsda_processed_by_week OWNER TO pao;

--
-- Name: bsda_received_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsda_received_by_week (
    week timestamp without time zone,
    received bigint,
    quantity_received double precision
);


ALTER TABLE refined_zone_stats_publiques.bsda_received_by_week OWNER TO pao;

--
-- Name: bsda_sent_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsda_sent_by_week (
    week timestamp without time zone,
    sent bigint,
    quantity_sent double precision
);


ALTER TABLE refined_zone_stats_publiques.bsda_sent_by_week OWNER TO pao;

--
-- Name: bsda_statistiques_hebdomadaires; Type: VIEW; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE VIEW refined_zone_stats_publiques.bsda_statistiques_hebdomadaires AS
 SELECT week,
    bsda_created_by_week.created,
    bsda_created_by_week.quantity_tracked,
    bsda_emitted_by_week.emitted,
    bsda_emitted_by_week.quantity_emitted,
    bsda_sent_by_week.sent,
    bsda_sent_by_week.quantity_sent,
    bsda_received_by_week.received,
    bsda_received_by_week.quantity_received,
    bsda_processed_by_week.processed,
    bsda_processed_by_week.quantity_processed,
    bsda_processed_by_week.processed_non_final_operation,
    bsda_processed_by_week.processed_final_operation,
    bsda_processed_by_week.quantity_processed_non_final_operation,
    bsda_processed_by_week.quantity_processed_final_operation
   FROM ((((refined_zone_stats_publiques.bsda_created_by_week
     FULL JOIN refined_zone_stats_publiques.bsda_emitted_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsda_sent_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsda_received_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsda_processed_by_week USING (week));


ALTER TABLE refined_zone_stats_publiques.bsda_statistiques_hebdomadaires OWNER TO pao;

--
-- Name: bsdasri_created_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsdasri_created_by_week (
    week timestamp without time zone,
    created bigint,
    quantity_tracked double precision
);


ALTER TABLE refined_zone_stats_publiques.bsdasri_created_by_week OWNER TO pao;

--
-- Name: bsdasri_emitted_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsdasri_emitted_by_week (
    week timestamp without time zone,
    emitted bigint,
    quantity_emitted double precision
);


ALTER TABLE refined_zone_stats_publiques.bsdasri_emitted_by_week OWNER TO pao;

--
-- Name: bsdasri_processed_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsdasri_processed_by_week (
    week timestamp without time zone,
    processed bigint,
    quantity_processed double precision,
    processed_non_final_operation bigint,
    processed_final_operation bigint,
    quantity_processed_non_final_operation double precision,
    quantity_processed_final_operation double precision
);


ALTER TABLE refined_zone_stats_publiques.bsdasri_processed_by_week OWNER TO pao;

--
-- Name: bsdasri_received_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsdasri_received_by_week (
    week timestamp without time zone,
    received bigint,
    quantity_received double precision
);


ALTER TABLE refined_zone_stats_publiques.bsdasri_received_by_week OWNER TO pao;

--
-- Name: bsdasri_sent_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsdasri_sent_by_week (
    week timestamp without time zone,
    sent bigint,
    quantity_sent double precision
);


ALTER TABLE refined_zone_stats_publiques.bsdasri_sent_by_week OWNER TO pao;

--
-- Name: bsdasri_statistiques_hebdomadaires; Type: VIEW; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE VIEW refined_zone_stats_publiques.bsdasri_statistiques_hebdomadaires AS
 SELECT week,
    bsdasri_created_by_week.created,
    bsdasri_created_by_week.quantity_tracked,
    bsdasri_emitted_by_week.emitted,
    bsdasri_emitted_by_week.quantity_emitted,
    bsdasri_sent_by_week.sent,
    bsdasri_sent_by_week.quantity_sent,
    bsdasri_received_by_week.received,
    bsdasri_received_by_week.quantity_received,
    bsdasri_processed_by_week.processed,
    bsdasri_processed_by_week.quantity_processed,
    bsdasri_processed_by_week.processed_non_final_operation,
    bsdasri_processed_by_week.processed_final_operation,
    bsdasri_processed_by_week.quantity_processed_non_final_operation,
    bsdasri_processed_by_week.quantity_processed_final_operation
   FROM ((((refined_zone_stats_publiques.bsdasri_created_by_week
     FULL JOIN refined_zone_stats_publiques.bsdasri_emitted_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsdasri_sent_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsdasri_received_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsdasri_processed_by_week USING (week));


ALTER TABLE refined_zone_stats_publiques.bsdasri_statistiques_hebdomadaires OWNER TO pao;

--
-- Name: bsdd_created_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsdd_created_by_week (
    week timestamp without time zone,
    created bigint,
    quantity_tracked double precision
);


ALTER TABLE refined_zone_stats_publiques.bsdd_created_by_week OWNER TO pao;

--
-- Name: bsdd_emitted_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsdd_emitted_by_week (
    week timestamp without time zone,
    emitted bigint,
    quantity_emitted double precision
);


ALTER TABLE refined_zone_stats_publiques.bsdd_emitted_by_week OWNER TO pao;

--
-- Name: bsdd_processed_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsdd_processed_by_week (
    week timestamp without time zone,
    processed bigint,
    quantity_processed double precision,
    processed_non_final_operation bigint,
    processed_final_operation bigint,
    quantity_processed_non_final_operation double precision,
    quantity_processed_final_operation double precision
);


ALTER TABLE refined_zone_stats_publiques.bsdd_processed_by_week OWNER TO pao;

--
-- Name: bsdd_received_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsdd_received_by_week (
    week timestamp without time zone,
    received bigint,
    quantity_received double precision
);


ALTER TABLE refined_zone_stats_publiques.bsdd_received_by_week OWNER TO pao;

--
-- Name: bsdd_sent_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsdd_sent_by_week (
    week timestamp without time zone,
    sent bigint,
    quantity_sent double precision
);


ALTER TABLE refined_zone_stats_publiques.bsdd_sent_by_week OWNER TO pao;

--
-- Name: bsdd_statistiques_hebdomadaires; Type: VIEW; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE VIEW refined_zone_stats_publiques.bsdd_statistiques_hebdomadaires AS
 SELECT week,
    bsdd_created_by_week.created,
    bsdd_created_by_week.quantity_tracked,
    bsdd_emitted_by_week.emitted,
    bsdd_emitted_by_week.quantity_emitted,
    bsdd_sent_by_week.sent,
    bsdd_sent_by_week.quantity_sent,
    bsdd_received_by_week.received,
    bsdd_received_by_week.quantity_received,
    bsdd_processed_by_week.processed,
    bsdd_processed_by_week.quantity_processed,
    bsdd_processed_by_week.processed_non_final_operation,
    bsdd_processed_by_week.processed_final_operation,
    bsdd_processed_by_week.quantity_processed_non_final_operation,
    bsdd_processed_by_week.quantity_processed_final_operation
   FROM ((((refined_zone_stats_publiques.bsdd_created_by_week
     FULL JOIN refined_zone_stats_publiques.bsdd_emitted_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsdd_sent_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsdd_received_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsdd_processed_by_week USING (week));


ALTER TABLE refined_zone_stats_publiques.bsdd_statistiques_hebdomadaires OWNER TO pao;

--
-- Name: bsff_created_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsff_created_by_week (
    week timestamp without time zone,
    created bigint,
    quantity_tracked double precision
);


ALTER TABLE refined_zone_stats_publiques.bsff_created_by_week OWNER TO pao;

--
-- Name: bsff_emitted_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsff_emitted_by_week (
    week timestamp without time zone,
    emitted bigint,
    quantity_emitted double precision
);


ALTER TABLE refined_zone_stats_publiques.bsff_emitted_by_week OWNER TO pao;

--
-- Name: bsff_packagings_processed_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsff_packagings_processed_by_week (
    week timestamp without time zone,
    packagings_processed bigint,
    packagings_quantity_rpcoessed double precision,
    packagings_processed_non_final_operation bigint,
    packagings_processed_final_operation bigint,
    packagings_quantity_rpcoessed_non_final_operation double precision,
    packagings_quantity_rpcoessed_final_operation double precision
);


ALTER TABLE refined_zone_stats_publiques.bsff_packagings_processed_by_week OWNER TO pao;

--
-- Name: bsff_received_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsff_received_by_week (
    week timestamp without time zone,
    received bigint,
    quantity_received double precision
);


ALTER TABLE refined_zone_stats_publiques.bsff_received_by_week OWNER TO pao;

--
-- Name: bsff_sent_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsff_sent_by_week (
    week timestamp without time zone,
    sent bigint,
    quantity_sent double precision
);


ALTER TABLE refined_zone_stats_publiques.bsff_sent_by_week OWNER TO pao;

--
-- Name: bsff_statistiques_hebdomadaires; Type: VIEW; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE VIEW refined_zone_stats_publiques.bsff_statistiques_hebdomadaires AS
 SELECT week,
    bsff_created_by_week.created,
    bsff_created_by_week.quantity_tracked,
    bsff_emitted_by_week.emitted,
    bsff_emitted_by_week.quantity_emitted,
    bsff_sent_by_week.sent,
    bsff_sent_by_week.quantity_sent,
    bsff_received_by_week.received,
    bsff_received_by_week.quantity_received,
    bsff_packagings_processed_by_week.packagings_processed,
    bsff_packagings_processed_by_week.packagings_quantity_rpcoessed,
    bsff_packagings_processed_by_week.packagings_processed_non_final_operation,
    bsff_packagings_processed_by_week.packagings_processed_final_operation,
    bsff_packagings_processed_by_week.packagings_quantity_rpcoessed_non_final_operation,
    bsff_packagings_processed_by_week.packagings_quantity_rpcoessed_final_operation
   FROM ((((refined_zone_stats_publiques.bsff_created_by_week
     FULL JOIN refined_zone_stats_publiques.bsff_emitted_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsff_sent_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsff_received_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsff_packagings_processed_by_week USING (week));


ALTER TABLE refined_zone_stats_publiques.bsff_statistiques_hebdomadaires OWNER TO pao;

--
-- Name: bsvhu_created_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsvhu_created_by_week (
    week timestamp without time zone,
    created bigint,
    quantity_tracked double precision
);


ALTER TABLE refined_zone_stats_publiques.bsvhu_created_by_week OWNER TO pao;

--
-- Name: bsvhu_emitted_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsvhu_emitted_by_week (
    week timestamp without time zone,
    emitted bigint,
    quantity_emitted double precision
);


ALTER TABLE refined_zone_stats_publiques.bsvhu_emitted_by_week OWNER TO pao;

--
-- Name: bsvhu_processed_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsvhu_processed_by_week (
    week timestamp without time zone,
    processed bigint,
    quantity_processed double precision,
    processed_non_final_operation bigint,
    processed_final_operation bigint,
    quantity_processed_non_final_operation double precision,
    quantity_processed_final_operation double precision
);


ALTER TABLE refined_zone_stats_publiques.bsvhu_processed_by_week OWNER TO pao;

--
-- Name: bsvhu_received_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsvhu_received_by_week (
    week timestamp without time zone,
    received bigint,
    quantity_received double precision
);


ALTER TABLE refined_zone_stats_publiques.bsvhu_received_by_week OWNER TO pao;

--
-- Name: bsvhu_sent_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.bsvhu_sent_by_week (
    week timestamp without time zone,
    sent bigint,
    quantity_sent double precision
);


ALTER TABLE refined_zone_stats_publiques.bsvhu_sent_by_week OWNER TO pao;

--
-- Name: bsvhu_statistiques_hebdomadaires; Type: VIEW; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE VIEW refined_zone_stats_publiques.bsvhu_statistiques_hebdomadaires AS
 SELECT week,
    bsvhu_created_by_week.created,
    bsvhu_created_by_week.quantity_tracked,
    bsvhu_emitted_by_week.emitted,
    bsvhu_emitted_by_week.quantity_emitted,
    bsvhu_sent_by_week.sent,
    bsvhu_sent_by_week.quantity_sent,
    bsvhu_received_by_week.received,
    bsvhu_received_by_week.quantity_received,
    bsvhu_processed_by_week.processed,
    bsvhu_processed_by_week.quantity_processed,
    bsvhu_processed_by_week.processed_non_final_operation,
    bsvhu_processed_by_week.processed_final_operation,
    bsvhu_processed_by_week.quantity_processed_non_final_operation,
    bsvhu_processed_by_week.quantity_processed_final_operation
   FROM ((((refined_zone_stats_publiques.bsvhu_created_by_week
     FULL JOIN refined_zone_stats_publiques.bsvhu_emitted_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsvhu_sent_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsvhu_received_by_week USING (week))
     FULL JOIN refined_zone_stats_publiques.bsvhu_processed_by_week USING (week));


ALTER TABLE refined_zone_stats_publiques.bsvhu_statistiques_hebdomadaires OWNER TO pao;

--
-- Name: companies_created_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.companies_created_by_week (
    week_of_creation timestamp without time zone,
    count bigint
);


ALTER TABLE refined_zone_stats_publiques.companies_created_by_week OWNER TO pao;

--
-- Name: number_of_bordereaux_created_by_year_and_type; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.number_of_bordereaux_created_by_year_and_type (
    _bs_type text,
    year_of_creation double precision,
    count bigint
);


ALTER TABLE refined_zone_stats_publiques.number_of_bordereaux_created_by_year_and_type OWNER TO pao;

--
-- Name: total_bordereaux_created; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.total_bordereaux_created (
    _bs_type text,
    year double precision,
    count bigint
);


ALTER TABLE refined_zone_stats_publiques.total_bordereaux_created OWNER TO pao;

--
-- Name: users_created_by_week; Type: TABLE; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE TABLE refined_zone_stats_publiques.users_created_by_week (
    week_of_creation timestamp without time zone,
    count bigint
);


ALTER TABLE refined_zone_stats_publiques.users_created_by_week OWNER TO pao;

--
-- Name: base_codes_postaux; Type: VIEW; Schema: trusted_zone; Owner: pao
--

CREATE VIEW trusted_zone.base_codes_postaux AS
 SELECT laposte_hexasmal.code_commune_insee,
    laposte_hexasmal.code_postal,
    laposte_hexasmal.nom_commune,
    laposte_hexasmal.ligne_5,
    laposte_hexasmal."libellé_d_acheminement" AS libelle_acheminement,
    (split_part((laposte_hexasmal.coordonnees_gps)::text, ','::text, 1))::double precision AS latitude,
    (split_part((laposte_hexasmal.coordonnees_gps)::text, ','::text, 2))::double precision AS longitude
   FROM raw_zone.laposte_hexasmal;


ALTER TABLE trusted_zone.base_codes_postaux OWNER TO pao;

--
-- Name: code_dechets; Type: TABLE; Schema: trusted_zone; Owner: pao
--

CREATE TABLE trusted_zone.code_dechets (
    code character varying,
    description character varying
);


ALTER TABLE trusted_zone.code_dechets OWNER TO pao;

--
-- Name: codes_operations_traitements; Type: VIEW; Schema: trusted_zone; Owner: pao
--

CREATE VIEW trusted_zone.codes_operations_traitements AS
 SELECT replace((codes_operations_traitements.code)::text, ' '::text, ''::text) AS code,
    codes_operations_traitements.description
   FROM raw_zone.codes_operations_traitements;


ALTER TABLE trusted_zone.codes_operations_traitements OWNER TO pao;

--
-- Name: coordonnees-epci-fp-2022-last; Type: TABLE; Schema: trusted_zone; Owner: pao
--

CREATE TABLE trusted_zone."coordonnees-epci-fp-2022-last" (
    "Région siège" character varying(500),
    "Département siège" character varying(500),
    "Arrondissement siège" character varying(500),
    "Commune siège" character varying(500),
    siren character varying,
    "Nom du groupement" character varying(500),
    "Nature juridique" character varying(500),
    "Syndicat à la carte" integer,
    "Groupement interdépartemental" integer,
    "Date de création" character varying(500),
    "Date d'effet" character varying(500),
    "Mode de répartition des sièges" character varying(500),
    "Autre mode de répartition des sièges" character varying(2048),
    "Nombre de membres" integer,
    population integer,
    "Nombre de compétences exercées" integer,
    "Mode de financement" character varying(500),
    "DGF Bonifiée" integer,
    dsc integer,
    reom integer,
    "Autre redevance" character varying(500),
    teom integer,
    "Autre taxe" character varying(500),
    "Civilité Président" character varying(500),
    "Prénom Président" character varying(500),
    "Nom Président" character varying(500),
    "Adresse du siège_1" character varying(500),
    "Adresse du siège_2" character varying(500),
    "Adresse du siège_3" character varying(500),
    "Code postal du siège - Ville du siège" character varying(500),
    "Téléphone du siège" character varying(500),
    "Fax du siège" character varying(500),
    "Courriel du siège" character varying(500),
    "Site internet" character varying(500),
    "Adresse annexe_1" character varying(500),
    "Adresse annexe_2" character varying(500),
    "Adresse annexe_3" character varying(500),
    "Code postal annexe - Ville annexe" character varying(500),
    "Téléphone annexe" character varying(500),
    "Fax annexe" character varying(500)
);


ALTER TABLE trusted_zone."coordonnees-epci-fp-2022-last" OWNER TO pao;

--
-- Name: eco_organismes_agrees_2022; Type: TABLE; Schema: trusted_zone; Owner: pao
--

CREATE TABLE trusted_zone.eco_organismes_agrees_2022 (
    siret text,
    raison_sociale text,
    nom_eco_organisme text,
    filiere_dsrep text,
    produits_relevant_filiere_responsabilite_elargie text,
    adresse text,
    code_postal text,
    ville text
);


ALTER TABLE trusted_zone.eco_organismes_agrees_2022 OWNER TO pao;

--
-- Name: gerep_2016_2017_producteurs; Type: TABLE; Schema: trusted_zone; Owner: pao
--

CREATE TABLE trusted_zone.gerep_2016_2017_producteurs (
    annee character varying,
    code_etablissement character varying,
    nom_etablissement character varying,
    adresse_site_exploitation character varying,
    code_postal_etablissement character varying,
    commune character varying,
    code_insee character varying,
    code_ape character varying,
    numero_siret character varying,
    nom_contact character varying,
    fonction_contact character varying,
    tel_contact character varying,
    mail_contact character varying,
    code_dechet_produit character varying,
    dechet_produit character varying
);


ALTER TABLE trusted_zone.gerep_2016_2017_producteurs OWNER TO pao;

--
-- Name: gerep_2016_2017_traiteurs; Type: TABLE; Schema: trusted_zone; Owner: pao
--

CREATE TABLE trusted_zone.gerep_2016_2017_traiteurs (
    annee character varying,
    code_etablissement character varying,
    nom_etablissement character varying,
    adresse_site_exploitation character varying,
    code_postal_etablissement character varying,
    commune character varying,
    code_insee character varying,
    numero_siret character varying,
    code_ape character varying,
    nom_contact character varying,
    tel_contact character varying,
    fonction_contact character varying,
    mail_contact character varying,
    code_dechet_traite character varying,
    dechet_traite character varying
);


ALTER TABLE trusted_zone.gerep_2016_2017_traiteurs OWNER TO pao;

--
-- Name: liste_declarants_syderep; Type: TABLE; Schema: trusted_zone; Owner: pao
--

CREATE TABLE trusted_zone.liste_declarants_syderep (
    filiere text,
    statut_inscription text,
    raison_sociale text,
    siren_siret text,
    code_naf text,
    categorie_acteur text,
    type_declarant text,
    adresse_1 text,
    adresse_2 text,
    adresse_3 text,
    code_postal text,
    ville text,
    pays text,
    nom_contact_referent_acteur text,
    prenom_contact_referent_acteur text,
    mail_contact_referent_acteur text,
    tel_contact_referent_acteur text,
    nom_contact_referent_filiere text,
    prenom_contact_referent_filiere text,
    mail_contact_referent_filiere text,
    tel_contact_referent_filiere text
);


ALTER TABLE trusted_zone.liste_declarants_syderep OWNER TO pao;

--
-- Name: mapping_rubrique_code_operation; Type: TABLE; Schema: trusted_zone; Owner: pao
--

CREATE TABLE trusted_zone.mapping_rubrique_code_operation (
    code_operation text,
    rubrique text
);


ALTER TABLE trusted_zone.mapping_rubrique_code_operation OWNER TO pao;

--
-- Name: operateurs_fluides_frigo; Type: TABLE; Schema: trusted_zone; Owner: pao
--

CREATE TABLE trusted_zone.operateurs_fluides_frigo (
    raison_sociale character varying,
    siren_siret character varying,
    code_departement character varying,
    code_region integer,
    code_postal character varying,
    ville character varying,
    secteur_activite character varying,
    attestation_ou_certificat character varying,
    categorie_attestation character varying
);


ALTER TABLE trusted_zone.operateurs_fluides_frigo OWNER TO pao;

--
-- Name: collectivites; Type: VIEW; Schema: trusted_zone_gsheet; Owner: pao
--

CREATE VIEW trusted_zone_gsheet.collectivites AS
 SELECT "coordonnees-epci-fp-2022-last"."SIREN" AS siren,
    "coordonnees-epci-fp-2022-last"."Région siège" AS region_siege,
    "coordonnees-epci-fp-2022-last"."Département siège" AS departement_siege,
    "coordonnees-epci-fp-2022-last"."Arrondissement siège" AS arrondissement_siege,
    "coordonnees-epci-fp-2022-last"."Commune siège" AS commune_siege,
    "coordonnees-epci-fp-2022-last"."Nom du groupement" AS nom_du_groupement,
    "coordonnees-epci-fp-2022-last"."Nature juridique" AS nature_juridique,
    ("coordonnees-epci-fp-2022-last"."Syndicat à la carte")::boolean AS syndicat_a_la_carte,
    ("coordonnees-epci-fp-2022-last"."Groupement interdépartemental")::boolean AS "groupement_interdépartemental",
    ("coordonnees-epci-fp-2022-last"."Date de création")::date AS date_creation,
    ("coordonnees-epci-fp-2022-last"."Date d'effet")::date AS date_effet,
    "coordonnees-epci-fp-2022-last"."Mode de répartition des sièges" AS mode_repartition_siege,
    "coordonnees-epci-fp-2022-last"."Autre mode de répartition des sièges" AS autre_mode_repartition_siege,
    "coordonnees-epci-fp-2022-last"."Nombre de membres" AS nombre_membres,
    "coordonnees-epci-fp-2022-last".population,
    "coordonnees-epci-fp-2022-last"."Nombre de compétences exercées" AS nombre_competences_exercees,
    "coordonnees-epci-fp-2022-last"."Mode de financement" AS mode_financement,
    ("coordonnees-epci-fp-2022-last"."DGF Bonifiée")::boolean AS dgf_bonifiee,
    ("coordonnees-epci-fp-2022-last".dsc)::boolean AS dsc,
    ("coordonnees-epci-fp-2022-last".reom)::boolean AS reom,
    "coordonnees-epci-fp-2022-last"."Autre redevance" AS autre_redevance,
    ("coordonnees-epci-fp-2022-last".teom)::boolean AS teom,
    "coordonnees-epci-fp-2022-last"."Autre taxe" AS autre_taxe,
    "coordonnees-epci-fp-2022-last"."Civilité Président" AS civilite_president,
    "coordonnees-epci-fp-2022-last"."Prénom Président" AS prenom_president,
    "coordonnees-epci-fp-2022-last"."Nom Président" AS nom_president,
    "coordonnees-epci-fp-2022-last"."Adresse du siège_1" AS adresse_siege_1,
    "coordonnees-epci-fp-2022-last"."Adresse du siège_2" AS adresse_siege_2,
    "coordonnees-epci-fp-2022-last"."Adresse du siège_3" AS adresse_siege_3,
    "coordonnees-epci-fp-2022-last"."Code postal du siège - Ville du siège" AS code_postal_ville_siege,
    "coordonnees-epci-fp-2022-last"."Téléphone du siège" AS telephone_siege,
    "coordonnees-epci-fp-2022-last"."Fax du siège" AS fax_siege,
    "coordonnees-epci-fp-2022-last"."Courriel du siège" AS courriel_siege,
    "coordonnees-epci-fp-2022-last"."Site internet" AS site_internet,
    "coordonnees-epci-fp-2022-last"."Adresse annexe_1" AS adresse_annexe_1,
    "coordonnees-epci-fp-2022-last"."Adresse annexe_2" AS adresse_annexe_2,
    "coordonnees-epci-fp-2022-last"."Adresse annexe_3" AS adresse_annexe_3,
    "coordonnees-epci-fp-2022-last"."Code postal annexe - Ville annexe" AS code_postal_ville_annexe,
    "coordonnees-epci-fp-2022-last"."Téléphone annexe" AS telephone_annexe,
    "coordonnees-epci-fp-2022-last"."Fax annexe" AS faxe_annexe
   FROM raw_zone_gsheet."coordonnees-epci-fp-2022-last";


ALTER TABLE trusted_zone_gsheet.collectivites OWNER TO pao;

--
-- Name: collectivites_competence_dechets; Type: VIEW; Schema: trusted_zone_gsheet; Owner: pao
--

CREATE VIEW trusted_zone_gsheet.collectivites_competence_dechets AS
 SELECT collectivites_compentence_dechets.siren_epci AS siren,
    collectivites_compentence_dechets.nom_complet AS nom,
    collectivites_compentence_dechets.dep_epci AS code_departement,
    collectivites_compentence_dechets.nj_epci2023,
    collectivites_compentence_dechets.fisc_epci2023,
    collectivites_compentence_dechets.nb_com_2023,
    collectivites_compentence_dechets.ptot_epci_2023,
    collectivites_compentence_dechets.pmun_epci_2023
   FROM raw_zone_gsheet.collectivites_compentence_dechets;


ALTER TABLE trusted_zone_gsheet.collectivites_competence_dechets OWNER TO pao;

--
-- Name: eco_organismes_agrees_2022; Type: VIEW; Schema: trusted_zone_gsheet; Owner: pao
--

CREATE VIEW trusted_zone_gsheet.eco_organismes_agrees_2022 AS
 SELECT eco_organismes_agrees_2022.siret,
    eco_organismes_agrees_2022.raison_sociale,
    eco_organismes_agrees_2022.nom_eco_organisme,
    eco_organismes_agrees_2022.filiere_dsrep,
    eco_organismes_agrees_2022.produits_relevant_filiere_responsabilite_elargie,
    eco_organismes_agrees_2022.adresse,
    eco_organismes_agrees_2022.code_postal,
    eco_organismes_agrees_2022.ville
   FROM raw_zone_gsheet.eco_organismes_agrees_2022;


ALTER TABLE trusted_zone_gsheet.eco_organismes_agrees_2022 OWNER TO pao;

--
-- Name: gerep_amiante; Type: TABLE; Schema: trusted_zone_gsheet; Owner: pao
--

CREATE TABLE trusted_zone_gsheet.gerep_amiante (
    index bigint,
    adresse_site_exploitation text,
    code_postal_etablissement text,
    commune text,
    code_insee text,
    code_ape text,
    numero_siret text,
    nom_contact text,
    fonction_contact text,
    tel_contact text,
    mail_contact text,
    "code_déchet_produit" text,
    "déchet_produit" text
);


ALTER TABLE trusted_zone_gsheet.gerep_amiante OWNER TO pao;

--
-- Name: gerep_exutoires_dasri; Type: TABLE; Schema: trusted_zone_gsheet; Owner: pao
--

CREATE TABLE trusted_zone_gsheet.gerep_exutoires_dasri (
    nom_etablissement text,
    adresse_site_exploitation text,
    code_postal_etablisement text,
    commune text,
    numero_siret text,
    nom_contact text,
    tel_contact text,
    fonction_contact text,
    mail_contact text,
    code_dechet_traite text,
    dechet_traite text
);


ALTER TABLE trusted_zone_gsheet.gerep_exutoires_dasri OWNER TO pao;

--
-- Name: gerep_producteurs_dasri; Type: TABLE; Schema: trusted_zone_gsheet; Owner: pao
--

CREATE TABLE trusted_zone_gsheet.gerep_producteurs_dasri (
    nom_etablissement text,
    adresse_site_exploitation text,
    code_postal_etablisement text,
    commune text,
    code_insee text,
    numero_siret text,
    nom_contact text,
    fonction_contact text,
    tel_contact text,
    mail_contact text,
    code_dechet_produit text,
    dechet_produit text
);


ALTER TABLE trusted_zone_gsheet.gerep_producteurs_dasri OWNER TO pao;

--
-- Name: gerep_traiteurs; Type: VIEW; Schema: trusted_zone_gsheet; Owner: pao
--

CREATE VIEW trusted_zone_gsheet.gerep_traiteurs AS
 SELECT gerep_2016_2017_traiteurs.annee,
    gerep_2016_2017_traiteurs.code_etablissement AS code_s3ic,
    gerep_2016_2017_traiteurs.numero_siret,
    gerep_2016_2017_traiteurs.nom_etablissement,
    gerep_2016_2017_traiteurs.code_dechet_traite,
    gerep_2016_2017_traiteurs.dechet_traite,
    gerep_2016_2017_traiteurs.adresse_site_exploitation,
    gerep_2016_2017_traiteurs.code_postal_etablissement,
    gerep_2016_2017_traiteurs.commune,
    gerep_2016_2017_traiteurs.code_insee AS code_commune_insee,
    gerep_2016_2017_traiteurs.code_ape,
    gerep_2016_2017_traiteurs.nom_contact,
    gerep_2016_2017_traiteurs.tel_contact,
    gerep_2016_2017_traiteurs.fonction_contact,
    gerep_2016_2017_traiteurs.mail_contact
   FROM raw_zone_gsheet.gerep_2016_2017_traiteurs;


ALTER TABLE trusted_zone_gsheet.gerep_traiteurs OWNER TO pao;

--
-- Name: gerep_traiteurs_amiante; Type: TABLE; Schema: trusted_zone_gsheet; Owner: pao
--

CREATE TABLE trusted_zone_gsheet.gerep_traiteurs_amiante (
    index bigint,
    annee text,
    code_etablissement text,
    nom_etablissement text,
    adresse_site_exploitation text,
    code_postal_etablissement text,
    commune text,
    code_insee text,
    numero_siret text,
    code_ape text,
    nom_contact text,
    tel_contact text,
    fonction_contact text,
    mail_contact text,
    code_dechet_traite text,
    dechet_traite text
);


ALTER TABLE trusted_zone_gsheet.gerep_traiteurs_amiante OWNER TO pao;

--
-- Name: etablissements; Type: VIEW; Schema: trusted_zone_icpe; Owner: pao
--

CREATE VIEW trusted_zone_icpe.etablissements AS
 SELECT ic_etablissement."codeS3ic" AS code_s3ic,
    ic_etablissement."s3icNumeroSiret" AS siret,
    (ic_etablissement.x)::integer AS x,
    (ic_etablissement.y)::integer AS y,
    (ic_etablissement.region)::integer AS region,
    ic_etablissement."nomEts" AS nom_etablissement,
    ic_etablissement."codeCommuneEtablissement" AS code_commune_etablissement,
    ic_etablissement."codePostal" AS code_postal,
    (ic_etablissement."etatActivite")::integer AS etat_activite,
    ic_etablissement."codeApe" AS code_ape,
    ic_etablissement."nomCommune" AS nom_commune,
    ic_etablissement.seveso,
    ic_etablissement.regime,
    (ic_etablissement."prioriteNationale")::boolean AS priorite_nationale,
    (ic_etablissement.ippc)::boolean AS ippc,
    (ic_etablissement."declarationAnnuelle")::boolean AS declaration_annuelle,
    ic_etablissement."familleIc" AS familleic,
    (ic_etablissement."baseIdService")::integer AS base_id_service,
    (ic_etablissement."natureIdService")::integer AS nature_id_service,
    ic_etablissement.adresse1 AS adresse_1,
    ic_etablissement.adresse2 AS adresse_2,
    (ic_etablissement."dateInspection")::date AS date_inspection,
    (ic_etablissement."indicationSsp")::boolean AS indication_ssp,
    (ic_etablissement.rayon)::integer AS rayon,
    (ic_etablissement."precisionPositionnement")::integer AS precision_positionnement,
    ic_etablissement.inserted_at
   FROM raw_zone_icpe.ic_etablissement;


ALTER TABLE trusted_zone_icpe.etablissements OWNER TO pao;

--
-- Name: installations_classees; Type: VIEW; Schema: trusted_zone_icpe; Owner: pao
--

CREATE VIEW trusted_zone_icpe.installations_classees AS
 SELECT ic_installation_classee.id,
    ic_installation_classee."codeS3ic" AS code_s3ic,
    (ic_installation_classee.volume)::double precision AS volume,
    ic_installation_classee.unite,
    (ic_installation_classee.statut_ic)::boolean AS statut_ic,
    ic_installation_classee.id_ref_nomencla_ic AS id_nomenclature,
    ic_installation_classee.inserted_at,
    to_date(ic_installation_classee.date_debut_exploitation, 'DD/MM/YYYY'::text) AS date_debut_exploitation,
    to_date(ic_installation_classee.date_fin_validite, 'DD/MM/YYYY'::text) AS date_fin_validite
   FROM raw_zone_icpe.ic_installation_classee;


ALTER TABLE trusted_zone_icpe.installations_classees OWNER TO pao;

--
-- Name: nomenclature; Type: VIEW; Schema: trusted_zone_icpe; Owner: pao
--

CREATE VIEW trusted_zone_icpe.nomenclature AS
 SELECT ic_ref_nomenclature_ic.id,
    ic_ref_nomenclature_ic.rubrique_ic AS rubrique,
    ic_ref_nomenclature_ic.famille_ic AS famille,
    ic_ref_nomenclature_ic.sfamille_ic AS s_famille,
    ic_ref_nomenclature_ic.ssfamille_ic AS ss_famille,
    ic_ref_nomenclature_ic.alinea,
    ic_ref_nomenclature_ic.libellecourt_activite AS libelle_court_activite,
    ic_ref_nomenclature_ic.id_regime,
    (ic_ref_nomenclature_ic.envigueur)::boolean AS en_vigueur,
    (ic_ref_nomenclature_ic.ippc)::boolean AS ippc,
    ic_ref_nomenclature_ic.inserted_at
   FROM raw_zone_icpe.ic_ref_nomenclature_ic;


ALTER TABLE trusted_zone_icpe.nomenclature OWNER TO pao;

--
-- Name: code_geo_arrondissements; Type: VIEW; Schema: trusted_zone_insee; Owner: pao
--

CREATE VIEW trusted_zone_insee.code_geo_arrondissements AS
 SELECT arrondissement.arr AS code_arrondissement,
    arrondissement.dep AS code_departement,
    (arrondissement.reg)::integer AS code_region,
    arrondissement.cheflieu AS code_commune_chef_lieu,
    (arrondissement.tncc)::integer AS type_nom_en_clair,
    arrondissement.ncc AS nom_en_clair,
    arrondissement.nccenr AS nom_en_clair_enrichi,
    arrondissement.libelle
   FROM raw_zone_insee.arrondissement;


ALTER TABLE trusted_zone_insee.code_geo_arrondissements OWNER TO pao;

--
-- Name: code_geo_cantons; Type: VIEW; Schema: trusted_zone_insee; Owner: pao
--

CREATE VIEW trusted_zone_insee.code_geo_cantons AS
 SELECT canton.id_canton AS code_canton,
    canton.id_departement AS code_departement,
    (canton.id_region)::integer AS code_region,
    (canton.typct)::integer AS type_canton,
    canton.burcentral AS code_commune_bureau_centraliseur,
    (canton.tncc)::integer AS type_nom_en_clair,
    canton.ncc AS nom_en_clair,
    canton.nccenr AS nom_en_clair_enrichi,
    canton.libelle,
    canton.actual
   FROM raw_zone_insee.canton;


ALTER TABLE trusted_zone_insee.code_geo_cantons OWNER TO pao;

--
-- Name: code_geo_communes; Type: VIEW; Schema: trusted_zone_insee; Owner: pao
--

CREATE VIEW trusted_zone_insee.code_geo_communes AS
 SELECT commune.typecom AS type_commune,
    (commune.reg)::integer AS code_region,
    commune.dep AS code_departement,
    commune.com AS code_commune,
    commune.can AS code_canton,
    commune.arr AS code_arrondissement,
    commune.ctcd AS code_ctcd,
    (commune.tncc)::integer AS type_nom_en_clair,
    commune.ncc AS nom_en_clair,
    commune.nccenr AS nom_en_clair_enrichi,
    commune.libelle,
    commune.comparent AS code_commune_parente
   FROM raw_zone_insee.commune;


ALTER TABLE trusted_zone_insee.code_geo_communes OWNER TO pao;

--
-- Name: code_geo_departements; Type: VIEW; Schema: trusted_zone_insee; Owner: pao
--

CREATE VIEW trusted_zone_insee.code_geo_departements AS
 SELECT (departement.reg)::integer AS code_region,
    departement.dep AS code_departement,
    departement.cheflieu AS code_commune_chef_lieu,
    (departement.tncc)::integer AS type_nom_en_clair,
    departement.ncc AS nom_en_clair,
    departement.nccenr AS nom_en_clair_enrichi,
    departement.libelle
   FROM raw_zone_insee.departement;


ALTER TABLE trusted_zone_insee.code_geo_departements OWNER TO pao;

--
-- Name: code_geo_departments; Type: VIEW; Schema: trusted_zone_insee; Owner: pao
--

CREATE VIEW trusted_zone_insee.code_geo_departments AS
 SELECT (departement.reg)::integer AS code_region,
    departement.dep AS code_departement,
    departement.cheflieu AS code_commune_chef_lieu,
    (departement.tncc)::integer AS type_nom_en_clair,
    departement.ncc AS nom_en_clair,
    departement.nccenr AS nom_en_clair_enrichi,
    departement.libelle
   FROM raw_zone_insee.departement;


ALTER TABLE trusted_zone_insee.code_geo_departments OWNER TO pao;

--
-- Name: code_geo_pays; Type: VIEW; Schema: trusted_zone_insee; Owner: pao
--

CREATE VIEW trusted_zone_insee.code_geo_pays AS
 SELECT pays.cog AS code_pays,
    (pays.actual)::integer AS "coe_actualité",
    pays.capay AS code_ancien_pays_rattachement,
    pays.crpay AS code_actuel_pays_rattachement,
    (pays.ani)::integer AS annee_independance,
    pays.libcog AS libelle,
    pays.libenr AS nom_officiel,
    pays.ancnom AS ancien_nom,
    pays.codeiso2 AS code_iso_2,
    pays.codeiso3 AS code_iso_3,
    (pays.codenum3)::integer AS code_iso_num
   FROM raw_zone_insee.pays;


ALTER TABLE trusted_zone_insee.code_geo_pays OWNER TO pao;

--
-- Name: code_geo_regions; Type: VIEW; Schema: trusted_zone_insee; Owner: pao
--

CREATE VIEW trusted_zone_insee.code_geo_regions AS
 SELECT (region.reg)::integer AS code_region,
    region.cheflieu AS code_commune_chef_lieu,
    (region.tncc)::integer AS type_nom_en_clair,
    region.ncc AS nom_en_clair,
    region.nccenr AS nom_en_clair_enrichi,
    region.libelle
   FROM raw_zone_insee.region;


ALTER TABLE trusted_zone_insee.code_geo_regions OWNER TO pao;

--
-- Name: nomenclature_activites_francaises; Type: VIEW; Schema: trusted_zone_insee; Owner: pao
--

CREATE VIEW trusted_zone_insee.nomenclature_activites_francaises AS
 SELECT naf2008.code_section,
    naf2008.libelle_section,
    naf2008.code_division,
    naf2008.libelle_division,
    naf2008.code_groupe,
    naf2008.libelle_groupe,
    naf2008.code_classe,
    naf2008.libelle_classe,
    naf2008.code_sous_classe,
    naf2008.libelle_sous_classe
   FROM raw_zone_insee.naf2008;


ALTER TABLE trusted_zone_insee.nomenclature_activites_francaises OWNER TO pao;

--
-- Name: stock_etablissement; Type: VIEW; Schema: trusted_zone_insee; Owner: pao
--

CREATE VIEW trusted_zone_insee.stock_etablissement AS
 SELECT stock_etablissement.siren,
    stock_etablissement.nic,
    stock_etablissement.siret,
    stock_etablissement."statutDiffusionEtablissement" AS statut_diffusion_etablissement,
    (stock_etablissement."dateCreationEtablissement")::date AS date_creation_etablissement,
    stock_etablissement."trancheEffectifsEtablissement" AS tranche_effectifs_etablissement,
    (stock_etablissement."anneeEffectifsEtablissement")::integer AS annee_effectifs_etablissement,
    stock_etablissement."activitePrincipaleRegistreMetiersEtablissement" AS activite_principale_registre_metiers_etablissement,
    (stock_etablissement."dateDernierTraitementEtablissement")::timestamp without time zone AS date_dernier_traitement_etablissement,
    (stock_etablissement."etablissementSiege")::boolean AS etablissement_siege,
    (stock_etablissement."nombrePeriodesEtablissement")::integer AS nombre_periodes_etablissement,
    stock_etablissement."complementAdresseEtablissement" AS complement_adresse_etablissement,
    stock_etablissement."numeroVoieEtablissement" AS numero_voie_etablissement,
    stock_etablissement."indiceRepetitionEtablissement" AS indice_repetition_etablissement,
    stock_etablissement."typeVoieEtablissement" AS type_voie_etablissement,
    stock_etablissement."libelleVoieEtablissement" AS libelle_voie_etablissement,
    stock_etablissement."codePostalEtablissement" AS code_postal_etablissement,
    stock_etablissement."libelleCommuneEtablissement" AS libelle_commune_etablissement,
    stock_etablissement."libelleCommuneEtrangerEtablissement" AS libelle_commune_etranger_etablissement,
    stock_etablissement."distributionSpecialeEtablissement" AS distribution_speciale_etablissement,
    stock_etablissement."codeCommuneEtablissement" AS code_commune_etablissement,
    stock_etablissement."codeCedexEtablissement" AS code_cedex_etablissement,
    stock_etablissement."libelleCedexEtablissement" AS libelle_cedex_etablissement,
    (stock_etablissement."codePaysEtrangerEtablissement")::integer AS code_pays_etranger_etablissement,
    stock_etablissement."libellePaysEtrangerEtablissement" AS libelle_pays_etranger_etablissement,
    stock_etablissement."complementAdresse2Etablissement" AS complement_adresse_2_etablissement,
    stock_etablissement."numeroVoie2Etablissement" AS numero_voie_2_etablissement,
    stock_etablissement."indiceRepetition2Etablissement" AS indice_repetition_2_etablissement,
    stock_etablissement."typeVoie2Etablissement" AS type_voie_2_etablissement,
    stock_etablissement."libelleVoie2Etablissement" AS libelle_voie_2_etablissement,
    stock_etablissement."codePostal2Etablissement" AS code_postal_2_etablissement,
    stock_etablissement."libelleCommune2Etablissement" AS libelle_commune_2_etablissement,
    stock_etablissement."libelleCommuneEtranger2Etablissement" AS libelle_commune_etranger_2_etablissement,
    stock_etablissement."distributionSpeciale2Etablissement" AS distribution_speciale_2_etablissement,
    stock_etablissement."codeCommune2Etablissement" AS code_commune_2_etablissement,
    stock_etablissement."codeCedex2Etablissement" AS code_cedex_2_etablissement,
    stock_etablissement."libelleCedex2Etablissement" AS libelle_cedex_2_etablissement,
    (stock_etablissement."codePaysEtranger2Etablissement")::integer AS code_pays_etranger_2_etablissement,
    stock_etablissement."libellePaysEtranger2Etablissement" AS libelle_pays_etranger_2_etablissement,
    (stock_etablissement."dateDebut")::date AS date_debut,
    stock_etablissement."etatAdministratifEtablissement" AS etat_administratif_etablissement,
    stock_etablissement."enseigne1Etablissement" AS enseigne_1_etablissement,
    stock_etablissement."enseigne2Etablissement" AS enseigne_2_etablissement,
    stock_etablissement."enseigne3Etablissement" AS enseigne_3_etablissement,
    stock_etablissement."denominationUsuelleEtablissement" AS denomination_usuelle_etablissement,
    stock_etablissement."activitePrincipaleEtablissement" AS activite_principale_etablissement,
    stock_etablissement."nomenclatureActivitePrincipaleEtablissement" AS nomenclature_activite_principale_etablissement,
    stock_etablissement."caractereEmployeurEtablissement" AS caractere_employeur_etablissement
   FROM raw_zone_insee.stock_etablissement;


ALTER TABLE trusted_zone_insee.stock_etablissement OWNER TO pao;

--
-- Name: broker_receipt; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.broker_receipt AS
 SELECT brokerreceipt.id,
    brokerreceipt.receiptnumber AS receipt_number,
    brokerreceipt.validitylimit AS validity_limit,
    brokerreceipt.department
   FROM raw_zone_trackdechets.brokerreceipt;


ALTER TABLE trusted_zone_trackdechets.broker_receipt OWNER TO pao;

--
-- Name: bsda; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.bsda AS
 SELECT bsda.id,
    bsda.createdat AS created_at,
    bsda.updatedat AS updated_at,
    bsda.status,
    bsda.type,
    bsda.isdeleted AS is_deleted,
    bsda.isdraft AS is_draft,
    bsda.wastecode AS waste_code,
    bsda.wastefamilycode AS waste_family_code,
    bsda.wastepop AS waste_pop,
    bsda.wasteconsistence AS waste_consistence,
    bsda.wastematerialname AS waste_material_name,
    bsda.wasteadr AS waste_adr,
    bsda.wastesealnumbers AS waste_seal_numbers,
    bsda.weightisestimate AS weight_is_estimate,
    bsda.packagings,
    bsda.repackagedinid AS repackaged_in_id,
    bsda.emittercompanysiret AS emitter_company_siret,
    bsda.emittercompanyname AS emitter_company_name,
    bsda.emittercompanyaddress AS emitter_company_address,
    bsda.emittercompanycontact AS emitter_company_contact,
    bsda.emittercompanymail AS emitter_company_mail,
    bsda.emittercompanyphone AS emitter_company_phone,
    bsda.emittercustominfo AS emitter_custom_info,
    bsda.emitteremissionsignatureauthor AS emitter_emission_signature_author,
    bsda.emitteremissionsignaturedate AS emitter_emission_signature_date,
    bsda.emitterisprivateindividual AS emitter_isprivate_individual,
    bsda.emitterpickupsitename AS emitter_pickup_site_name,
    bsda.emitterpickupsiteaddress AS emitter_pickup_site_address,
    bsda.emitterpickupsitepostalcode AS emitter_pickup_site_postal_code,
    bsda.emitterpickupsitecity AS emitter_pickup_site_city,
    bsda.emitterpickupsiteinfos AS emitter_pickup_site_infos,
    bsda.workercompanysiret AS worker_company_siret,
    bsda.workercompanyname AS worker_company_name,
    bsda.workercompanyaddress AS worker_company_address,
    bsda.workercompanycontact AS worker_company_contact,
    bsda.workercompanyphone AS worker_company_phone,
    bsda.workercompanymail AS worker_company_mail,
    bsda.workercertificationorganisation AS worker_certification_organisation,
    bsda.workercertificationcertificationnumber AS worker_certification_certification_number,
    bsda.workercertificationhassubsectionthree AS worker_certification_has_subsection_three,
    bsda.workercertificationhassubsectionfour AS worker_certification_has_subsection_four,
    bsda.workercertificationvaliditylimit AS worker_certificationvalidity_limit,
    bsda.workerworkhasemitterpapersignature AS worker_work_has_emitter_paper_signature,
    bsda.workerworksignatureauthor AS worker_work_signature_author,
    bsda.workerworksignaturedate AS worker_work_signature_date,
    bsda.workerisdisabled AS worker_is_disabled,
    bsda.transportercompanysiret AS transporter_company_siret,
    bsda.transportercompanyname AS transporter_company_name,
    bsda.transportercompanyaddress AS transporter_company_address,
    bsda.transporterrecepissedepartment AS transporter_recepisse_department,
    bsda.transportercompanycontact AS transporter_company_contact,
    bsda.transportercompanymail AS transporter_company_mail,
    bsda.transportercompanyphone AS transporter_company_phone,
    bsda.transportercompanyvatnumber AS transporter_company_vat_number,
    bsda.transportercustominfo AS transporter_custom_info,
    bsda.transporterrecepisseisexempted AS transporter_recepisse_is_exempted,
    bsda.transporterrecepissenumber AS transporter_recepisse_number,
    bsda.transporterrecepissevaliditylimit AS transporter_recepisse_validity_limit,
    bsda.transportertransportmode AS transporter_transport_mode,
    bsda.transportertransportplates AS transporter_transport_plates,
    bsda.transportertransportsignatureauthor AS transporter_transport_signature_author,
    bsda.transportertransportsignaturedate AS transporter_transport_signature_date,
    bsda.transportertransporttakenoverat AS transporter_transport_taken_over_at,
    bsda.destinationcompanysiret AS destination_company_siret,
    bsda.destinationcompanyname AS destination_company_name,
    bsda.destinationcompanyaddress AS destination_company_address,
    bsda.destinationcompanycontact AS destination_company_contact,
    bsda.destinationcompanymail AS destination_company_mail,
    bsda.destinationcompanyphone AS destination_company_phone,
    bsda.destinationcustominfo AS destination_custom_info,
    bsda.destinationreceptiondate AS destination_reception_date,
    bsda.destinationcap AS destination_cap,
    bsda.destinationreceptionacceptationstatus AS destination_reception_acceptation_status,
    bsda.destinationoperationdate AS destination_operation_date,
    bsda.destinationoperationdescription AS destination_operation_description,
    bsda.destinationoperationsignatureauthor AS destination_operation_signature_author,
    bsda.destinationoperationsignaturedate AS destination_operation_signature_date,
    bsda.destinationreceptionrefusalreason AS destination_reception_refusal_reason,
    bsda.ecoorganismesiret AS eco_organisme_siret,
    bsda.ecoorganismename AS eco_organisme_name,
    bsda.destinationoperationnextdestinationcompanysiret AS destination_operation_next_destination_company_siret,
    bsda.destinationoperationnextdestinationcompanyname AS destination_operation_next_destination_company_name,
    bsda.destinationoperationnextdestinationcompanyaddress AS destination_operation_next_destination_company_address,
    bsda.destinationoperationnextdestinationcompanycontact AS destination_operation_next_destination_company_contact,
    bsda.destinationoperationnextdestinationcompanymail AS destination_operation_next_destination_company_mail,
    bsda.destinationoperationnextdestinationcompanyphone AS destination_operation_next_destination_company_phone,
    bsda.destinationoperationnextdestinationcompanyvatnumber AS destination_operation_next_destination_company_vat_number,
    bsda.destinationoperationnextdestinationcap AS destination_operation_next_destination_cap,
    bsda.destinationoperationnextdestinationplannedoperationcode AS destination_operation_next_destination_planned_operation_code,
    bsda.brokercompanyaddress AS broker_company_address,
    bsda.brokercompanycontact AS broker_company_contact,
    bsda.brokercompanymail AS broker_company_mail,
    bsda.brokercompanyname AS broker_company_name,
    bsda.brokercompanyphone AS broker_company_phone,
    bsda.brokercompanysiret AS broker_company_siret,
    bsda.brokerrecepissedepartment AS broker_recepisse_department,
    bsda.brokerrecepissenumber AS broker_recepisse_number,
    bsda.brokerrecepissevaliditylimit AS broker_recepisse_validity_limit,
    bsda.forwardingid AS forwarding_id,
    bsda.groupedinid AS grouped_in_id,
    replace((bsda.destinationplannedoperationcode)::text, ' '::text, ''::text) AS destination_planned_operation_code,
    replace((bsda.destinationoperationcode)::text, ' '::text, ''::text) AS destination_operation_code,
    (bsda.weightvalue / (1000)::double precision) AS weight_value,
    (bsda.destinationreceptionweight / (1000)::double precision) AS destination_reception_weight
   FROM raw_zone_trackdechets.bsda;


ALTER TABLE trusted_zone_trackdechets.bsda OWNER TO pao;

--
-- Name: bsda_revision_request; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.bsda_revision_request AS
 SELECT bsdarevisionrequest.id,
    bsdarevisionrequest.createdat AS created_at,
    bsdarevisionrequest.updatedat AS updated_at,
    bsdarevisionrequest.bsdaid AS bsda_id,
    bsdarevisionrequest.authoringcompanyid AS authoring_company_id,
    bsdarevisionrequest.comment,
    bsdarevisionrequest.status,
    bsdarevisionrequest.iscanceled AS is_canceled,
    bsdarevisionrequest.wastecode AS waste_code,
    bsdarevisionrequest.wastepop AS waste_pop,
    bsdarevisionrequest.packagings,
    bsdarevisionrequest.wastesealnumbers AS waste_seal_numbers,
    bsdarevisionrequest.wastematerialname AS waste_material_name,
    bsdarevisionrequest.destinationcap AS destination_cap,
    bsdarevisionrequest.destinationreceptionweight AS destination_reception_weight,
    bsdarevisionrequest.destinationoperationcode AS destination_operation_code,
    bsdarevisionrequest.destinationoperationdescription AS destination_operation_description,
    bsdarevisionrequest.brokercompanysiret AS broker_company_siret,
    bsdarevisionrequest.brokercompanyname AS broker_company_name,
    bsdarevisionrequest.brokercompanyaddress AS broker_company_address,
    bsdarevisionrequest.brokercompanycontact AS broker_company_contact,
    bsdarevisionrequest.brokercompanymail AS broker_company_mail,
    bsdarevisionrequest.brokercompanyphone AS broker_company_phone,
    bsdarevisionrequest.brokerrecepissenumber AS broker_recepisse_number,
    bsdarevisionrequest.brokerrecepissevaliditylimit AS broker_recepisse_validity_limit,
    bsdarevisionrequest.brokerrecepissedepartment AS broker_recepisse_department,
    bsdarevisionrequest.emitterpickupsitename AS emitter_pickup_sitename,
    bsdarevisionrequest.emitterpickupsiteaddress AS emitter_pickup_site_address,
    bsdarevisionrequest.emitterpickupsitecity AS emitter_pickup_site_city,
    bsdarevisionrequest.emitterpickupsitepostalcode AS emitter_pickup_site_postal_code,
    bsdarevisionrequest.emitterpickupsiteinfos AS emitter_pickup_site_infos
   FROM raw_zone_trackdechets.bsdarevisionrequest;


ALTER TABLE trusted_zone_trackdechets.bsda_revision_request OWNER TO pao;

--
-- Name: bsdasri; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.bsdasri AS
 SELECT bsdasri.id,
    bsdasri.createdat AS created_at,
    bsdasri.updatedat AS updated_at,
    bsdasri.status,
    bsdasri.type,
    bsdasri.isdeleted AS is_deleted,
    bsdasri.isdraft AS is_draft,
    bsdasri.wasteadr AS waste_adr,
    bsdasri.wastecode AS waste_code,
    bsdasri.identificationnumbers AS identification_numbers,
    bsdasri.emittercompanysiret AS emitter_company_siret,
    bsdasri.emittercompanyname AS emitter_company_name,
    bsdasri.emittercompanyaddress AS emitter_company_address,
    bsdasri.emittercompanycontact AS emitter_company_contact,
    bsdasri.emittercompanymail AS emitter_company_mail,
    bsdasri.emittercompanyphone AS emitter_company_phone,
    bsdasri.emittercustominfo AS emitter_custom_info,
    bsdasri.emitterpickupsitename AS emitter_pickup_sitename,
    bsdasri.emitterpickupsiteaddress AS emitter_pickup_site_address,
    bsdasri.emitterpickupsitepostalcode AS emitter_pickup_site_postal_code,
    bsdasri.emitterpickupsitecity AS emitter_pickup_site_city,
    bsdasri.emitterpickupsiteinfos AS emitter_pickup_site_infos,
    bsdasri.emitteremissionsignaturedate AS emitter_emission_signature_date,
    bsdasri.emitteremissionsignatureauthor AS emitter_emission_signature_author,
    bsdasri.emittedbyecoorganisme AS emitted_by_eco_organisme,
    bsdasri.emitterwastevolume AS emitter_waste_volume,
    bsdasri.emitterwasteweightvalue AS emitter_waste_weight_value,
    bsdasri.emitterwasteweightisestimate AS emitter_waste_weight_is_estimate,
    bsdasri.emitterwastepackagings AS emitter_waste_packagings,
    bsdasri.emissionsignatoryid AS emission_signatory_id,
    bsdasri.isemissiondirecttakenover AS is_emission_direct_taken_over,
    bsdasri.isemissiontakenoverwithsecretcode AS is_emission_taken_over_with_secret_code,
    bsdasri.transportercompanysiret AS transporter_company_siret,
    bsdasri.transportercompanyname AS transporter_company_name,
    bsdasri.transportercompanyaddress AS transporter_company_address,
    bsdasri.transportercompanycontact AS transporter_company_contact,
    bsdasri.transportercompanymail AS transporter_company_mail,
    bsdasri.transportercompanyphone AS transporter_company_phone,
    bsdasri.transportercompanyvatnumber AS transporter_company_vat_number,
    bsdasri.transportercustominfo AS transporter_custom_info,
    bsdasri.transportsignatoryid AS transport_signatory_id,
    bsdasri.transporterrecepissenumber AS transporter_recepisse_number,
    bsdasri.transporterrecepissedepartment AS transporter_recepisse_department,
    bsdasri.transporterrecepissevaliditylimit AS transporter_recepisse_validity_limit,
    bsdasri.transportertransportmode AS transporter_transport_mode,
    bsdasri.transportertransportplates AS transporter_transport_plates,
    bsdasri.transporteracceptationstatus AS transporter_acceptation_status,
    bsdasri.transportertakenoverat AS transporter_taken_over_at,
    bsdasri.transportertransportsignaturedate AS transporter_transport_signature_date,
    bsdasri.transportertransportsignatureauthor AS transporter_transport_signature_author,
    bsdasri.transporterwastevolume AS transporter_waste_volume,
    bsdasri.transporterwasteweightisestimate AS transporter_waste_weight_is_estimate,
    bsdasri.transporterwastepackagings AS transporter_waste_packagings,
    bsdasri.transporterwasterefusalreason AS transporter_waste_refusal_reason,
    bsdasri.transporterwasterefusedweightvalue AS transporter_waste_refused_weight_value,
    bsdasri.destinationcompanysiret AS destination_company_siret,
    bsdasri.destinationcompanyname AS destination_company_name,
    bsdasri.destinationcompanyaddress AS destination_company_address,
    bsdasri.destinationcompanycontact AS destination_company_contact,
    bsdasri.destinationcompanymail AS destination_company_mail,
    bsdasri.destinationcompanyphone AS destination_company_phone,
    bsdasri.destinationcustominfo AS destination_custom_info,
    bsdasri.destinationreceptiondate AS destination_reception_date,
    bsdasri.destinationreceptionsignaturedate AS destination_reception_signature_date,
    bsdasri.destinationreceptionsignatureauthor AS destination_reception_signature_author,
    bsdasri.destinationwastepackagings AS destination_waste_packagings,
    bsdasri.destinationreceptionwastevolume AS destination_reception_waste_volume,
    bsdasri.destinationreceptionwasterefusalreason AS destination_reception_waste_refusal_reason,
    bsdasri.receptionsignatoryid AS reception_signatory_id,
    bsdasri.destinationoperationdate AS destination_operation_date,
    bsdasri.destinationoperationcode AS destination_operation_code,
    bsdasri.destinationoperationsignaturedate AS destination_operation_signature_date,
    bsdasri.destinationoperationsignatureauthor AS destination_operation_signature_author,
    bsdasri.operationsignatoryid AS operation_signatory_id,
    bsdasri.destinationreceptionacceptationstatus AS destination_reception_acceptation_status,
    bsdasri.handedovertorecipientat AS handed_over_to_recipient_at,
    bsdasri.ecoorganismesiret AS eco_organisme_siret,
    bsdasri.ecoorganismename AS eco_organisme_name,
    bsdasri.groupedinid AS grouped_in_id,
    bsdasri.synthesizedinid AS synthesized_in_id,
    (bsdasri.transporterwasteweightvalue / (1000)::double precision) AS transporter_waste_weight_value,
    (bsdasri.destinationreceptionwasteweightvalue / (1000)::double precision) AS destination_reception_waste_weight_value,
    (bsdasri.destinationreceptionwasterefusedweightvalue / (1000)::double precision) AS destination_reception_waste_refused_weight_value
   FROM raw_zone_trackdechets.bsdasri;


ALTER TABLE trusted_zone_trackdechets.bsdasri OWNER TO pao;

--
-- Name: bsdd; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.bsdd AS
 SELECT form.id,
    form.customid AS custom_id,
    form.readableid AS readable_id,
    form.createdat AS created_at,
    form.updatedat AS updated_at,
    form.status,
    form.isdeleted AS is_deleted,
    form.ownerid AS owner_id,
    form.wastedetailscode AS waste_details_code,
    form.wastedetailsname AS waste_details_name,
    form.wastedetailspop AS waste_details_pop,
    form.wastedetailsisdangerous AS waste_details_is_dangerous,
    form.wastedetailsonucode AS waste_details_onu_code,
    form.wastedetailsquantity AS waste_details_quantity,
    form.wastedetailsquantitytype AS waste_details_quantity_type,
    form.wastedetailsconsistence AS waste_details_consistence,
    form.wastedetailspackaginginfos AS waste_details_packaging_infos,
    form.wastedetailsanalysisreferences AS waste_details_analysis_references,
    form.wastedetailslandidentifiers AS waste_details_land_identifiers,
    form.wastedetailsparcelnumbers AS waste_details_parcel_numbers,
    form.wasteacceptationstatus AS waste_acceptation_status,
    form.wasterefusalreason AS waste_refusal_reason,
    form.emittercompanysiret AS emitter_company_siret,
    form.emittercompanyname AS emitter_company_name,
    form.emittertype AS emitter_type,
    form.emittercompanyaddress AS emitter_company_address,
    form.emittercompanycontact AS emitter_company_contact,
    form.emittercompanymail AS emitter_company_mail,
    form.emittercompanyphone AS emitter_company_phone,
    form.emitterisforeignship AS emitter_is_foreignship,
    form.emittercompanyominumber AS emitter_company_omi_number,
    form.emitterisprivateindividual AS emitter_is_private_individual,
    form.emitterpickupsite AS emitter_pickup_site,
    form.emitterworksitename AS emitter_worksite_name,
    form.emitterworksiteaddress AS emitter_worksite_address,
    form.emitterworksitepostalcode AS emitter_worksite_postal_code,
    form.emitterworksitecity AS emitter_worksite_city,
    form.emitterworksiteinfos AS emitter_worksite_infos,
    form.emittedbyecoorganisme AS emitted_by_eco_organisme,
    form.emittedat AS emitted_at,
    form.emittedby AS emitted_by,
    form.signedat AS signed_at,
    form.signedby AS signed_by,
    form.signedbytransporter AS signed_by_transporter,
    form.sentat AS sent_at,
    form.sentby AS sent_by,
    form.transportercompanysiret AS transporter_company_siret,
    form.transportercompanyname AS transporter_company_name,
    form.transportercompanyaddress AS transporter_company_address,
    form.transporterdepartment AS transporter_department,
    form.transportercompanycontact AS transporter_company_contact,
    form.transportercompanymail AS transporter_company_mail,
    form.transportercompanyphone AS transporter_company_phone,
    form.transporternumberplate AS transporter_number_plate,
    form.transporterreceipt AS transporter_receipt,
    form.transportervaliditylimit AS transporter_validity_limit,
    form.transportertransportmode AS transporter_transport_mode,
    form.transportercompanyvatnumber AS transporter_company_vat_number,
    form.transportercustominfo AS transporter_custom_info,
    form.transporterisexemptedofreceipt AS transporter_is_exempted_of_receipt,
    form.currenttransportersiret AS current_transporter_siret,
    form.nexttransportersiret AS next_transporter_siret,
    form.takenoverat AS taken_over_at,
    form.takenoverby AS taken_over_by,
    form.recipientcompanysiret AS recipient_company_siret,
    form.recipientcompanyname AS recipient_company_name,
    form.recipientcompanyaddress AS recipient_company_address,
    form.recipientcompanycontact AS recipient_company_contact,
    form.recipientcompanymail AS recipient_company_mail,
    form.recipientcompanyphone AS recipient_company_phone,
    form.recipientistempstorage AS recipient_is_temp_storage,
    form.recipientcap AS recipient_cap,
    form.receivedat AS received_at,
    form.receivedby AS received_by,
    form.processedat AS processed_at,
    form.processedby AS processed_by,
    form.quantityreceived AS quantity_received,
    form.quantityreceivedtype AS quantity_received_type,
    form.processingoperationdescription AS processing_operation_description,
    form.notraceability AS no_traceability,
    form.isaccepted AS is_accepted,
    form.nextdestinationcompanysiret AS next_destination_company_siret,
    form.nextdestinationcompanyname AS next_destination_company_name,
    form.nextdestinationcompanyaddress AS next_destination_company_address,
    form.nextdestinationcompanycountry AS next_destination_company_country,
    form.nextdestinationcompanycontact AS next_destination_company_contact,
    form.nextdestinationcompanymail AS next_destination_company_mail,
    form.nextdestinationcompanyphone AS next_destination_company_phone,
    form.nextdestinationcompanyvatnumber AS next_destination_company_vat_number,
    form.nextdestinationprocessingoperation AS next_destination_processing_operation,
    form.brokercompanysiret AS broker_company_siret,
    form.brokercompanyname AS broker_company_name,
    form.brokercompanyaddress AS broker_company_address,
    form.brokerdepartment AS broker_department,
    form.brokercompanycontact AS broker_company_contact,
    form.brokercompanymail AS broker_company_mail,
    form.brokercompanyphone AS broker_company_phone,
    form.brokerreceipt AS broker_receipt,
    form.brokervaliditylimit AS broker_validity_limit,
    form.tradercompanysiret AS trader_company_siret,
    form.tradercompanyname AS trader_company_name,
    form.tradercompanyaddress AS trader_company_address,
    form.traderdepartment AS trader_department,
    form.tradercompanycontact AS trader_company_contact,
    form.tradercompanymail AS trader_company_mail,
    form.tradercompanyphone AS trader_company_phone,
    form.traderreceipt AS trader_receipt,
    form.tradervaliditylimit AS trader_validity_limit,
    form.ecoorganismesiret AS eco_organisme_siret,
    form.ecoorganismename AS eco_organisme_name,
    form.isimportedfrompaper AS is_imported_from_paper,
    form.forwardedinid AS forwarded_in_id,
    replace((form.recipientprocessingoperation)::text, ' '::text, ''::text) AS recipient_processing_operation,
    replace((form.processingoperationdone)::text, ' '::text, ''::text) AS processing_operation_done
   FROM raw_zone_trackdechets.form;


ALTER TABLE trusted_zone_trackdechets.bsdd OWNER TO pao;

--
-- Name: bsdd_revision_request; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.bsdd_revision_request AS
 SELECT bsddrevisionrequest.id,
    bsddrevisionrequest.createdat AS created_at,
    bsddrevisionrequest.updatedat AS updated_at,
    bsddrevisionrequest.bsddid AS bsdd_id,
    bsddrevisionrequest.authoringcompanyid AS authoring_company_id,
    bsddrevisionrequest.comment,
    bsddrevisionrequest.status,
    bsddrevisionrequest.iscanceled AS is_canceled,
    bsddrevisionrequest.recipientcap AS recipient_cap,
    bsddrevisionrequest.wastedetailscode AS waste_details_code,
    bsddrevisionrequest.wastedetailspop AS waste_details_pop,
    bsddrevisionrequest.wastedetailsname AS waste_details_name,
    bsddrevisionrequest.wastedetailspackaginginfos AS waste_details_packaging_infos,
    bsddrevisionrequest.quantityreceived AS quantity_received,
    bsddrevisionrequest.processingoperationdone AS processing_operation_done,
    bsddrevisionrequest.processingoperationdescription AS processing_operation_description,
    bsddrevisionrequest.brokercompanysiret AS broker_company_siret,
    bsddrevisionrequest.brokercompanyname AS broker_company_name,
    bsddrevisionrequest.brokercompanyaddress AS broker_company_address,
    bsddrevisionrequest.brokerdepartment AS broker_department,
    bsddrevisionrequest.brokercompanycontact AS broker_company_contact,
    bsddrevisionrequest.brokercompanymail AS broker_company_mail,
    bsddrevisionrequest.brokercompanyphone AS broker_company_phone,
    bsddrevisionrequest.brokerreceipt AS broker_receipt,
    bsddrevisionrequest.brokervaliditylimit AS broker_validity_limit,
    bsddrevisionrequest.tradercompanysiret AS trader_company_siret,
    bsddrevisionrequest.tradercompanyname AS trader_company_name,
    bsddrevisionrequest.tradercompanyaddress AS trader_company_address,
    bsddrevisionrequest.traderdepartment AS trader_department,
    bsddrevisionrequest.tradercompanycontact AS trader_company_contact,
    bsddrevisionrequest.tradercompanymail AS trader_company_mail,
    bsddrevisionrequest.tradercompanyphone AS trader_company_phone,
    bsddrevisionrequest.traderreceipt AS trader_receipt,
    bsddrevisionrequest.tradervaliditylimit AS trader_validity_limit,
    bsddrevisionrequest.temporarystoragedestinationprocessingoperation AS temporary_storage_destination_processing_operation,
    bsddrevisionrequest.temporarystoragetemporarystorerquantityreceived AS temporary_storage_temporary_storer_quantity_received,
    bsddrevisionrequest.temporarystoragedestinationcap AS temporary_storage_destination_cap
   FROM raw_zone_trackdechets.bsddrevisionrequest;


ALTER TABLE trusted_zone_trackdechets.bsdd_revision_request OWNER TO pao;

--
-- Name: bsff; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.bsff AS
 SELECT bsff.id,
    bsff.createdat AS created_at,
    bsff.updatedat AS updated_at,
    bsff.isdeleted AS is_deleted,
    bsff.isdraft AS is_draft,
    bsff.status,
    bsff.type,
    bsff.wastecode AS waste_code,
    bsff.wastedescription AS waste_description,
    bsff.wasteadr AS waste_adr,
    bsff.weightisestimate AS weight_is_estimate,
    bsff.emittercompanysiret AS emitter_company_siret,
    bsff.emittercompanyname AS emitter_company_name,
    bsff.emittercompanyaddress AS emitter_company_address,
    bsff.emittercompanycontact AS emitter_company_contact,
    bsff.emittercompanymail AS emitter_company_mail,
    bsff.emittercompanyphone AS emitter_company_phone,
    bsff.emittercustominfo AS emitter_custom_info,
    bsff.emitteremissionsignaturedate AS emitter_emission_signature_date,
    bsff.emitteremissionsignatureauthor AS emitter_emission_signature_author,
    bsff.transportercompanyaddress AS transporter_company_address,
    bsff.transportercompanycontact AS transporter_company_contact,
    bsff.transportercompanymail AS transporter_company_mail,
    bsff.transportercompanyname AS transporter_company_name,
    bsff.transportercompanyphone AS transporter_company_phone,
    bsff.transportercompanysiret AS transporter_company_siret,
    bsff.transportercompanyvatnumber AS transporter_company_vat_number,
    bsff.transportercustominfo AS transporter_custom_info,
    bsff.transporterrecepissedepartment AS transporter_recepisse_department,
    bsff.transporterrecepissenumber AS transporter_recepisse_number,
    bsff.transporterrecepissevaliditylimit AS transporter_recepisse_validity_limit,
    bsff.transportertransportmode AS transporter_transport_mode,
    bsff.transportertransportplates AS transporter_transport_plates,
    bsff.transportertransportsignatureauthor AS transporter_transport_signature_author,
    bsff.transportertransportsignaturedate AS transporter_transport_signature_date,
    bsff.transportertransporttakenoverat AS transporter_transport_taken_over_at,
    bsff.destinationcompanysiret AS destination_company_siret,
    bsff.destinationcompanyaddress AS destination_company_address,
    bsff.destinationcompanycontact AS destination_company_contact,
    bsff.destinationcompanymail AS destination_company_mail,
    bsff.destinationcompanyname AS destination_company_name,
    bsff.destinationcompanyphone AS destination_company_phone,
    bsff.destinationcustominfo AS destination_custom_info,
    bsff.destinationreceptiondate AS destination_reception_date,
    bsff.destinationreceptionsignaturedate AS destination_reception_signature_date,
    bsff.destinationreceptionsignatureauthor AS destination_reception_signature_author,
    bsff.destinationreceptionacceptationstatus AS destination_reception_acceptation_status,
    bsff.destinationreceptionrefusalreason AS destination_reception_refusal_reason,
    bsff.destinationplannedoperationcode AS destination_planned_operation_code,
    bsff.destinationoperationcode AS destination_operation_code,
    bsff.destinationoperationsignaturedate AS destination_operation_signature_date,
    bsff.destinationoperationsignatureauthor AS destination_operation_signature_author,
    bsff.destinationoperationnextdestinationcompanysiret AS destination_operation_next_destination_company_siret,
    bsff.destinationoperationnextdestinationcompanyname AS destination_operation_next_destination_company_name,
    bsff.destinationoperationnextdestinationcompanyaddress AS destination_operation_next_destination_company_address,
    bsff.destinationoperationnextdestinationcompanycontact AS destination_operation_next_destination_company_contact,
    bsff.destinationoperationnextdestinationcompanymail AS destination_operation_next_destination_company_mail,
    bsff.destinationoperationnextdestinationcompanyphone AS destination_operation_next_destination_company_phone,
    bsff.destinationoperationnextdestinationcompanyvatnumber AS destination_operation_next_destination_company_vat_number,
    bsff.forwardingid AS forwarding_id,
    bsff.groupedinid AS grouped_in_id,
    bsff.repackagedinid AS repackaged_in_id,
    (bsff.weightvalue / (1000)::double precision) AS weight_value,
    (bsff.destinationreceptionweight / (1000)::double precision) AS destination_reception_weight
   FROM raw_zone_trackdechets.bsff;


ALTER TABLE trusted_zone_trackdechets.bsff OWNER TO pao;

--
-- Name: bsff_packaging; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.bsff_packaging AS
 SELECT bsffpackaging.id,
    bsffpackaging.bsffid AS bsff_id,
    bsffpackaging.numero,
    bsffpackaging.type,
    bsffpackaging.volume,
    bsffpackaging.acceptationstatus AS acceptation_status,
    bsffpackaging.acceptationdate AS acceptation_date,
    bsffpackaging.acceptationsignaturedate AS acceptation_signature_date,
    bsffpackaging.acceptationsignatureauthor AS acceptation_signature_author,
    bsffpackaging.acceptationrefusalreason,
    bsffpackaging.acceptationwastecode AS acceptation_waste_code,
    bsffpackaging.acceptationwastedescription AS acceptation_waste_description,
    bsffpackaging.operationdate AS operation_date,
    bsffpackaging.operationsignaturedate AS operation_signature_date,
    bsffpackaging.operationsignatureauthor AS operation_signature_author,
    bsffpackaging.operationcode AS operation_code,
    bsffpackaging.operationdescription AS operation_description,
    bsffpackaging.operationnotraceability AS operation_no_traceability,
    bsffpackaging.operationnextdestinationcompanysiret AS operation_next_destination_company_siret,
    bsffpackaging.operationnextdestinationcompanyvatnumber AS operation_next_destination_company_vat_number,
    bsffpackaging.operationnextdestinationcompanyname AS operation_next_destination_company_name,
    bsffpackaging.operationnextdestinationcompanyaddress AS operation_next_destination_company_address,
    bsffpackaging.operationnextdestinationcompanycontact AS operation_next_destination_company_contact,
    bsffpackaging.operationnextdestinationcompanymail AS operation_next_destination_company_mail,
    bsffpackaging.operationnextdestinationcompanyphone AS operation_next_destination_company_phone,
    bsffpackaging.operationnextdestinationplannedoperationcode AS operation_next_destination_planned_operation_code,
    bsffpackaging.operationnextdestinationcap AS operation_next_destination_cap,
    bsffpackaging.nextpackagingid AS next_packaging_id,
    bsffpackaging.other,
    (bsffpackaging.acceptationweight / (1000)::double precision) AS acceptation_weight,
    (bsffpackaging.weight / (1000)::double precision) AS weight
   FROM raw_zone_trackdechets.bsffpackaging;


ALTER TABLE trusted_zone_trackdechets.bsff_packaging OWNER TO pao;

--
-- Name: bsvhu; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.bsvhu AS
 SELECT bsvhu.id,
    bsvhu.createdat AS created_at,
    bsvhu.updatedat AS updated_at,
    bsvhu.isdeleted AS is_deleted,
    bsvhu.isdraft AS is_draft,
    bsvhu.status,
    bsvhu.wastecode AS waste_code,
    bsvhu.quantity,
    bsvhu.weightisestimate AS weight_is_estimate,
    bsvhu.packaging,
    bsvhu.emittercompanysiret AS emitter_company_siret,
    bsvhu.emittercompanyname AS emitter_company_name,
    bsvhu.emittercompanyaddress AS emitter_company_address,
    bsvhu.emittercompanycontact AS emitter_company_contact,
    bsvhu.emittercompanymail AS emitter_company_mail,
    bsvhu.emittercompanyphone AS emitter_company_phone,
    bsvhu.emittercustominfo AS emitter_custom_info,
    bsvhu.emitteragrementnumber AS emitter_agrement_number,
    bsvhu.emitteremissionsignaturedate AS emitter_emission_signature_date,
    bsvhu.emitteremissionsignatureauthor AS emitter_emission_signature_author,
    bsvhu.transportercompanysiret AS transporter_company_siret,
    bsvhu.transportercompanyname AS transporter_company_name,
    bsvhu.transportercompanyaddress AS transporter_company_address,
    bsvhu.transportercompanycontact AS transporter_company_contact,
    bsvhu.transportercompanymail AS transporter_company_mail,
    bsvhu.transportercompanyphone AS transporter_company_phone,
    bsvhu.transportercustominfo AS transporter_custom_info,
    bsvhu.transportercompanyvatnumber AS transporter_company_vat_number,
    bsvhu.transporterrecepissenumber AS transporter_recepisse_number,
    bsvhu.transporterrecepissedepartment AS transporter_recepisse_department,
    bsvhu.transporterrecepissevaliditylimit AS transporter_recepisse_validity_limit,
    bsvhu.transportertransportplates AS transporter_transport_plates,
    bsvhu.transportertransporttakenoverat AS transporter_transport_taken_over_at,
    bsvhu.transportertransportsignaturedate AS transporter_transport_signature_date,
    bsvhu.transportertransportsignatureauthor AS transporter_transport_signature_author,
    bsvhu.destinationcompanysiret AS destination_company_siret,
    bsvhu.destinationcompanyname AS destination_company_name,
    bsvhu.destinationcompanyaddress AS destination_company_address,
    bsvhu.destinationcompanycontact AS destination_company_contact,
    bsvhu.destinationcompanymail AS destination_company_mail,
    bsvhu.destinationcompanyphone AS destination_company_phone,
    bsvhu.destinationcustominfo AS destination_custom_info,
    bsvhu.destinationagrementnumber AS destination_agrement_number,
    bsvhu.destinationreceptiondate AS destination_reception_date,
    bsvhu.destinationreceptionquantity AS destination_reception_quantity,
    bsvhu.destinationreceptionidentificationnumbers AS destination_reception_identification_numbers,
    bsvhu.destinationreceptionidentificationtype AS destination_reception_identification_type,
    bsvhu.destinationreceptionacceptationstatus AS destination_reception_acceptation_status,
    bsvhu.destinationreceptionrefusalreason AS destination_reception_refusal_reason,
    bsvhu.destinationoperationdate AS destination_operation_date,
    bsvhu.destinationoperationsignaturedate AS destination_operation_signature_date,
    bsvhu.destinationoperationsignatureauthor AS destination_operation_signature_author,
    bsvhu.destinationtype AS destination_type,
    bsvhu.destinationoperationnextdestinationcompanysiret AS destination_operation_next_destination_company_siret,
    bsvhu.destinationoperationnextdestinationcompanyname AS destination_operation_next_destination_company_name,
    bsvhu.destinationoperationnextdestinationcompanyaddress AS destination_operation_next_destination_company_address,
    bsvhu.destinationoperationnextdestinationcompanycontact AS destination_operation_next_destination_company_contact,
    bsvhu.destinationoperationnextdestinationcompanymail AS destination_operation_next_destination_company_mail,
    bsvhu.destinationoperationnextdestinationcompanyphone AS destination_operation_next_destination_company_phone,
    bsvhu.destinationoperationnextdestinationcompanyvatnumber AS destination_operation_next_destination_company_vat_number,
    bsvhu.identificationnumbers AS identification_numbers,
    bsvhu.identificationtype AS identification_type,
    replace((bsvhu.destinationplannedoperationcode)::text, ' '::text, ''::text) AS destination_planned_operation_code,
    replace((bsvhu.destinationoperationcode)::text, ' '::text, ''::text) AS destination_operation_code,
    (bsvhu.weightvalue / (1000)::double precision) AS weight_value,
    (bsvhu.destinationreceptionweight / (1000)::double precision) AS destination_reception_weight
   FROM raw_zone_trackdechets.bsvhu;


ALTER TABLE trusted_zone_trackdechets.bsvhu OWNER TO pao;

--
-- Name: company; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.company AS
 SELECT company.id,
    company.siret,
    company.createdat AS created_at,
    company.updatedat AS updated_at,
    company.securitycode AS security_code,
    company.name,
    company.gerepid AS gerep_id,
    company.codenaf AS code_naf,
    company.givenname AS given_name,
    company.contactemail AS contact_email,
    company.contactphone AS contact_phone,
    company.website,
    company.transporterreceiptid AS transporter_receipt_id,
    company.traderreceiptid AS trader_receipt_id,
    company.ecoorganismeagreements AS eco_organisme_agreements,
    company.companytypes AS company_types,
    company.address,
    company.latitude,
    company.longitude,
    company.brokerreceiptid AS broker_receipt_id,
    company.verificationcode AS verification_code,
    company.verificationstatus AS verification_status,
    company.verificationmode AS verification_mode,
    company.verificationcomment AS verification_comment,
    company.verifiedat AS verified_at,
    company.vhuagrementdemolisseurid AS vhu_agrement_demolisseur_id,
    company.vhuagrementbroyeurid AS vhu_agrement_broyeur_id,
    company.allowbsdasritakeoverwithoutsignature AS allow_bsdasri_take_over_without_signature,
    company.vatnumber AS vat_number,
    company.contact,
    company.codedepartement AS code_departement,
    company.workercertificationid AS worker_certification_id
   FROM raw_zone_trackdechets.company;


ALTER TABLE trusted_zone_trackdechets.company OWNER TO pao;

--
-- Name: company_association; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.company_association AS
 SELECT companyassociation.id,
    companyassociation.role,
    companyassociation.companyid AS company_id,
    companyassociation.userid AS user_id
   FROM raw_zone_trackdechets.companyassociation;


ALTER TABLE trusted_zone_trackdechets.company_association OWNER TO pao;

--
-- Name: eco_organisme; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.eco_organisme AS
 SELECT ecoorganisme.id,
    ecoorganisme.siret,
    ecoorganisme.name,
    ecoorganisme.address,
    ecoorganisme.handlebsdasri AS handle_bsdasri
   FROM raw_zone_trackdechets.ecoorganisme;


ALTER TABLE trusted_zone_trackdechets.eco_organisme OWNER TO pao;

--
-- Name: trader_receipt; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.trader_receipt AS
 SELECT traderreceipt.id,
    traderreceipt.receiptnumber AS receipt_number,
    traderreceipt.validitylimit AS validity_limit,
    traderreceipt.department
   FROM raw_zone_trackdechets.traderreceipt;


ALTER TABLE trusted_zone_trackdechets.trader_receipt OWNER TO pao;

--
-- Name: transporter_receipt; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.transporter_receipt AS
 SELECT transporterreceipt.id,
    transporterreceipt.receiptnumber AS receipt_number,
    transporterreceipt.validitylimit AS validity_limit,
    transporterreceipt.department
   FROM raw_zone_trackdechets.transporterreceipt;


ALTER TABLE trusted_zone_trackdechets.transporter_receipt OWNER TO pao;

--
-- Name: user; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets."user" AS
 SELECT "user".id,
    "user".email,
    "user".name,
    "user".phone,
    "user".createdat AS created_at,
    "user".updatedat AS updated_at,
    "user".isactive AS is_active,
    "user".activatedat AS activated_at,
    "user".firstassociationdate AS first_association_date,
    "user".isadmin AS is_admin,
    "user".isregistrenational AS is_registre_national
   FROM raw_zone_trackdechets."user";


ALTER TABLE trusted_zone_trackdechets."user" OWNER TO pao;

--
-- Name: vhu_agrement; Type: VIEW; Schema: trusted_zone_trackdechets; Owner: pao
--

CREATE VIEW trusted_zone_trackdechets.vhu_agrement AS
 SELECT vhuagrement.id,
    vhuagrement.agrementnumber AS agrement_number,
    vhuagrement.department
   FROM raw_zone_trackdechets.vhuagrement;


ALTER TABLE trusted_zone_trackdechets.vhu_agrement OWNER TO pao;

--
-- Name: groups; Type: VIEW; Schema: trusted_zone_zammad; Owner: pao
--

CREATE VIEW trusted_zone_zammad.groups AS
 SELECT groups.id,
    groups.name,
    groups.created_at,
    groups.created_by_id,
    groups.updated_at,
    groups.updated_by_id,
    groups.active,
    groups.assignment_timeout,
    groups.email_address_id,
    groups.follow_up_assignment,
    groups.follow_up_possible,
    groups.note,
    groups.reopen_time_in_days,
    groups.shared_drafts,
    groups.signature_id,
    groups.user_ids
   FROM raw_zone_zammad.groups;


ALTER TABLE trusted_zone_zammad.groups OWNER TO pao;

--
-- Name: tags; Type: VIEW; Schema: trusted_zone_zammad; Owner: pao
--

CREATE VIEW trusted_zone_zammad.tags AS
 SELECT tags.ticket_id,
    tags.tags
   FROM raw_zone_zammad.tags;


ALTER TABLE trusted_zone_zammad.tags OWNER TO pao;

--
-- Name: tickets; Type: VIEW; Schema: trusted_zone_zammad; Owner: pao
--

CREATE VIEW trusted_zone_zammad.tickets AS
 SELECT tickets.id,
    tickets.number,
    tickets.created_at,
    tickets.created_by_id,
    tickets.updated_at,
    tickets.updated_by_id,
    tickets.title,
    tickets.article_count,
    tickets.article_ids,
    tickets.close_at,
    tickets.close_diff_in_min,
    tickets.close_escalation_at,
    tickets.close_in_min,
    tickets.create_article_sender_id,
    tickets.create_article_type_id,
    tickets.customer_id,
    tickets.escalation_at,
    tickets.first_response_at,
    tickets.first_response_diff_in_min,
    tickets.first_response_escalation_at,
    tickets.first_response_in_min,
    tickets.group_id,
    tickets.last_close_at,
    tickets.last_contact_agent_at,
    tickets.last_contact_at,
    tickets.last_contact_customer_at,
    tickets.last_owner_update_at,
    tickets.note,
    tickets.organization_id,
    tickets.owner_id,
    tickets.pending_time,
    tickets.priority_id,
    tickets.state_id,
    tickets.ticket_time_accounting_ids,
    tickets.time_unit,
    tickets.type,
    tickets.update_diff_in_min,
    tickets.update_escalation_at,
    tickets.update_in_min
   FROM raw_zone_zammad.tickets;


ALTER TABLE trusted_zone_zammad.tickets OWNER TO pao;

--
-- Name: users; Type: VIEW; Schema: trusted_zone_zammad; Owner: pao
--

CREATE VIEW trusted_zone_zammad.users AS
 SELECT users.id,
    users.created_at,
    users.created_by_id,
    users.updated_at,
    users.updated_by_id,
    users.active,
    users.verified,
    users.login,
    users.email,
    users.firstname,
    users.lastname,
    users.address,
    users.authorization_ids,
    users.city,
    users.country,
    users.department,
    users.fax,
    users.group_ids,
    users.image,
    users.image_source,
    users.karma_user_ids,
    users.last_login,
    users.login_failed,
    users.mobile,
    users.note,
    users.organization_id,
    users.organization_ids,
    users.out_of_office,
    users.out_of_office_end_at,
    users.out_of_office_replacement_id,
    users.out_of_office_start_at,
    users.phone,
    users.role_ids,
    users.source,
    users.street,
    users.vip,
    users.web,
    users.zip
   FROM raw_zone_zammad.users;


ALTER TABLE trusted_zone_zammad.users OWNER TO pao;

--
-- Name: brokerreceipt brokerreceipt_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.brokerreceipt
    ADD CONSTRAINT brokerreceipt_pkey PRIMARY KEY (id);


--
-- Name: bsda bsda_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.bsda
    ADD CONSTRAINT bsda_pkey PRIMARY KEY (id);


--
-- Name: bsdarevisionrequest bsdarevisionrequest_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.bsdarevisionrequest
    ADD CONSTRAINT bsdarevisionrequest_pkey PRIMARY KEY (id);


--
-- Name: bsdasri bsdasri_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.bsdasri
    ADD CONSTRAINT bsdasri_pkey PRIMARY KEY (id);


--
-- Name: bsddrevisionrequest bsddrevisionrequest_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.bsddrevisionrequest
    ADD CONSTRAINT bsddrevisionrequest_pkey PRIMARY KEY (id);


--
-- Name: bsff bsff_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.bsff
    ADD CONSTRAINT bsff_pkey PRIMARY KEY (id);


--
-- Name: bsffpackaging bsffpackaging_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.bsffpackaging
    ADD CONSTRAINT bsffpackaging_pkey PRIMARY KEY (id);


--
-- Name: bsvhu bsvhu_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.bsvhu
    ADD CONSTRAINT bsvhu_pkey PRIMARY KEY (id);


--
-- Name: company company_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.company
    ADD CONSTRAINT company_pkey PRIMARY KEY (id);


--
-- Name: companyassociation companyassociation_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.companyassociation
    ADD CONSTRAINT companyassociation_pkey PRIMARY KEY (id);


--
-- Name: ecoorganisme ecoorganisme_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.ecoorganisme
    ADD CONSTRAINT ecoorganisme_pkey PRIMARY KEY (id);


--
-- Name: form form_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.form
    ADD CONSTRAINT form_pkey PRIMARY KEY (id);


--
-- Name: traderreceipt traderreceipt_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.traderreceipt
    ADD CONSTRAINT traderreceipt_pkey PRIMARY KEY (id);


--
-- Name: transporterreceipt transporterreceipt_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.transporterreceipt
    ADD CONSTRAINT transporterreceipt_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: vhuagrement vhuagrement_pkey; Type: CONSTRAINT; Schema: raw_zone_trackdechets; Owner: pao
--

ALTER TABLE ONLY raw_zone_trackdechets.vhuagrement
    ADD CONSTRAINT vhuagrement_pkey PRIMARY KEY (id);


--
-- Name: groups groups_pkey; Type: CONSTRAINT; Schema: raw_zone_zammad; Owner: pao
--

ALTER TABLE ONLY raw_zone_zammad.groups
    ADD CONSTRAINT groups_pkey PRIMARY KEY (id);


--
-- Name: organizations organizations_pkey; Type: CONSTRAINT; Schema: raw_zone_zammad; Owner: pao
--

ALTER TABLE ONLY raw_zone_zammad.organizations
    ADD CONSTRAINT organizations_pkey PRIMARY KEY (id);


--
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: raw_zone_zammad; Owner: pao
--

ALTER TABLE ONLY raw_zone_zammad.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (ticket_id);


--
-- Name: tickets tickets_pkey; Type: CONSTRAINT; Schema: raw_zone_zammad; Owner: pao
--

ALTER TABLE ONLY raw_zone_zammad.tickets
    ADD CONSTRAINT tickets_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: raw_zone_zammad; Owner: pao
--

ALTER TABLE ONLY raw_zone_zammad.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: commune_com_idx; Type: INDEX; Schema: raw_zone_insee; Owner: pao
--

CREATE INDEX commune_com_idx ON raw_zone_insee.commune USING btree (com);


--
-- Name: stock_etablissement_siret_idx; Type: INDEX; Schema: raw_zone_insee; Owner: pao
--

CREATE UNIQUE INDEX stock_etablissement_siret_idx ON raw_zone_insee.stock_etablissement USING btree (siret);


--
-- Name: bsda_createdat_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsda_createdat_idx ON raw_zone_trackdechets.bsda USING btree (createdat);


--
-- Name: bsda_destinationcompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsda_destinationcompanysiret_idx ON raw_zone_trackdechets.bsda USING btree (destinationcompanysiret);


--
-- Name: bsda_emittercompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsda_emittercompanysiret_idx ON raw_zone_trackdechets.bsda USING btree (emittercompanysiret);


--
-- Name: bsda_transportercompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsda_transportercompanysiret_idx ON raw_zone_trackdechets.bsda USING btree (transportercompanysiret);


--
-- Name: bsdasri_createdat_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsdasri_createdat_idx ON raw_zone_trackdechets.bsdasri USING btree (createdat);


--
-- Name: bsdasri_destinationcompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsdasri_destinationcompanysiret_idx ON raw_zone_trackdechets.bsdasri USING btree (destinationcompanysiret);


--
-- Name: bsdasri_emittercompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsdasri_emittercompanysiret_idx ON raw_zone_trackdechets.bsdasri USING btree (emittercompanysiret);


--
-- Name: bsdasri_transportercompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsdasri_transportercompanysiret_idx ON raw_zone_trackdechets.bsdasri USING btree (transportercompanysiret);


--
-- Name: bsff_createdat_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsff_createdat_idx ON raw_zone_trackdechets.bsff USING btree (createdat);


--
-- Name: bsff_destinationcompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsff_destinationcompanysiret_idx ON raw_zone_trackdechets.bsff USING btree (destinationcompanysiret);


--
-- Name: bsff_emittercompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsff_emittercompanysiret_idx ON raw_zone_trackdechets.bsff USING btree (emittercompanysiret);


--
-- Name: bsff_transportercompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsff_transportercompanysiret_idx ON raw_zone_trackdechets.bsff USING btree (transportercompanysiret);


--
-- Name: bsvhu_createdat_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsvhu_createdat_idx ON raw_zone_trackdechets.bsvhu USING btree (createdat);


--
-- Name: bsvhu_destinationcompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsvhu_destinationcompanysiret_idx ON raw_zone_trackdechets.bsvhu USING btree (destinationcompanysiret);


--
-- Name: bsvhu_emittercompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsvhu_emittercompanysiret_idx ON raw_zone_trackdechets.bsvhu USING btree (emittercompanysiret);


--
-- Name: bsvhu_transportercompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX bsvhu_transportercompanysiret_idx ON raw_zone_trackdechets.bsvhu USING btree (transportercompanysiret);


--
-- Name: company_createdat_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX company_createdat_idx ON raw_zone_trackdechets.company USING btree (createdat);


--
-- Name: company_siret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX company_siret_idx ON raw_zone_trackdechets.company USING btree (siret);


--
-- Name: form_createdat_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX form_createdat_idx ON raw_zone_trackdechets.form USING btree (createdat);


--
-- Name: form_emittercompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX form_emittercompanysiret_idx ON raw_zone_trackdechets.form USING btree (emittercompanysiret);


--
-- Name: form_recipientcompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX form_recipientcompanysiret_idx ON raw_zone_trackdechets.form USING btree (recipientcompanysiret);


--
-- Name: form_transportercompanysiret_idx; Type: INDEX; Schema: raw_zone_trackdechets; Owner: pao
--

CREATE INDEX form_transportercompanysiret_idx ON raw_zone_trackdechets.form USING btree (transportercompanysiret);


--
-- Name: tickets_created_at_idx; Type: INDEX; Schema: raw_zone_zammad; Owner: pao
--

CREATE INDEX tickets_created_at_idx ON raw_zone_zammad.tickets USING btree (created_at);


--
-- Name: tickets_number_idx; Type: INDEX; Schema: raw_zone_zammad; Owner: pao
--

CREATE INDEX tickets_number_idx ON raw_zone_zammad.tickets USING btree (number);


--
-- Name: 28756f6bc38fc5b8de76ae3ea2af7210; Type: INDEX; Schema: refined_zone_analytics; Owner: pao
--

CREATE INDEX "28756f6bc38fc5b8de76ae3ea2af7210" ON refined_zone_analytics.moulinette_dechetteries USING btree (siret);


--
-- Name: 2ab4c3eaeff9f62ba170e212019aa01b; Type: INDEX; Schema: refined_zone_analytics; Owner: pao
--

CREATE UNIQUE INDEX "2ab4c3eaeff9f62ba170e212019aa01b" ON refined_zone_analytics.identification_eco_organismes USING btree (siret);


--
-- Name: 6c202c788c0a67269fa2baef7b7ce838; Type: INDEX; Schema: refined_zone_analytics; Owner: pao
--

CREATE UNIQUE INDEX "6c202c788c0a67269fa2baef7b7ce838" ON refined_zone_analytics.bordereaux_counts_by_siret USING btree (siret);


--
-- Name: 167a7bfe672b692a1a64d6b69bd4368a; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "167a7bfe672b692a1a64d6b69bd4368a" ON refined_zone_enriched.bsdd_enriched USING btree (recipient_company_siret);


--
-- Name: 16c671a838e702278c5658cabbd06379; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "16c671a838e702278c5658cabbd06379" ON refined_zone_enriched.bsdasri_enriched USING btree (destination_operation_date);


--
-- Name: 1cc626e603755f64ce96ef30d93769bc; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "1cc626e603755f64ce96ef30d93769bc" ON refined_zone_enriched.bsda_enriched USING btree (waste_code);


--
-- Name: 1e9314d9869f4b651006749a10c3f167; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "1e9314d9869f4b651006749a10c3f167" ON refined_zone_enriched.bsda_enriched USING btree (destination_company_siret);


--
-- Name: 32c0deba13829ffbf15ade8db59f19c7; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE UNIQUE INDEX "32c0deba13829ffbf15ade8db59f19c7" ON refined_zone_enriched.bsdasri_enriched USING btree (id);


--
-- Name: 362a5c06a4802f4e0057b1bd7abe40f7; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "362a5c06a4802f4e0057b1bd7abe40f7" ON refined_zone_enriched.bsdasri_enriched USING btree (emitter_company_siret);


--
-- Name: 41ab69646e6f8568b31a2bbc52b13e7c; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "41ab69646e6f8568b31a2bbc52b13e7c" ON refined_zone_enriched.bsvhu_enriched USING btree (waste_code);


--
-- Name: 500cd7b82fd6a03d1a6fda24f642cb75; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "500cd7b82fd6a03d1a6fda24f642cb75" ON refined_zone_enriched.bsvhu_enriched USING btree (emitter_company_siret);


--
-- Name: 54c8c4b6fb291ffb3296f8594c29158b; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "54c8c4b6fb291ffb3296f8594c29158b" ON refined_zone_enriched.bsdd_enriched USING btree (processed_at);


--
-- Name: 5694d40d6ed49b78fbd67157edd685aa; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE UNIQUE INDEX "5694d40d6ed49b78fbd67157edd685aa" ON refined_zone_enriched.bsdd_enriched USING btree (id);


--
-- Name: 575d4f91e1ad6a9df5e7a1b11f5f2aba; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "575d4f91e1ad6a9df5e7a1b11f5f2aba" ON refined_zone_enriched.bsdd_enriched USING btree (emitter_company_siret);


--
-- Name: 61dd46cbde4168a2b09663a3f7eeb5f4; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "61dd46cbde4168a2b09663a3f7eeb5f4" ON refined_zone_enriched.bsff_enriched USING btree (transporter_company_siret);


--
-- Name: 64205afa7f0ccf5dab4af76a2b685f7b; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "64205afa7f0ccf5dab4af76a2b685f7b" ON refined_zone_enriched.bsff_enriched USING btree (waste_code);


--
-- Name: 6d3d4ffb74c1ea4b9e9be3abeca73897; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "6d3d4ffb74c1ea4b9e9be3abeca73897" ON refined_zone_enriched.bsvhu_enriched USING btree (transporter_company_siret);


--
-- Name: 6eb6de1ec01fbcda9df603dbc016b827; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE UNIQUE INDEX "6eb6de1ec01fbcda9df603dbc016b827" ON refined_zone_enriched.bsvhu_enriched USING btree (id);


--
-- Name: 74ca3d5ac76c230072e15a611a1b366a; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "74ca3d5ac76c230072e15a611a1b366a" ON refined_zone_enriched.bsff_enriched USING btree (emitter_company_siret);


--
-- Name: 7b6e04c7104d5ac38f092f07892ea70b; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "7b6e04c7104d5ac38f092f07892ea70b" ON refined_zone_enriched.bsdd_enriched USING btree (waste_details_code);


--
-- Name: 7d1d3766e08a2bd1d8b32e842c51fbb3; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "7d1d3766e08a2bd1d8b32e842c51fbb3" ON refined_zone_enriched.bsff_enriched USING btree (created_at);


--
-- Name: 816f5d0536e091503426b650a4997cab; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "816f5d0536e091503426b650a4997cab" ON refined_zone_enriched.bsvhu_enriched USING btree (destination_company_siret);


--
-- Name: 8398920fc0bd67dbc88ebbf7590fd16a; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE UNIQUE INDEX "8398920fc0bd67dbc88ebbf7590fd16a" ON refined_zone_enriched.bsff_enriched USING btree (id);


--
-- Name: 88c7b90f0acfcc9c16f14f40890f17f1; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE UNIQUE INDEX "88c7b90f0acfcc9c16f14f40890f17f1" ON refined_zone_enriched.bsda_enriched USING btree (id);


--
-- Name: 8a470e2f11a41dbb52ee3452f5e92ffd; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "8a470e2f11a41dbb52ee3452f5e92ffd" ON refined_zone_enriched.bsda_enriched USING btree (created_at);


--
-- Name: 90ca067ccacb92ad28fe7beca3a3a178; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "90ca067ccacb92ad28fe7beca3a3a178" ON refined_zone_enriched.bsdasri_enriched USING btree (transporter_company_siret);


--
-- Name: 988dae71b43410708dbf50f29e6cc766; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX "988dae71b43410708dbf50f29e6cc766" ON refined_zone_enriched.bsdasri_enriched USING btree (created_at);


--
-- Name: b3588a6dd328e29d2049917ff891116a; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX b3588a6dd328e29d2049917ff891116a ON refined_zone_enriched.bsvhu_enriched USING btree (created_at);


--
-- Name: bccf953d169310a7b3787d8ef0d73fee; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX bccf953d169310a7b3787d8ef0d73fee ON refined_zone_enriched.bsda_enriched USING btree (emitter_company_siret);


--
-- Name: cbbc98e33e59909e5ab0a5b2dbc742cb; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX cbbc98e33e59909e5ab0a5b2dbc742cb ON refined_zone_enriched.bsdasri_enriched USING btree (destination_company_siret);


--
-- Name: d247f3fad5c5d1bffe5997595b76ddfc; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX d247f3fad5c5d1bffe5997595b76ddfc ON refined_zone_enriched.bsdasri_enriched USING btree (waste_code);


--
-- Name: d386197f032949c27debbb9c4f5f2c80; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX d386197f032949c27debbb9c4f5f2c80 ON refined_zone_enriched.bsdd_enriched USING btree (transporter_company_siret);


--
-- Name: dacd9a12d633a835d39ee9470fc3c04d; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX dacd9a12d633a835d39ee9470fc3c04d ON refined_zone_enriched.bsdd_enriched USING btree (created_at);


--
-- Name: db2940b096ca56164079eb3083819756; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX db2940b096ca56164079eb3083819756 ON refined_zone_enriched.bsff_enriched USING btree (destination_company_siret);


--
-- Name: e46be46f9f5bde83a69d2d6fa4ddc68d; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX e46be46f9f5bde83a69d2d6fa4ddc68d ON refined_zone_enriched.bsvhu_enriched USING btree (destination_operation_date);


--
-- Name: f141cfc42b751cce244a251f4343e679; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX f141cfc42b751cce244a251f4343e679 ON refined_zone_enriched.bsda_enriched USING btree (transporter_company_siret);


--
-- Name: fc3826ba754ad47106cb25f17f444869; Type: INDEX; Schema: refined_zone_enriched; Owner: pao
--

CREATE INDEX fc3826ba754ad47106cb25f17f444869 ON refined_zone_enriched.bsda_enriched USING btree (destination_operation_date);


--
-- Name: 2a233b2fcdd2f1ff9f360cc347ca8af6; Type: INDEX; Schema: refined_zone_icpe; Owner: pao
--

CREATE UNIQUE INDEX "2a233b2fcdd2f1ff9f360cc347ca8af6" ON refined_zone_icpe.reconciliation_exutoires_georisques_td USING btree (siret);


--
-- Name: 05cc72e705dc73526103f67872963a84; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "05cc72e705dc73526103f67872963a84" ON refined_zone_stats_publiques.bsvhu_received_by_week USING btree (week);


--
-- Name: 35c0058c0bbd19a5aa54387c96d62360; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "35c0058c0bbd19a5aa54387c96d62360" ON refined_zone_stats_publiques.bsda_processed_by_week USING btree (week);


--
-- Name: 3b0ed4069afb74ee14fcc588631e42c9; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "3b0ed4069afb74ee14fcc588631e42c9" ON refined_zone_stats_publiques.bsdd_processed_by_week USING btree (week);


--
-- Name: 3ec3cdd178a485209f10143e84174b3e; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "3ec3cdd178a485209f10143e84174b3e" ON refined_zone_stats_publiques.bsff_received_by_week USING btree (week);


--
-- Name: 42e3b9a348500bb5a6cb6984974651e9; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "42e3b9a348500bb5a6cb6984974651e9" ON refined_zone_stats_publiques.bsvhu_created_by_week USING btree (week);


--
-- Name: 570d13b503d16ec8e976c4c21aa4e38e; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "570d13b503d16ec8e976c4c21aa4e38e" ON refined_zone_stats_publiques.bsda_sent_by_week USING btree (week);


--
-- Name: 59c8bbd1941e4232187af4bc6c7b5dc2; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "59c8bbd1941e4232187af4bc6c7b5dc2" ON refined_zone_stats_publiques.bsff_emitted_by_week USING btree (week);


--
-- Name: 5ab9a6460930ec391811a2b925afea6c; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "5ab9a6460930ec391811a2b925afea6c" ON refined_zone_stats_publiques.bsdasri_created_by_week USING btree (week);


--
-- Name: 5fe327db207efb438721ad00a8270874; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "5fe327db207efb438721ad00a8270874" ON refined_zone_stats_publiques.bsff_created_by_week USING btree (week);


--
-- Name: 667a0a30f199c796e00c7c4d89e44a81; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "667a0a30f199c796e00c7c4d89e44a81" ON refined_zone_stats_publiques.bsdd_created_by_week USING btree (week);


--
-- Name: 6a53aa5783edfb9695334cd2f6bc7a05; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "6a53aa5783edfb9695334cd2f6bc7a05" ON refined_zone_stats_publiques.bsdasri_emitted_by_week USING btree (week);


--
-- Name: 7836c63b2b6fc8ef6a0d012b6f84a8aa; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "7836c63b2b6fc8ef6a0d012b6f84a8aa" ON refined_zone_stats_publiques.bsvhu_sent_by_week USING btree (week);


--
-- Name: 7fc1b41c15234e65a50a666003e2bb69; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "7fc1b41c15234e65a50a666003e2bb69" ON refined_zone_stats_publiques.bsdd_emitted_by_week USING btree (week);


--
-- Name: 804fa3f52c9d5f0bbbfcb68346998e85; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "804fa3f52c9d5f0bbbfcb68346998e85" ON refined_zone_stats_publiques.bsdasri_sent_by_week USING btree (week);


--
-- Name: 85715752f746b873dad7328e832f79c2; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX "85715752f746b873dad7328e832f79c2" ON refined_zone_stats_publiques.bsff_sent_by_week USING btree (week);


--
-- Name: a4368d4599e1cd3a8a213f42c0d99963; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX a4368d4599e1cd3a8a213f42c0d99963 ON refined_zone_stats_publiques.bsdasri_processed_by_week USING btree (week);


--
-- Name: a8c65de4eb4b4d8dd8da36a4795a0152; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX a8c65de4eb4b4d8dd8da36a4795a0152 ON refined_zone_stats_publiques.bsdasri_received_by_week USING btree (week);


--
-- Name: af1a6e89f9353d5973619d937c2e5f94; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX af1a6e89f9353d5973619d937c2e5f94 ON refined_zone_stats_publiques.bsda_emitted_by_week USING btree (week);


--
-- Name: b5f78732c836edfc55124a8a0aac3588; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX b5f78732c836edfc55124a8a0aac3588 ON refined_zone_stats_publiques.bsff_packagings_processed_by_week USING btree (week);


--
-- Name: c2f8a98bce0de9acaa58d363ac0d9510; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX c2f8a98bce0de9acaa58d363ac0d9510 ON refined_zone_stats_publiques.bsda_created_by_week USING btree (week);


--
-- Name: c73b251d1d1540ba6c46eb60617a3bd9; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX c73b251d1d1540ba6c46eb60617a3bd9 ON refined_zone_stats_publiques.bsda_received_by_week USING btree (week);


--
-- Name: dcf9307ee23faf0e1b3021afab86bdbf; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX dcf9307ee23faf0e1b3021afab86bdbf ON refined_zone_stats_publiques.bsvhu_emitted_by_week USING btree (week);


--
-- Name: e077b6fff640977acd4f7febfddd88e5; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX e077b6fff640977acd4f7febfddd88e5 ON refined_zone_stats_publiques.bsvhu_processed_by_week USING btree (week);


--
-- Name: e597649191e9b7cb3bd8074d80cacae7; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX e597649191e9b7cb3bd8074d80cacae7 ON refined_zone_stats_publiques.bsdd_sent_by_week USING btree (week);


--
-- Name: ebe8c258febed72c37da55d7fc8b8245; Type: INDEX; Schema: refined_zone_stats_publiques; Owner: pao
--

CREATE UNIQUE INDEX ebe8c258febed72c37da55d7fc8b8245 ON refined_zone_stats_publiques.bsdd_received_by_week USING btree (week);


--
-- Name: ix_trusted_zone_mapping_rubrique_code_operation_index; Type: INDEX; Schema: trusted_zone; Owner: pao
--

CREATE INDEX ix_trusted_zone_mapping_rubrique_code_operation_index ON trusted_zone.mapping_rubrique_code_operation USING btree (code_operation);


--
-- Name: ix_trusted_zone_gsheet_gerep_amiante_index; Type: INDEX; Schema: trusted_zone_gsheet; Owner: pao
--

CREATE INDEX ix_trusted_zone_gsheet_gerep_amiante_index ON trusted_zone_gsheet.gerep_amiante USING btree (index);


--
-- Name: ix_trusted_zone_gsheet_gerep_traiteurs_amiante_index; Type: INDEX; Schema: trusted_zone_gsheet; Owner: pao
--

CREATE INDEX ix_trusted_zone_gsheet_gerep_traiteurs_amiante_index ON trusted_zone_gsheet.gerep_traiteurs_amiante USING btree (index);


--
-- PostgreSQL database dump complete
--

