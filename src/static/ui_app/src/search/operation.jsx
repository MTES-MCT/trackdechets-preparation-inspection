import { useState } from "react";

const ProcessingCodes = () => {
  const [selectedCodes, setSelectedCodes] = useState([]);

  const codes = {
    R1: {
      code: "R1",
      description:
        "Utilisation principale comme combustible ou autre moyen de produire de l'énergie",
    },
    R2: {
      code: "R2",
      description: "Récupération ou régénération des solvants",
    },
    R3: {
      code: "R3",
      description:
        "Recyclage ou récupération des substances organiques qui ne sont pas utilisées comme solvants (y compris les opérations de compostage et autres transformations biologiques)",
    },
    R5: {
      code: "R5",
      description: "Recyclage ou récupération d'autres matières inorganiques",
    },
    R12: {
      code: "R12",
      description:
        "Échange de déchets en vue de les soumettre à l'une des opérations numérotées R1 à R11",
    },
    R13: {
      code: "R13",
      description:
        "Stockage de déchets préalablement à l'une des opérations R1 à R12 (à l'exclusion du stockage temporaire, avant collecte, sur le site de production).",
    },
    D10: {
      code: "D10",
      description: "Incinération à terre",
    },
    D13: {
      code: "D13",
      description:
        "Regroupement préalablement à l'une des opérations numérotées D1 à D12",
    },
    D14: {
      code: "D14",
      description:
        "Reconditionnement préalablement à l'une des opérations numérotées D1 à D13",
    },
    D15: {
      code: "D15",
      description:
        "Stockage préalablement à l'une des opérations D1 à D14 (à l'exclusion du stockage temporaire, avant collecte, sur le site de production).",
    },
  };

  const handleToggleCode = (code) => {
    if (selectedCodes.includes(code)) {
      setSelectedCodes(selectedCodes.filter((c) => c !== code));
    } else {
      setSelectedCodes([...selectedCodes, code]);
    }
  };

  return (
    <div>
      <h2>Codes de traitement des déchets</h2>

      <div>
        <div>
          {Object.entries(codes).map(([key, item]) => (
            <div key={key} className="fr-fieldset__element">
              <div className="fr-checkbox-group">
                <input
                  type="checkbox"
                  id={item.code}
                  checked={selectedCodes.includes(item.code)}
                  onChange={() => handleToggleCode(item.code)}
                />
                <label htmlFor={item.code}>
                  {item.code} - {item.description}
                </label>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ProcessingCodes;
