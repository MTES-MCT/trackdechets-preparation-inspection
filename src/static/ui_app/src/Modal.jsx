import React, { useState } from "react";

export const Modal = ({ children }) => {
  return (
    <dialog
      aria-labelledby="fr-modal-title-modal-4"
      role="dialog"
      className="fr-modal fr-modal--opened"
    >
      <div className="fr-container fr-container--fluid fr-container-md">
        <div className="fr-grid-row fr-grid-row--center">
          <div className="fr-col-10">
            <div className="fr-modal__body">
              <div className="fr-modal__header">
                <button
                  className="fr-btn--close fr-btn"
                  title="Fermer la fenêtre modale"
                  aria-controls="fr-modal-4"
                  target="_self"
                >
                  Fermer
                </button>
              </div>
              <div className="fr-modal__content">{children}</div>
            </div>
          </div>
        </div>
      </div>
    </dialog>
  );
};
