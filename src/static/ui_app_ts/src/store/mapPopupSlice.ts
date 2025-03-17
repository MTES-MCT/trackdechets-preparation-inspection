import { createSlice } from "@reduxjs/toolkit";
import {RootState} from "./root.ts";

const initialState = {
  popupTitle: "",
  popupText: "",
  popupRow1: [],
  popupRow2: [],
  popupRow3: [],
  popupLink: "",
};

export const mapPopupSlice = createSlice({
  name: "mapPopup",
  initialState,
  reducers: {
    setPopupData: (state, action) => {
      const {
        popupTitle,
        popupText,
        popupRow1,
        popupRow2,
        popupRow3,
        popupLink,
      } = action.payload;
      state.popupTitle = popupTitle || "";
      state.popupText = popupText || "";
      state.popupRow1 = popupRow1 || [];
      state.popupRow2 = popupRow2 || [];
      state.popupRow3 = popupRow3 || [];
      state.popupLink = popupLink || "";
    },
    closePopup: (state) => {
      state.popupTitle = "";
      state.popupText = "";
      state.popupRow1 = [];
      state.popupRow2 = [];
      state.popupRow3 = [];
      state.popupLink = "";
    },
  },
});

export const { setPopupData, closePopup } = mapPopupSlice.actions;

export const selectPopupTitle = (state:RootState) => state.mapPopup.popupTitle;
export const selectPopupText = (state:RootState) => state.mapPopup.popupText;
export const selectPopupRow1 = (state:RootState) => state.mapPopup.popupRow1;
export const selectPopupRow2 = (state:RootState) => state.mapPopup.popupRow2;
export const selectPopupRow3 = (state:RootState) => state.mapPopup.popupRow3;
export const selectPopupLink = (state:RootState) => state.mapPopup.popupLink;

export default mapPopupSlice.reducer;
