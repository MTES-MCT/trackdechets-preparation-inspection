import "maplibre-gl/dist/maplibre-gl.css";
import { useRef } from "react";
import Map, { NavigationControl, ScaleControl } from "react-map-gl/maplibre";
import { useMapStore } from "./Store";
import { Popup } from "./Popup";
import { useShallow } from "zustand/react/shallow";

const MAP_STYLE =
  "https://openmaptiles.geo.data.gouv.fr/styles/osm-bright/style.json";

export default function MapContainer({ mapRef, lat, lng, pins }) {
  const {
    zoom,
    setZoom,
    setBounds,
    popupTitle,
    popupText,
    popupRow1,
    popupRow2,
    popupRow3,
    popupLink,
    closePopup,
  } = useMapStore(
    useShallow((state) => ({
      zoom: state.zoom,

      setZoom: state.setZoom,
      setBounds: state.setBounds,
      popupTitle: state.popupTitle,
      popupText: state.popupText,
      popupRow1: state.popupRow1,
      popupRow2: state.popupRow2,
      popupRow3: state.popupRow3,
      popupLink: state.popupLink,
      closePopup: state.closePopup,
    })),
  );

  return (
    <>
      <Map
        ref={mapRef}
        initialViewState={{
          longitude: lng,
          latitude: lat,
          zoom: zoom,
        }}
        dragRotate={false}
        touchZoomRotate={false}
        mapStyle={MAP_STYLE}
        onMoveEnd={(event) => {
          closePopup();
          setZoom(event.target.getZoom());
          setBounds(event.target.getBounds());
        }}
        onLoad={(event) => {
          if (mapRef) {
            mapRef["current"] = event.target;
            setBounds(event.target.getBounds());
          }
        }}
      >
        <NavigationControl showCompass={false} />
        <ScaleControl />

        {pins}
        {popupTitle && (
          <Popup
            title={popupTitle}
            text={popupText}
            row1={popupRow1}
            row2={popupRow2}
            row3={popupRow3}
            link={popupLink}
            onClose={closePopup}
          />
        )}
      </Map>
    </>
  );
}
