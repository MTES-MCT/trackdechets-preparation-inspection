import { useEffect, useRef } from "react";
import "./App.css";
import { Marker } from "react-map-gl/maplibre";
import MapContainer from "./Map";
import { LocMarker } from "./icons/LocMarker";
import { Cluster } from "./icons/Cluster";
import { Sidebar } from "./Sidebar";

import { useShallow } from "zustand/react/shallow";
import { useMapStore } from "./Store";

import { ZOOM_ETABS, ZOOM_DEPARTMENTS, ZOOM_CLUSTERS } from "./constants";

const PREPARE_SLUG = "/sheets/prepare/";
const mapPlotToPopup = (plot, zoom) => {
  if (zoom >= ZOOM_ETABS) {
    return {
      popupTitle: plot.nom_etablissement,
      popupText: plot.adresse_td,
      popupRow1: ["Siret", plot.siret],
      popupRow2: ["Profil", plot.profiles],
      popupRow3: ["Déchet", plot.wastes],
      popupLink: `${PREPARE_SLUG}?siret=${plot.siret}`,
    };
  }
  if (zoom >= ZOOM_CLUSTERS) {
    return {
      popupTitle: `${plot.count} établissements`,
    };
  }
  return {};
};

function App() {
  const mapRef = useRef();
  const { plots, zoom, fetchPlots, setPopupData } = useMapStore(
    useShallow((state) => ({
      plots: state.plots,
      zoom: state.zoom,
      fetchPlots: state.fetchPlots,
      bounds: state.bounds,
      setPopupData: state.setPopupData,
    })),
  );

  useEffect(() => {
    fetchPlots();
  }, []);

  // default coords
  const lng = 2.209667;
  const lat = 46.232193;

  const color =
    zoom < ZOOM_DEPARTMENTS
      ? "#000091"
      : zoom < ZOOM_CLUSTERS
        ? "#666666"
        : zoom < ZOOM_ETABS
          ? "#f95c5e"
          : "#1f8d49";

  const pins = plots.map((plot, index) => (
    <Marker
      key={`marker-${index}`}
      longitude={plot.long}
      latitude={plot.lat}
      anchor="center"
      onClick={(e) => {
        e.originalEvent.stopPropagation();
        if (zoom < ZOOM_CLUSTERS) return;
        setPopupData(mapPlotToPopup(plot, zoom));
      }}
    >
      {zoom < ZOOM_ETABS ? (
        <Cluster txt={plot.count} fill={color} />
      ) : (
        <LocMarker />
      )}
    </Marker>
  ));

  return (
    <div className="map-app">
      <Sidebar mapRef={mapRef} />
      <MapContainer lat={lat} lng={lng} pins={pins} mapRef={mapRef} />
    </div>
  );
}

export default App;
