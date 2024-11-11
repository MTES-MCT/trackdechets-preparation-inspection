import { create } from "zustand";
import { subscribeWithSelector } from "zustand/middleware";
import axios from "axios";
import { shallow } from "zustand/shallow";
import { ZOOM_ETABS, ZOOM_CLUSTERS, ZOOM_DEPARTMENTS } from "./constants";

const getSlug = (zoom) => {
  if (zoom < ZOOM_DEPARTMENTS) return "/map/api/companies/regions";
  if (zoom < ZOOM_CLUSTERS) return "/map/api/companies/departments";
  if (zoom < ZOOM_ETABS) return "/map/api/companies/clusters";
  return "/map/api/companies/companies";
};

const buildUrl = (
  zoom,
  profileFilters,
  bsdFilters,
  operationCodeFilters,
  bounds,
) => {
  const baseUrl = getSlug(zoom);

  const params = new URLSearchParams({
    ...(profileFilters.length ? { profils: profileFilters } : {}),

    ...(bsdFilters.length
      ? { bsds: bsdFilters.map((bsd) => bsd.toLowerCase()).join(",") }
      : {}),
    ...(operationCodeFilters.length
      ? { operationcodes: operationCodeFilters }
      : {}),
    ...(bounds._sw
      ? {
          bounds: [
            bounds._sw.lng,
            bounds._sw.lat,
            bounds._ne.lng,
            bounds._ne.lat,
          ],
        }
      : {}),
  });
  return `${baseUrl}?${params.toString()}`;
};

export const createSearchUiState = (set) => ({
  bsdFilters: [],
  profileFilters: [],
  operationCodeFilters: [],

  addBsdFilter: (bsdType) =>
    set((state) => ({ bsdFilters: [...state.bsdFilters, bsdType] })),

  removeBsdFilter: (bsdType) =>
    set((state) => ({
      bsdFilters: state.bsdFilters.filter((item) => item !== bsdType),
    })),

  addProfileFilter: (profile) =>
    set((state) => ({ profileFilters: [...state.profileFilters, profile] })),
  removeProfileFilter: (profile) =>
    set((state) => ({
      profileFilters: state.profileFilters.filter((item) => item !== profile),
    })),
  addOperationCodeFilter: (operationCode) =>
    set((state) => ({
      operationCodeFilters: [...state.operationCodeFilters, operationCode],
    })),
  removeOperationCodeFilter: (operationCode) =>
    set((state) => ({
      operationCodeFilters: state.operationCodeFilters.filter(
        (item) => item !== operationCode,
      ),
    })),
});

export const createMapDataState = (set, get) => ({
  regions: [],
  departments: [],
  plots: [],
  fetchPlots: async () => {
    const { zoom, profileFilters, bsdFilters, operationCodeFilters, bounds } =
      get();

    const url = buildUrl(
      zoom,
      profileFilters,
      bsdFilters,
      operationCodeFilters,
      bounds,
    );
    axios.get(url).then((res) => {
      set({ plots: res.data });
    });
  },
});

export const createMapUiState = (set) => ({
  zoom: 5,
  bounds: {},

  setZoom: (zoom) => set(() => ({ zoom })),
  setBounds: (bounds) =>
    set(() => {
      return { bounds };
    }),
});

const defaultPopupState = {
  popupTitle: "",
  popupText: "",
  popupRow1: [],
  popupRow2: [],
  popupRow3: [],
};
export const createMapPopupState = (set) => ({
  ...defaultPopupState,
  setPopupData: ({ popupTitle, popupText, popupRow1, popupRow2, popupRow3 }) =>
    set(() => {
      return { popupTitle, popupText, popupRow1, popupRow2, popupRow3 };
    }),
  closePopup: () =>
    set(() => {
      return defaultPopupState;
    }),
});

export const useMapStore = create(
  subscribeWithSelector((...a) => ({
    ...createSearchUiState(...a),
    ...createMapDataState(...a),
    ...createMapUiState(...a),
    ...createMapPopupState(...a),
  })),
);

useMapStore.subscribe(
  (state) => [
    state.bsdFilters,
    state.profileFilters,
    state.operationCodeFilters,
    state.bounds,
  ],

  () => {
    const { fetchPlots } = useMapStore.getState();

    fetchPlots();
  },
  { equalityFn: shallow },
);
