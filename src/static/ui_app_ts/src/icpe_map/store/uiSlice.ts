import { createSlice, PayloadAction } from "@reduxjs/toolkit";

interface UiState {
  adminDivision: string;
  displayPlots: boolean;
}

const initialState: UiState = {
  adminDivision: "regions",
  displayPlots: false,
};

export const uiSlice = createSlice({
  name: "ui",
  initialState,
  reducers: {
    setAdminDivision: (state, action: PayloadAction<string>) => {
      state.adminDivision = action.payload;
    },
    toggleDisplayPlots: (state, action: PayloadAction<boolean>) => {
      state.displayPlots = action.payload;
    },
  },
});

export const { setAdminDivision, toggleDisplayPlots } = uiSlice.actions;

export default uiSlice.reducer;
