import React from "react";
import { Modal } from "../Modal.jsx";
import ProcessingCodes from "./operation.jsx";
import WasteTypes from "./WasteTypes.tsx";
import Profiles from "./Profiles.tsx";
import Departments from "./Departments.tsx";

export const Filters = () => {
  return (
    <Modal>
      <h1 id="fr-modal-title-modal-4" className="fr-modal__title">
        Paramétrer les filtres
      </h1>
      <p>Je recherche par</p>
      <p>
        <label>
          <input type="radio" name="d" /> Types de déchets et rôles
        </label>
        <label className="fr-ml-2w">
          <input type="radio" name="d" /> Code déchet
        </label>
      </p>
      <div className="fr-tabs">
        <ul className="fr-tabs__list" role="tablist" aria-label="Filtres">
          <li role="presentation">
            <button
              id="tabpanel-001"
              className="fr-tabs__tab fr-icon-checkbox-line fr-tabs__tab--icon-left"
              tabIndex="0"
              role="tab"
              aria-selected="true"
              aria-controls="tabpanel-001-panel"
            >
              Types de déchets et rôles
            </button>
          </li>
          <li role="presentation">
            <button
              id="tabpanel-002"
              className="fr-tabs__tab fr-icon-checkbox-line fr-tabs__tab--icon-left"
              tabIndex="-1"
              role="tab"
              aria-selected="false"
              aria-controls="tabpanel-002-panel"
            >
              Traitement réalisé
            </button>
          </li>
          <li role="presentation">
            <button
              id="tabpanel-003"
              className="fr-tabs__tab fr-icon-checkbox-line fr-tabs__tab--icon-left"
              tabIndex="-1"
              role="tab"
              aria-selected="false"
              aria-controls="tabpanel-003-panel"
            >
              Profils
            </button>
          </li>
          <li role="presentation">
            <button
              id="tabpanel-004"
              className="fr-tabs__tab fr-icon-checkbox-line fr-tabs__tab--icon-left"
              tabIndex="-1"
              role="tab"
              aria-selected="false"
              aria-controls="tabpanel-004-panel"
            >
              Départements
            </button>
          </li>
        </ul>
        <div
          id="tabpanel-001-panel"
          className="fr-tabs__panel fr-tabs__panel--selected"
          role="tabpanel"
          aria-labelledby="tabpanel-001"
          tabIndex="0"
        >
          <WasteTypes />
        </div>
        <div
          id="tabpanel-002-panel"
          className="fr-tabs__panel"
          role="tabpanel"
          aria-labelledby="tabpanel-002"
          tabIndex="0"
        >
          <div>
            <ProcessingCodes />
          </div>
        </div>
        <div
          id="tabpanel-003-panel"
          className="fr-tabs__panel"
          role="tabpanel"
          aria-labelledby="tabpanel-003"
          tabIndex="0"
        >
          <Profiles />
        </div>
        <div
          id="tabpanel-004-panel"
          className="fr-tabs__panel"
          role="tabpanel"
          aria-labelledby="tabpanel-004"
          tabIndex="0"
        >
          <Departments />
        </div>
      </div>
    </Modal>
  );
};
