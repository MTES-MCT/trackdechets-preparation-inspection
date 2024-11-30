import { SelectWithSubOptions } from "./SelectWithSubOptions.jsx";
import { useMapStore } from "./Store";
import { useShallow } from "zustand/react/shallow";
import {
  BSDS_OPTIONS,
  PROCESSING_CODES_OPTIONS,
  PROFILE_OPTIONS,
} from "./constants";

export function Sidebar({ mapRef }) {
  const {
    bsdFilters,
    profileFilters,
    operationCodeFilters,
    addBsdFilter,
    removeBsdFilter,
    addProfileFilter,
    removeProfileFilter,
    addOperationCodeFilter,
    removeOperationCodeFilter,
  } = useMapStore(
    useShallow((state) => ({
      bsdFilters: state.bsdFilters,
      profileFilters: state.profileFilters,
      operationCodeFilters: state.operationCodeFilters,

      addBsdFilter: state.addBsdFilter,
      removeBsdFilter: state.removeBsdFilter,
      addProfileFilter: state.addProfileFilter,
      removeProfileFilter: state.removeProfileFilter,
      addOperationCodeFilter: state.addOperationCodeFilter,
      removeOperationCodeFilter: state.removeOperationCodeFilter,
    })),
  );

  return (
    <div className="map__sidebar">
      <p className="fr-text--lg fr-text--bold">Filtrer</p>

      <div className="fr-select-group">
        <label className="fr-label" htmlFor="id_profile_select">
          Déchets
        </label>
        <SelectWithSubOptions
          options={BSDS_OPTIONS}
          selected={bsdFilters}
          onAdd={addBsdFilter}
          onRemove={removeBsdFilter}
        />
      </div>
      <div className="fr-select-group">
        <label className="fr-label" htmlFor="id_profile_select">
          Profil
        </label>
        <SelectWithSubOptions
          options={PROFILE_OPTIONS}
          selected={profileFilters}
          onAdd={addProfileFilter}
          onRemove={removeProfileFilter}
        />
      </div>

      <div className="fr-select-group">
        <label className="fr-label" htmlFor="id_profile_select">
          Code opération
        </label>
        <SelectWithSubOptions
          options={PROCESSING_CODES_OPTIONS}
          selected={operationCodeFilters}
          onAdd={addOperationCodeFilter}
          onRemove={removeOperationCodeFilter}
        />
      </div>
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
