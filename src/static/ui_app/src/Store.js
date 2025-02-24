import { create } from "zustand";
import { immer } from "zustand/middleware/immer";
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
  departmentFilters,
  bounds,
) => {
  const baseUrl = getSlug(zoom);

  const params = new URLSearchParams({
    ...(profileFilters.root.length ? { profils: profileFilters.root } : {}),
    ...(profileFilters.collectorTypes.length
      ? { profils_collecteur: profileFilters.collectorTypes }
      : {}),
    ...(profileFilters.wasteProcessorTypes.length
      ? { profils_installation: profileFilters.wasteProcessorTypes }
      : {}),
    ...(bsdFilters.root.length
      ? { bsds: bsdFilters.root.map((bsd) => bsd.toLowerCase()).join(",") }
      : {}),
    ...(operationCodeFilters.root.length
      ? { operationcodes: operationCodeFilters.root }
      : {}),
    ...(departmentFilters.root.length
      ? { departments: departmentFilters.root }
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

// const availableFilterKeys = [
//   "bsdFilters",
//   "profileFilters",
//   "collectorFilters",
//   "operationCodeFilters",
//
//   "departmentFilters",
// ];
export const createSearchUiState = immer((set) => ({
  bsdFilters: { root: [] },
  profileFilters: {
    root: [],
    collectorTypes: [],
    wasteProcessorTypes: [],
    wasteVehiclesTypes: [],
  },

  operationCodeFilters: { root: [] },

  departmentFilters: { root: [] },

  searchType: 1,
  bsdWasteType: 1,
  bsdWasteRole: 1,

  addFilter: ({ filterKey, subFilterKey = "root", value }) =>
    set((state) => {
      state[filterKey][subFilterKey].push(value);
    }),

  removeFilter: ({ filterKey, subFilterKey = "root", value }) =>
    set((state) => {
      const arr = state[filterKey][subFilterKey];
      const index = arr.findIndex((el) => el === value);
      if (index !== -1) arr.splice(index, 1);
    }),

  clearFilter: ({ filterKey, subFilterKey = "root" }) =>
    set((state) => {
      state[filterKey][subFilterKey] = [];
    }),
}));

export const createMapDataState = (set, get) => ({
  regions: [],
  departments: [],
  plots: [],
  fetchPlots: async () => {
    const {
      zoom,
      profileFilters,

      bsdFilters,
      operationCodeFilters,
      departmentFilters,
      bounds,
    } = get();

    const url = buildUrl(
      zoom,
      profileFilters,

      bsdFilters,
      operationCodeFilters,
      departmentFilters,
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
  popupLink: "",
};
export const createMapPopupState = (set) => ({
  ...defaultPopupState,
  setPopupData: ({
    popupTitle,
    popupText,
    popupRow1,
    popupRow2,
    popupRow3,
    popupLink,
  }) =>
    set(() => {
      return {
        popupTitle,
        popupText,
        popupRow1,
        popupRow2,
        popupRow3,
        popupLink,
      };
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
    state.departmentFilters,
    state.bounds,
  ],

  () => {
    const { fetchPlots, closePopup } = useMapStore.getState();

    closePopup();
    fetchPlots();
  },
  { equalityFn: shallow },
);
