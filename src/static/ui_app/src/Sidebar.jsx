import { SelectWithSubOptions } from "./SelectWithSubOptions.jsx";
import { useMapStore } from "./Store";
import { useShallow } from "zustand/react/shallow";
import {
  BSDS_OPTIONS,
  PROCESSING_CODES_OPTIONS,
  PROFILE_OPTIONS,
  FRENCH_DEPARTEMENTS,
} from "./constants";

export function Sidebar({ mapRef }) {
  const {
    bsdFilters,
    profileFilters,
    operationCodeFilters,

    departmentFilters,

    addFilter,
    removeFilter,
    clearFilter,
  } = useMapStore(
    useShallow((state) => ({
      bsdFilters: state.bsdFilters,
      profileFilters: state.profileFilters,
      operationCodeFilters: state.operationCodeFilters,
      departmentFilters: state.departmentFilters,

      addFilter: state.addFilter,
      removeFilter: state.removeFilter,
      clearFilter: state.clearFilter,
    })),
  );
  return (
    <div className="map__sidebar">
      <div>
        <FlyTo
          mapRef={mapRef}
          lat={46.2321}
          long={2.209667}
          zoom={5}
          label="Métropole"
        />
        <FlyTo
          mapRef={mapRef}
          lat={14.63554}
          long={-61.02281}
          label="Martinique"
        />
        <FlyTo
          mapRef={mapRef}
          lat={16.1922}
          long={-61.272382}
          label="Guadeloupe"
        />
        <FlyTo mapRef={mapRef} lat={-21.114} long={55.532} label="La Réunion" />
        <FlyTo
          mapRef={mapRef}
          lat={3.9517949}
          long={-53.07822}
          label="Guyane"
          zoom={7}
        />
        <FlyTo
          mapRef={mapRef}
          lat={-12.82451}
          long={45.165455}
          label="Mayotte"
          zoom={7}
        />
      </div>
      <p className="fr-text--lg fr-text--bold">Je cherche des établissements</p>
      <button className="fr-btn fr-btn--secondary fr-icon-equalizer-line  fr-btn--icon-right">
        Paramétrer les filtres
      </button>

      <div className="fr-select-group">
        <label className="fr-label" htmlFor="id_profile_select">
          Déchets
        </label>
        <SelectWithSubOptions
          options={BSDS_OPTIONS}
          filterKey="bsdFilters"
          selected={bsdFilters}
          onAdd={addFilter}
          onRemove={removeFilter}
          onClear={clearFilter}
        />
      </div>
      <div className="fr-select-group">
        <label className="fr-label" htmlFor="id_profile_select">
          Profil
        </label>
        <SelectWithSubOptions
          options={PROFILE_OPTIONS}
          filterKey="profileFilters"
          selected={profileFilters}
          onAdd={addFilter}
          onRemove={removeFilter}
          onClear={clearFilter}
        />
      </div>

      <div className="fr-select-group">
        <label className="fr-label" htmlFor="id_profile_select">
          Code opération
        </label>
        <SelectWithSubOptions
          options={PROCESSING_CODES_OPTIONS}
          filterKey="operationCodeFilters"
          selected={operationCodeFilters}
          onAdd={addFilter}
          onRemove={removeFilter}
          onClear={clearFilter}
        />
      </div>

      <div className="fr-select-group">
        <label className="fr-label" htmlFor="id_profile_select">
          Département
        </label>
        <SelectWithSubOptions
          options={FRENCH_DEPARTEMENTS}
          filterKey="departmentFilters"
          selected={departmentFilters}
          onAdd={addFilter}
          onRemove={removeFilter}
          onClear={clearFilter}
        />
      </div>
    </div>
  );
}

const FlyTo = ({ mapRef, lat, long, label, zoom = 9 }) => {
  return (
    <button
      className="fr-btn fr-btn--sm  fr-btn--secondary fr-ml-1v fr-mb-1v"
      onClick={() => mapRef.current.flyTo({ center: [long, lat], zoom })}
    >
      {label}
    </button>
  );
};
