import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";
import { FilterValues } from "../types";
import { RootState } from "./root";
import {
  ZOOM_CLUSTERS,
  ZOOM_DEPARTMENTS,
} from "../constants/constants";

const getSlug = (zoom: number): string => {
  if (zoom < ZOOM_DEPARTMENTS) return "/map/api/companies/regions";
  if (zoom < ZOOM_CLUSTERS) return "/map/api/companies/departments";
  return "/map/api/companies/companies";
};

type BuildUrlInput = {
  zoom: number;
  profileFilters: {
    root: string[];
    collectorTypes: string[];
    wasteProcessorTypes: string[];
    wasteVehiclesTypes: string[];
    [key: string]: string[];
  };
  roleFilters: FilterValues; // Made optional since it's not used
  bsdTypeFilters: FilterValues;
  operationCodeFilters: FilterValues;
  departmentFilters: FilterValues;
  wasteCodesFilter: FilterValues;
  bounds: MapBounds;
};

const buildUrl = ({
  zoom,
  profileFilters,
  roleFilters,
  bsdTypeFilters,
  operationCodeFilters,
  departmentFilters,
  bounds,
  wasteCodesFilter,
}: BuildUrlInput): string => {
  const baseUrl = getSlug(zoom);

  const bsdTypeFilter = bsdTypeFilters?.root[0] ?? null;

  // Handle BSD type and roles filter combination
  const bsdRoles =
    bsdTypeFilter && roleFilters.root.length
      ? roleFilters.root
          .map((role) => `${bsdTypeFilter.toLowerCase()}_${role.toLowerCase()}`)
          .join(",")
      : "";

  const params = new URLSearchParams();

  if (bsdRoles) {
    params.append("bsds_roles", bsdRoles);
  } else if (bsdTypeFilter) {
    // Just the BSD type if no roles selected
    params.append("bsd_type", bsdTypeFilter);
  }

  if (profileFilters.root.length) {
    params.append("profils", profileFilters.root.join(","));
  }

  if (profileFilters.collectorTypes.length) {
    params.append(
      "profils_collecteur",
      profileFilters.collectorTypes.join(","),
    );
  }

  if (profileFilters.wasteProcessorTypes.length) {
    params.append(
      "profils_installation",
      profileFilters.wasteProcessorTypes.join(","),
    );
  }

  if (profileFilters.wasteVehiclesTypes.length) {
    params.append(
      "waste_vehicles_types",
      profileFilters.wasteVehiclesTypes.join(","),
    );
  }

  if (departmentFilters.root.length) {
    params.append("departments", departmentFilters.root.join(","));
  }

  if (operationCodeFilters.root.length) {
    params.append("operation_codes", operationCodeFilters.root.join(","));
  }

  if (wasteCodesFilter?.root.length) {
    params.append("waste_codes", wasteCodesFilter.root.join(","));
  }

  // Add map bounds
  if (bounds._sw && bounds._ne) {
    params.append(
      "bounds",
      [bounds._sw.lng, bounds._sw.lat, bounds._ne.lng, bounds._ne.lat].join(
        ",",
      ),
    );
  }

  return `${baseUrl}?${params.toString()}`;
};

export const fetchPlots = createAsyncThunk<
  Plot[],
  void,
  {
    state: RootState;
  }
>(
  "mapData/fetchPlots",
  async (_, { getState }: { getState: () => RootState }) => {
    const state = getState();

    const zoom = state.mapUi.zoom;

    const {
      profileFilters,
      bsdTypeFilters,
      operationCodeFilters,
      departmentFilters,
      roleFilters,
      wasteCodesFilter,
    } = state.searchFilters;
    const bounds = state.mapUi.bounds;

    const url = buildUrl({
      zoom,
      profileFilters,
      bsdTypeFilters,
      operationCodeFilters,
      departmentFilters,
      roleFilters,
      wasteCodesFilter,
      bounds,
    });
    const response = await axios.get(url);

    return response.data;
  },
);

export interface MapBounds {
  _sw?: {
    lng: number;
    lat: number;
  };
  _ne?: {
    lng: number;
    lat: number;
  };

  [key: string]: any;
}

export interface Plot {
  long: number;
  lat: number;
  count?: number;
  nom_etablissement?: string;
  adresse_td?: string;
  siret?: string;
  profiles?: string;
  wastes?: string;

  [key: string]: any;
}

export interface MapDataState {
  regions: any[];
  departments: any[];
  plots: Plot[];
  status: "idle" | "loading" | "succeeded" | "failed";
  error: string | null;
}

const initialState: MapDataState = {
  regions: [],
  departments: [],
  plots: [],
  status: "idle",
  error: null,
};

export const mapDataSlice = createSlice({
  name: "mapData",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchPlots.pending, (state) => {
        state.status = "loading";
      })
      .addCase(fetchPlots.fulfilled, (state, action) => {
        state.status = "succeeded";
        state.plots = action.payload;
      })
      .addCase(fetchPlots.rejected, (state, action) => {
        state.status = "failed";
        state.error = action.error.message ?? null;
      });
  },
});

export const selectPlots = (state: RootState) => state.mapData.plots;
export const selectMapDataStatus = (state: RootState) => state.mapData.status;
export const selectMapDataError = (state: RootState) => state.mapData.error;

export default mapDataSlice.reducer;