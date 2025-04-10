import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";
import { FilterValues } from "../types";
import { RootState } from "./root";
import { MapBounds } from "../types";

const baseUrl = "/map/api/companies/objects";
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
  profileFilters,
  roleFilters,
  bsdTypeFilters,
  operationCodeFilters,
  departmentFilters,
  bounds,
  wasteCodesFilter,
}: BuildUrlInput): string => {
  const bsdTypeFilter = bsdTypeFilters?.root[0] ?? null;

  // Handle BSD type and roles filtering combination
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
    params.append("bsds_roles", bsdTypeFilter.toLowerCase());
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
      "profils_installation_vhu",
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

interface ApiResponse {
  companies?: Plot[];
  clusters?: Plot[];
  total_count?: number;
}

export const fetchPlots = createAsyncThunk<
  ApiResponse,
  void,
  {
    state: RootState;
  }
>(
  "mapData/fetchPlots",
  async (_, { getState }: { getState: () => RootState }) => {
    const state = getState();

    const { zoom, bounds } = state.mapUi;

    const {
      profileFilters,
      bsdTypeFilters,
      operationCodeFilters,
      departmentFilters,
      roleFilters,
      wasteCodesFilter,
    } = state.searchFilters;

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

export interface Plot {
  long: number;
  lat: number;
  count?: number;
  nom_etablissement?: string;
  adresse_td?: string;
  siret?: string;
  profiles?: string;
  wastes?: string;

  [key: string]: string | number | undefined;
}

export interface MapDataState {
  plots: Plot[];
  clusters: Plot[];
  totalCount: number;
  status: "idle" | "loading" | "succeeded" | "failed";
  error: string | null;
}

const initialState: MapDataState = {
  plots: [],
  clusters: [],
  totalCount: 0,
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

        state.plots = action.payload.companies ?? [];
        state.clusters = action.payload.clusters ?? [];
        state.totalCount = action.payload.total_count ?? 0;
      })
      .addCase(fetchPlots.rejected, (state, action) => {
        state.status = "failed";
        state.error = action.error.message ?? null;
      });
  },
});

export default mapDataSlice.reducer;
