// Core type definitions

// Map related types
export interface Bounds {
  _sw?: {
    lng: number;
    lat: number;
  };
  _ne?: {
    lng: number;
    lat: number;
  };
}

// Plot/marker data types
export interface Plot {
  lat: number;
  long: number;
  count?: number;
  nom_etablissement?: string;
  adresse_td?: string;
  siret?: string;
  profiles?: string;
  wastes?: string;
}

// Filter types
export interface FilterAction {
  filterKey: string;
  subFilterKey?: string;
  value: string;
}



export interface FilterValue {
  root: string[];
  [key: string]: string[];
}

export type FilterValues = {
  root: string[];
  [key: string]: string[];
};
// Popup related types
export interface PopupData {
  popupTitle?: string;
  popupText?: string;
  popupRow1?: [string, string];
  popupRow2?: [string, string];
  popupRow3?: [string, string];
  popupLink?: string;
}

// Options types
export interface Option {
  value: string;
  label: string;
  shortLabel: string;
  options?: Option[];
  subTypesName?: string;
}

// Store types
export interface MapStoreState {
  // Filter states
  bsdFilters: FilterValue;
  profileFilters: {
    root: string[];
    collectorTypes: string[];
    wasteProcessorTypes: string[];
    wasteVehiclesTypes: string[];
    [key: string]: string[];
  };
  operationCodeFilters: FilterValue;
  departmentFilters: FilterValue;

  // Map data
  regions: any[];
  departments: any[];
  plots: Plot[];

  // Map UI state
  zoom: number;
  bounds: Bounds;

  // Popup state
  popupTitle: string;
  popupText: string;
  popupRow1: [string, string] | null;
  popupRow2: [string, string] | null;
  popupRow3: [string, string] | null;
  popupLink: string;

  // Actions
  addFilter: (filter: FilterAction) => void;
  removeFilter: (filter: FilterAction) => void;
  clearFilter: (
    filter: Pick<FilterAction, "filterKey" | "subFilterKey">,
  ) => void;
  fetchPlots: () => Promise<void>;
  setZoom: (zoom: number) => void;
  setBounds: (bounds: Bounds) => void;
  setPopupData: (data: PopupData) => void;
  closePopup: () => void;
}

// Component props types
export interface MapContainerProps {
  mapRef: React.RefObject<any>;
  lat: number;
  lng: number;
  // pins: React.ReactNode;
}

export interface PopupProps {
  title: string;
  text: string;
  onClose: () => void;
  row1?: [string, string] | null;
  row2?: [string, string] | null;
  row3?: [string, string] | null;
  link?: string | null;
}

export interface SelectWithSubOptionsProps {
  options: Option[];
  filterKey: string;
  subFilterKey?: string;
  selected: FilterValue;
  onAdd: (filter: FilterAction) => void;
  onRemove: (filter: FilterAction) => void;
  onClear?: (filter: Pick<FilterAction, "filterKey" | "subFilterKey">) => void;
}

export interface MapOptionsProps {
  options: Option[];
  filterKey: string;
  subFilterKey?: string;
  parentPaths?: string[];
  ml?: number;
  onAdd: (filter: FilterAction) => void;
  onRemove: (filter: FilterAction) => void;
  selected: FilterValue;
}

export interface SidebarProps {
  mapRef: React.RefObject<any>;
}

export interface FlyToProps {
  mapRef: React.RefObject<any>;
  lat: number;
  long: number;
  label: string;
  zoom?: number;
}

// export interface ClusterProps {
//   txt?: number;
//   fill?: string;
// }

// Constants types
export interface CollectorType {
  DangerousWastes: string;
  DeeeWastes: string;
  NonDangerousWastes: string;
  OtherDangerousWastes: string;
  OtherNonDangerousWastes: string;
}

export interface WasteProcessorType {
  Cremation: string;
  DangerousWastesIncineration: string;
  DangerousWastesStorage: string;
  InertWastesStorage: string;
  NonDangerousWastesIncineration: string;
  NonDangerousWastesStorage: string;
  OtherDangerousWastes: string;
  OtherNonDangerousWastes: string;
}

 
