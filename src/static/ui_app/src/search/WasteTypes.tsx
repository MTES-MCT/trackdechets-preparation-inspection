const WasteTypes = () => {
  return (
    <div>
      <p>Types de déchets</p>
      <div className="fr-grid-row">
        <div className="fr-col">
          <div className="fr-fieldset__element">
            <div className="fr-radio-group">
              <input id="id_waste_type_1" type="radio" name="waste_type" />
              <label htmlFor="id_waste_type_1">Tous les types de déchets</label>
            </div>
          </div>

          <div className="fr-fieldset__element">
            <div className="fr-radio-group">
              <input id="id_waste_type_2" type="radio" name="waste_type" />
              <label htmlFor="id_waste_type_2">Amiante</label>
            </div>
          </div>

          <div className="fr-fieldset__element">
            <div className="fr-radio-group">
              <input id="id_waste_type_3" type="radio" name="waste_type" />
              <label htmlFor="id_waste_type_3">DASRI</label>
            </div>
          </div>

          <div className="fr-fieldset__element">
            <div className="fr-radio-group">
              <input id="id_waste_type_4" type="radio" name="waste_type" />
              <label htmlFor="id_waste_type_4">Déchets dangereux</label>
            </div>
          </div>

          <div className="fr-fieldset__element">
            <div className="fr-radio-group">
              <input id="id_waste_type_5" type="radio" name="waste_type" />
              <label htmlFor="id_waste_type_5">Déchets non dangereux</label>
            </div>
          </div>

          <div className="fr-fieldset__element">
            <div className="fr-radio-group">
              <input id="id_waste_type_6" type="radio" name="waste_type" />
              <label htmlFor="id_waste_type_6">Fluide frigorigène</label>
            </div>
          </div>
          <div className="fr-fieldset__element">
            <div className="fr-radio-group">
              <input id="id_waste_type_7" type="radio" name="waste_type" />
              <label htmlFor="id_waste_type_7">Terres & sédiments</label>
            </div>
          </div>
          <div className="fr-fieldset__element">
            <div className="fr-radio-group">
              <input id="id_waste_type_8" type="radio" name="waste_type" />
              <label htmlFor="id_waste_type_8">Véhicules hors d'usage</label>
            </div>
          </div>
        </div>

        <div className="fr-col">
          <fieldset
            className="fr-fieldset"
            id="checkboxes"
            aria-labelledby="checkboxes-legend checkboxes-messages"
          >
            <legend
              className="fr-fieldset__legend--regular fr-fieldset__legend"
              id="checkboxes-legend"
            >
              Rôle sur le bordereau
            </legend>
            <div className="fr-fieldset__element">
              <div className="fr-checkbox-group">
                <input
                  name="checkboxes-1"
                  id="checkboxes-1"
                  type="checkbox"
                  aria-describedby="checkboxes-1-messages"
                />
                <label className="fr-label" htmlFor="checkboxes-1">
                  Producteur - émetteur
                </label>
                <div
                  className="fr-messages-group"
                  id="checkboxes-1-messages"
                  aria-live="assertive"
                ></div>
              </div>
            </div>
            <div className="fr-fieldset__element">
              <div className="fr-checkbox-group">
                <input
                  name="checkboxes-2"
                  id="checkboxes-2"
                  type="checkbox"
                  aria-describedby="checkboxes-2-messages"
                />
                <label className="fr-label" htmlFor="checkboxes-2">
                  Transporteur
                </label>
                <div
                  className="fr-messages-group"
                  id="checkboxes-2-messages"
                  aria-live="assertive"
                ></div>
              </div>
            </div>
            <div className="fr-fieldset__element">
              <div className="fr-checkbox-group">
                <input
                  name="checkboxes-3"
                  id="checkboxes-3"
                  type="checkbox"
                  aria-describedby="checkboxes-3-messages"
                />
                <label className="fr-label" htmlFor="checkboxes-3">
                  Entreprise de travaux amiante
                </label>
                <div
                  className="fr-messages-group"
                  id="checkboxes-3-messages"
                  aria-live="assertive"
                ></div>
              </div>
            </div>{" "}
            <div className="fr-fieldset__element">
              <div className="fr-checkbox-group">
                <input
                  name="checkboxes-3"
                  id="checkboxes-3"
                  type="checkbox"
                  aria-describedby="checkboxes-3-messages"
                />
                <label className="fr-label" htmlFor="checkboxes-3">
                  Destinataire (lié au traitement réalisé)
                </label>
                <div
                  className="fr-messages-group"
                  id="checkboxes-3-messages"
                  aria-live="assertive"
                ></div>
              </div>
            </div>
            <div
              className="fr-messages-group"
              id="checkboxes-messages"
              aria-live="assertive"
            ></div>
          </fieldset>
        </div>
      </div>
    </div>
  );
};
export default WasteTypes;
