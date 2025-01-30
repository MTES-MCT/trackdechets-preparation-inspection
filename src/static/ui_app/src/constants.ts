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

const CollectorType = {
  /** Déchets Dangereux (Rubrique 2718) */
  DangerousWastes: "DANGEROUS_WASTES",
  /** Déchets DEEE (Rubrique 2711) */
  DeeeWastes: "DEEE_WASTES",
  /** Déchets non Dangereux (Rubriques 2713, 2714, 2715, 2716) */
  NonDangerousWastes: "NON_DANGEROUS_WASTES",
  /** Autres cas déchets dangereux (Rubriques 2719, 2792-1, 2793-1, 2793-2, 2797-1, 2798) */
  OtherDangerousWastes: "OTHER_DANGEROUS_WASTES",
  /** Autres cas déchets non dangereux (Rubrique 2731) */
  OtherNonDangerousWastes: "OTHER_NON_DANGEROUS_WASTES",
};
const WasteProcessorType = {
  /** Crémation */
  Cremation: "CREMATION",
  /** Incinération de déchets dangereux (Rubrique 2770) */
  DangerousWastesIncineration: "DANGEROUS_WASTES_INCINERATION",
  /** Installation de stockage de déchets dangereux (Rubriques 2720-1, 2760-1, 2760-4, 2797-2) */
  DangerousWastesStorage: "DANGEROUS_WASTES_STORAGE",
  /** Installation de stockage de déchets inertes (Rubrique 2760-3) */
  InertWastesStorage: "INERT_WASTES_STORAGE",
  /** Incinération de déchets non dangereux (Rubriques 2771, 2740) */
  NonDangerousWastesIncineration: "NON_DANGEROUS_WASTES_INCINERATION",
  /** Installation de stockage de déchets non dangereux, y compris casiers dédiés amiante, plâtre (Rubriques 2720-2, 2760-2-a, 2760-2-b) */
  NonDangerousWastesStorage: "NON_DANGEROUS_WASTES_STORAGE",
  /** Autres traitements de déchets dangereux (Rubriques 2790, 2792-2, 2793-3) */
  OtherDangerousWastes: "OTHER_DANGEROUS_WASTES",
  /** Autres traitements de déchets non dangereux (Rubriques 2791, 2781, 2782, 2780) */
  OtherNonDangerousWastes: "OTHER_NON_DANGEROUS_WASTES",
};
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
export const COLLECTOR_TYPE_OPTIONS = [
  {
    label: "Déchets non Dangereux (Rubriques 2713, 2714, 2715, 2716)",
    shortLabel: "Déchets non Dangereux",
    value: CollectorType.NonDangerousWastes,
  },
  {
    label: "Déchets Dangereux (Rubrique 2718)",
    value: CollectorType.DangerousWastes,

    shortLabel: "Déchets Dangereux",
  },
  {
    label: "Déchets DEEE (Rubrique 2711)",
    value: CollectorType.DeeeWastes,
    shortLabel: "Déchets DEEE",
  },
  {
    label: "Autres cas déchets non dangereux (Rubrique 2731)",
    value: CollectorType.OtherNonDangerousWastes,
    shortLabel: "Autres déchets non dangereux",
  },
  {
    label:
      "Autres cas déchets dangereux (Rubriques 2719, 2792-1, 2793-1, 2793-2, 2797-1, 2798)",
    value: CollectorType.OtherDangerousWastes,
    shortLabel: "Autres déchets dangereux",
  },
];

export const WASTE_PROCESSOR_TYPE_OPTIONS = [
  {
    label: "Incinération de déchets dangereux (Rubrique 2770)",
    shortLabel: "Incinération dd",
    value: WasteProcessorType.DangerousWastesIncineration,
  },
  {
    label: "Incinération de déchets non dangereux (Rubriques 2771, 2740)",
    shortLabel: "Incinération dnd",
    value: WasteProcessorType.NonDangerousWastesIncineration,
  },
  {
    label: "Crémation",
    shortLabel: "Crémation",
    value: WasteProcessorType.Cremation,
  },
  {
    label:
      "Installation de stockage de déchets dangereux (Rubriques 2720-1, 2760-1, 2760-4, 2797-2)",
    shortLabel: "Stockage dd",
    value: WasteProcessorType.DangerousWastesStorage,
  },
  {
    label:
      "Installation de stockage de déchets non dangereux, y compris casiers dédiés amiante, plâtre (Rubriques 2720-2, 2760-2-a, 2760-2-b)",
    shortLabel: "Stockage dnd",
    value: WasteProcessorType.NonDangerousWastesStorage,
  },
  {
    label: "Installation de stockage de déchets inertes (Rubrique 2760-3)",
    shortLabel: "Stockage inerte",
    value: WasteProcessorType.InertWastesStorage,
  },
  {
    label:
      "Autres traitements de déchets non dangereux (Rubriques 2791, 2781, 2782, 2780)",
    shortLabel: "Autres traitements  dnd",
    value: WasteProcessorType.OtherNonDangerousWastes,
  },
  {
    label:
      "Autres traitements de déchets dangereux (Rubriques 2790, 2792-2, 2793-3)",
    shortLabel: "Autres traitements dd",
    value: WasteProcessorType.OtherDangerousWastes,
  },
];

export const WASTE_VEHICLES_TYPE_OPTIONS = [
  { label: "Broyeur VHU", shortLabel: "Broyeur VHU", value: "Broyeur" },
  {
    label: "Casse automobile / démolisseur",
    shortLabel: "Casse auto",
    value: "Demolisseur",
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

    options: COLLECTOR_TYPE_OPTIONS,
    subTypesName: "collectorTypes",
  },
  {
    value: wasteprocessor,
    label: "Installation de traitement",
    shortLabel: "Installation de traitement",

    options: WASTE_PROCESSOR_TYPE_OPTIONS,

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

    options: WASTE_VEHICLES_TYPE_OPTIONS,
    subTypesName: "wasteVehiclesTypes",
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

export const FRENCH_DEPARTEMENTS = [
  { value: "01", label: "01 - Ain", shortLabel: "Ain" },
  { value: "02", label: "02 - Aisne", shortLabel: "Aisne" },
  { value: "03", label: "03 - Allier", shortLabel: "Allier" },
  {
    value: "04",
    label: "04 - Alpes-de-Haute-Provence",
    shortLabel: "Alpes-de-Haute-Provence",
  },
  { value: "05", label: "05 - Hautes-Alpes", shortLabel: "Hautes-Alpes" },
  { value: "06", label: "06 - Alpes-Maritimes", shortLabel: "Alpes-Maritimes" },
  { value: "07", label: "07 - Ardèche", shortLabel: "Ardèche" },
  { value: "08", label: "08 - Ardennes", shortLabel: "Ardennes" },
  { value: "09", label: "09 - Ariège", shortLabel: "Ariège" },
  { value: "10", label: "10 - Aube", shortLabel: "Aube" },
  { value: "11", label: "11 - Aude", shortLabel: "Aude" },
  { value: "12", label: "12 - Aveyron", shortLabel: "Aveyron" },
  {
    value: "13",
    label: "13 - Bouches-du-Rhône",
    shortLabel: "Bouches-du-Rhône",
  },
  { value: "14", label: "14 - Calvados", shortLabel: "Calvados" },
  { value: "15", label: "15 - Cantal", shortLabel: "Cantal" },
  { value: "16", label: "16 - Charente", shortLabel: "Charente" },
  {
    value: "17",
    label: "17 - Charente-Maritime",
    shortLabel: "Charente-Maritime",
  },
  { value: "18", label: "18 - Cher", shortLabel: "Cher" },
  { value: "19", label: "19 - Corrèze", shortLabel: "Corrèze" },
  { value: "2A", label: "2A - Corse-du-Sud", shortLabel: "Corse-du-Sud" },
  { value: "2B", label: "2B - Haute-Corse", shortLabel: "Haute-Corse" },
  { value: "21", label: "21 - Côte-d'Or", shortLabel: "Côte-d'Or" },
  { value: "22", label: "22 - Côtes-d'Armor", shortLabel: "Côtes-d'Armor" },
  { value: "23", label: "23 - Creuse", shortLabel: "Creuse" },
  { value: "24", label: "24 - Dordogne", shortLabel: "Dordogne" },
  { value: "25", label: "25 - Doubs", shortLabel: "Doubs" },
  { value: "26", label: "26 - Drôme", shortLabel: "Drôme" },
  { value: "27", label: "27 - Eure", shortLabel: "Eure" },
  { value: "28", label: "28 - Eure-et-Loir", shortLabel: "Eure-et-Loir" },
  { value: "29", label: "29 - Finistère", shortLabel: "Finistère" },
  { value: "30", label: "30 - Gard", shortLabel: "Gard" },
  { value: "31", label: "31 - Haute-Garonne", shortLabel: "Haute-Garonne" },
  { value: "32", label: "32 - Gers", shortLabel: "Gers" },
  { value: "33", label: "33 - Gironde", shortLabel: "Gironde" },
  { value: "34", label: "34 - Hérault", shortLabel: "Hérault" },
  { value: "35", label: "35 - Ille-et-Vilaine", shortLabel: "Ille-et-Vilaine" },
  { value: "36", label: "36 - Indre", shortLabel: "Indre" },
  { value: "37", label: "37 - Indre-et-Loire", shortLabel: "Indre-et-Loire" },
  { value: "38", label: "38 - Isère", shortLabel: "Isère" },
  { value: "39", label: "39 - Jura", shortLabel: "Jura" },
  { value: "40", label: "40 - Landes", shortLabel: "Landes" },
  { value: "41", label: "41 - Loir-et-Cher", shortLabel: "Loir-et-Cher" },
  { value: "42", label: "42 - Loire", shortLabel: "Loire" },
  { value: "43", label: "43 - Haute-Loire", shortLabel: "Haute-Loire" },
  {
    value: "44",
    label: "44 - Loire-Atlantique",
    shortLabel: "Loire-Atlantique",
  },
  { value: "45", label: "45 - Loiret", shortLabel: "Loiret" },
  { value: "46", label: "46 - Lot", shortLabel: "Lot" },
  { value: "47", label: "47 - Lot-et-Garonne", shortLabel: "Lot-et-Garonne" },
  { value: "48", label: "48 - Lozère", shortLabel: "Lozère" },
  { value: "49", label: "49 - Maine-et-Loire", shortLabel: "Maine-et-Loire" },
  { value: "50", label: "50 - Manche", shortLabel: "Manche" },
  { value: "51", label: "51 - Marne", shortLabel: "Marne" },
  { value: "52", label: "52 - Haute-Marne", shortLabel: "Haute-Marne" },
  { value: "53", label: "53 - Mayenne", shortLabel: "Mayenne" },
  {
    value: "54",
    label: "54 - Meurthe-et-Moselle",
    shortLabel: "Meurthe-et-Moselle",
  },
  { value: "55", label: "55 - Meuse", shortLabel: "Meuse" },
  { value: "56", label: "56 - Morbihan", shortLabel: "Morbihan" },
  { value: "57", label: "57 - Moselle", shortLabel: "Moselle" },
  { value: "58", label: "58 - Nièvre", shortLabel: "Nièvre" },
  { value: "59", label: "59 - Nord", shortLabel: "Nord" },
  { value: "60", label: "60 - Oise", shortLabel: "Oise" },
  { value: "61", label: "61 - Orne", shortLabel: "Orne" },
  { value: "62", label: "62 - Pas-de-Calais", shortLabel: "Pas-de-Calais" },
  { value: "63", label: "63 - Puy-de-Dôme", shortLabel: "Puy-de-Dôme" },
  {
    value: "64",
    label: "64 - Pyrénées-Atlantiques",
    shortLabel: "Pyrénées-Atlantiques",
  },
  { value: "65", label: "65 - Hautes-Pyrénées", shortLabel: "Hautes-Pyrénées" },
  {
    value: "66",
    label: "66 - Pyrénées-Orientales",
    shortLabel: "Pyrénées-Orientales",
  },
  { value: "67", label: "67 - Bas-Rhin", shortLabel: "Bas-Rhin" },
  { value: "68", label: "68 - Haut-Rhin", shortLabel: "Haut-Rhin" },
  { value: "69", label: "69 - Rhône", shortLabel: "Rhône" },
  { value: "70", label: "70 - Haute-Saône", shortLabel: "Haute-Saône" },
  { value: "71", label: "71 - Saône-et-Loire", shortLabel: "Saône-et-Loire" },
  { value: "72", label: "72 - Sarthe", shortLabel: "Sarthe" },
  { value: "73", label: "73 - Savoie", shortLabel: "Savoie" },
  { value: "74", label: "74 - Haute-Savoie", shortLabel: "Haute-Savoie" },
  { value: "75", label: "75 - Paris", shortLabel: "Paris" },
  { value: "76", label: "76 - Seine-Maritime", shortLabel: "Seine-Maritime" },
  { value: "77", label: "77 - Seine-et-Marne", shortLabel: "Seine-et-Marne" },
  { value: "78", label: "78 - Yvelines", shortLabel: "Yvelines" },
  { value: "79", label: "79 - Deux-Sèvres", shortLabel: "Deux-Sèvres" },
  { value: "80", label: "80 - Somme", shortLabel: "Somme" },
  { value: "81", label: "81 - Tarn", shortLabel: "Tarn" },
  { value: "82", label: "82 - Tarn-et-Garonne", shortLabel: "Tarn-et-Garonne" },
  { value: "83", label: "83 - Var", shortLabel: "Var" },
  { value: "84", label: "84 - Vaucluse", shortLabel: "Vaucluse" },
  { value: "85", label: "85 - Vendée", shortLabel: "Vendée" },
  { value: "86", label: "86 - Vienne", shortLabel: "Vienne" },
  { value: "87", label: "87 - Haute-Vienne", shortLabel: "Haute-Vienne" },
  { value: "88", label: "88 - Vosges", shortLabel: "Vosges" },
  { value: "89", label: "89 - Yonne", shortLabel: "Yonne" },
  {
    value: "90",
    label: "90 - Territoire de Belfort",
    shortLabel: "Territoire de Belfort",
  },
  { value: "91", label: "91 - Essonne", shortLabel: "Essonne" },
  { value: "92", label: "92 - Hauts-de-Seine", shortLabel: "Hauts-de-Seine" },
  {
    value: "93",
    label: "93 - Seine-Saint-Denis",
    shortLabel: "Seine-Saint-Denis",
  },
  { value: "94", label: "94 - Val-de-Marne", shortLabel: "Val-de-Marne" },
  { value: "95", label: "95 - Val-d'Oise", shortLabel: "Val-d'Oise" },
  { value: "971", label: "971 - Guadeloupe", shortLabel: "Guadeloupe" },
  { value: "972", label: "972 - Martinique", shortLabel: "Martinique" },
  { value: "973", label: "973 - Guyane", shortLabel: "Guyane" },
  { value: "974", label: "974 - La Réunion", shortLabel: "La Réunion" },
  { value: "976", label: "976 - Mayotte", shortLabel: "Mayotte" },
];

export const FRENCH_REGIONS = [
  {
    value: "84",
    label: "84 - Auvergne-Rhône-Alpes",
    shortLabel: "Auvergne-Rhône-Alpes",
  },
  {
    value: "27",
    label: "27 - Bourgogne-Franche-Comté",
    shortLabel: "Bourgogne-Franche-Comté",
  },
  { value: "53", label: "53 - Bretagne", shortLabel: "Bretagne" },
  {
    value: "24",
    label: "24 - Centre-Val de Loire",
    shortLabel: "Centre-Val de Loire",
  },
  { value: "94", label: "94 - Corse", shortLabel: "Corse" },
  { value: "44", label: "44 - Grand Est", shortLabel: "Grand Est" },
  { value: "32", label: "32 - Hauts-de-France", shortLabel: "Hauts-de-France" },
  { value: "11", label: "11 - Île-de-France", shortLabel: "Île-de-France" },
  {
    value: "75",
    label: "75 - Nouvelle-Aquitaine",
    shortLabel: "Nouvelle-Aquitaine",
  },
  { value: "76", label: "76 - Occitanie", shortLabel: "Occitanie" },
  {
    value: "52",
    label: "52 - Pays de la Loire",
    shortLabel: "Pays de la Loire",
  },
  {
    value: "93",
    label: "93 - Provence-Alpes-Côte d'Azur",
    shortLabel: "Provence-Alpes-Côte d'Azur",
  },
  { value: "01", label: "01 - Guadeloupe", shortLabel: "Guadeloupe" },
  { value: "02", label: "02 - Martinique", shortLabel: "Martinique" },
  { value: "03", label: "03 - Guyane", shortLabel: "Guyane" },
  { value: "04", label: "04 - La Réunion", shortLabel: "La Réunion" },
  { value: "06", label: "06 - Mayotte", shortLabel: "Mayotte" },
];
