import { createSlice } from "@reduxjs/toolkit";
import {RootState} from "./root.ts";

const initialState = {
  zoom: 5,
  bounds: {},
};

export const mapUiSlice = createSlice({
  name: "mapUi",
  initialState,
  reducers: {
    setZoom: (state, action) => {
      state.zoom = action.payload;
    },
    setBounds: (state, action) => {
      state.bounds = action.payload;
    },
  },
});

export const { setZoom, setBounds } = mapUiSlice.actions;

// Selectors
export const selectZoom = (state:RootState) => state.mapUi.zoom;
export const selectBounds = (state:RootState) => state.mapUi.bounds;

export default mapUiSlice.reducer;
