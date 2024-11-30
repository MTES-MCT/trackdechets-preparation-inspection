export const ZOOM_ETABS = 13;
export const ZOOM_CLUSTERS = 9;
export const ZOOM_DEPARTMENTS = 7;
// beyond: (6 to 1) regions

const broker = "BROKER";
/** Installation de Tri, transit regroupement de déchets */
const collector = "COLLECTOR";

/** Installation de valorisation de terres et sédiments */
const disposalfacility = "DISPOSAL_FACILITY";
/** Éco-organisme */
const ecoorganisme = "ECO_ORGANISME";
/** Intermédiaire : établissement qui peut être ajouté à une traçabilité, sans responsabilité réglementaire (y compris entreprises de travaux hors amiante) */
const intermediary = "INTERMEDIARY";
/** Producteur de déchet */
const producer = "PRODUCER";
/** Installation dans laquelle les déchets perdent leur statut de déchet */
const recoveryfacility = "RECOVERY_FACILITY";
/** Négociant */
const trader = "TRADER";
/** Transporteur */
const transporter = "TRANSPORTER";
/** Installation de traitement */
const wasteprocessor = "WASTEPROCESSOR";
/** Installation de collecte de déchets apportés par le producteur initial (Rubrique 2710) */
const wastecenter = "WASTE_CENTER";
/** Installation de traitement de VHU (casse automobile et/ou broyeur agréé) */
const wastevehicles = "WASTE_VEHICLES";
/** Entreprise de travaux */
const worker = "WORKER";

export const BSDS_OPTIONS = [
  {
    value: "BSDD",
    label: "Déchets dangereux",
    shortLabel: "Bsdd",
  },
  {
    value: "BSDA",
    label: "Déchets d'amiante",
    shortLabel: "Amiante",
  },
  {
    value: "BSFF",
    label: "Déchets de Fluides Frigorigènes",
    shortLabel: "Fluides frigo",
  },
  {
    value: "BSVHU",
    label: "Véhicules hors d'usage",
    shortLabel: "VHU",
  },
  {
    value: "BSDASRI",
    label: "Déchets d'Activités de Soins à Risques Infectieux",
    shortLabel: "Dasri",
  },
];

export const PROFILE_OPTIONS = [
  {
    value: producer,
    label: "Producteur de déchets, y compris terres et sédiments",
    shortLabel: "Producteur",
  },
  {
    value: intermediary,
    label: "Intermédiaire",
    shortLabel: "Intermédiaire",
  },
  {
    value: collector,
    label:
      "Installation de Tri, transit regroupement de déchets y compris non classée",
    shortLabel: "TTR",

    // subTypes: COLLECTOR_TYPE_OPTIONS,
    subTypesName: "collectorTypes",
  },
  {
    value: wasteprocessor,
    label: "Installation de traitement",
    shortLabel: "Installation de traitement",

    // subTypes: WASTE_PROCESSOR_TYPE_OPTIONS,
    subTypesName: "wasteProcessorTypes",
  },
  {
    value: disposalfacility,
    label: "Installation de valorisation de terres et sédiments",
    shortLabel: "Terres et sédiments",
  },
  {
    value: wastecenter,
    label:
      "Installation de collecte de déchets apportés par le producteur initial (Rubrique 2710)",
    shortLabel: "Installation de collecte",
  },
  {
    value: wastevehicles,
    label: "Installation de traitement de VHU",
    shortLabel: "Vhus",

    // subTypes: WASTE_VEHICLES_TYPE_OPTIONS,
    // subTypesName: "wasteVehiclesTypes",
  },
  {
    value: transporter,
    label: "Transporteur",
    shortLabel: "Transporteur",
  },
  {
    value: trader,
    label: "Négociant",
    shortLabel: "Négociant",
  },
  {
    value: broker,
    label: "Courtier",
    shortLabel: "Courtier",
  },
  {
    value: ecoorganisme,
    label: "Éco-organisme",
    shortLabel: "Éco-organisme",
  },
  {
    value: worker,
    label: "Entreprise de travaux amiante",
    shortLabel: "Travaux amiante",
  },
  {
    value: recoveryfacility,
    label:
      "Installation dans laquelle les déchets perdent leur statut de déchet",
    shortLabel: "Perte statut de déchet",
  },
];

export const PROCESSING_CODES_OPTIONS = [
  {
    value: "R1",
    label:
      "R1 - Utilisation principale comme combustible ou autre moyen de produire de l'énergie",
    shortLabel: "R1",
  },
  {
    value: "R2",
    label: "R2 - Récupération ou régénération des solvants",
    shortLabel: "R2",
  },
  {
    value: "R3",
    label:
      "R3 - Recyclage ou récupération des substances organiques qui ne sont pas utilisées comme solvants (y compris les opérations de compostage et autres transformations biologiques)",
    shortLabel: "R3",
  },
  {
    value: "R4",
    label:
      "R4 - Recyclage ou récupération des métaux et des composés métalliques",
    shortLabel: "R4",
  },
  {
    value: "R5",
    label: "R5 - Recyclage ou récupération d'autres matières inorganiques",
    shortLabel: "R5",
  },
  {
    value: "R6",
    label: "R6 - Régénération des acides ou des bases",
    shortLabel: "R6",
  },
  {
    value: "R7",
    label: "R7 - Récupération des produits servant à capter les polluants",
    shortLabel: "R7",
  },
  {
    value: "R8",
    label: "R8 - Récupération des produits provenant des catalyseurs",
    shortLabel: "R8",
  },
  {
    value: "R9",
    label: "R9 - Régénération ou autres réemplois des huiles",
    shortLabel: "R9",
  },
  {
    value: "R10",
    label:
      "R10 - Épandage sur le sol au profit de l'agriculture ou de l'écologie",
    shortLabel: "R10",
  },
  {
    value: "R11",
    label:
      "R11 - Utilisation de déchets résiduels obtenus à partir de l'une des opérations numérotées R1 à R10",
    shortLabel: "R11",
  },
  {
    value: "R12",
    label:
      "R12 - Échange de déchets en vue de les soumettre à l'une des opérations numérotées R1 à R11",
    shortLabel: "R12",
  },
  {
    value: "R13",
    label:
      "R13 - Stockage de déchets préalablement à l'une des opérations R1 à R12 (à l'exclusion du stockage temporaire, avant collecte, sur le site de production).",
    shortLabel: "R13",
  },
  {
    value: "D1",
    label:
      "D1 - Dépôt sur ou dans le sol (par exemple, mise en décharge, etc …)",
    shortLabel: "D1",
  },
  {
    value: "D2",
    label:
      "D2 - Traitement en milieu terrestre (par exemple, biodégradation de déchets liquides ou de boues dans les sols, etc …)",
    shortLabel: "D2",
  },
  {
    value: "D3",
    label:
      "D3 - Injection en profondeur (par exemple injection des déchets pompables dans des puits, des dômes de sel ou des failles géologiques naturelles, etc …)",
    shortLabel: "D3",
  },
  {
    value: "D4",
    label:
      "D4 - Lagunage (par exemple, déversement de déchets liquides ou de boues dans des puits, des étangs ou des bassins, etc …)",
    shortLabel: "D4",
  },
  {
    value: "D5",
    label:
      "D5 - Mise en décharge spécialement aménagée (par exemple, placement dans des alvéoles étanches séparées, recouvertes et isolées les unes et les autres et de l'environnement, etc …)",
    shortLabel: "D5",
  },
  {
    value: "D6",
    label: "D6 - Rejet dans le milieu aquatique sauf l'immersion",
    shortLabel: "D6",
  },
  {
    value: "D7",
    label: "D7 - Immersion, y compris enfouissement dans le sous-sol marin",
    shortLabel: "D7",
  },
  {
    value: "D8",
    label:
      "D8 - Traitement biologique non spécifié ailleurs dans la présente liste, aboutissant à des composés ou à des mélanges qui sont éliminés selon l'un des procédés numérotés D1 à D12",
    shortLabel: "D8",
  },
  {
    value: "D9",
    label:
      "D9 - Traitement physico-chimique non spécifié ailleurs dans la présente liste, aboutissant à des composés ou à des mélanges qui sont éliminés selon l'un des procédés numérotés D1 à D12 ( par exemple, évaporation, séchage, calcination, etc …)",
    shortLabel: "D9",
  },
  {
    value: "D9F",
    label:
      "D9F - (final) Traitement physico-chimique non spécifié ailleurs dans la présente liste, aboutissant à des composés ou à des mélanges qui sont éliminés selon l'un des procédés numérotés D1 à D12 ( par exemple, évaporation, séchage, calcination, etc …)",
    shortLabel: "D9F",
  },
  {
    value: "D10",
    label: "D10 - Incinération à terre",
    shortLabel: "D10",
  },
  {
    value: "D12",
    label:
      "D12 - Stockage permanent (par exemple, placement de conteneurs dans une mine, etc ...)",
    shortLabel: "D12",
  },
  {
    value: "D13",
    label:
      "D13 - Regroupement préalablement à l'une des opérations numérotées D1 à D12",
    shortLabel: "D13",
  },
  {
    value: "D14",
    label:
      "D14 - Reconditionnement préalablement à l'une des opérations numérotées D1 à D13",
    shortLabel: "D14",
  },
  {
    value: "D15",
    label:
      "D15 - Stockage préalablement à l'une des opérations D1 à D14 (à l'exclusion du stockage temporaire, avant collecte, sur le site de production).",
    shortLabel: "D15",
  },
];
