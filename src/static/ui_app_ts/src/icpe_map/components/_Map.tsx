import "maplibre-gl/dist/maplibre-gl.css";
import ReactMapGL, {
  NavigationControl,
  ScaleControl,
  Source,
  Layer,
  Marker,
  MapLayerMouseEvent,
  LineLayerSpecification,
  MapRef,
} from "react-map-gl/maplibre";
import { useCallback, useMemo, useState, useRef, useEffect } from "react";

import { MapGeoJSONFeature } from "maplibre-gl";
import { Plot } from "../../map/types.ts";
import { setPopupData } from "../../map/store/mapPopupSlice.ts";

const MAP_STYLE =
  "https://openmaptiles.geo.data.gouv.fr/styles/osm-bright/style.json";

// Component props types
export interface MapContainerProps {
  mapRef: React.RefObject<MapRef>;
  lat: number;
  lng: number;
}

const adminLayerDepartments: LineLayerSpecification = {
  id: "departements",
  type: "line",
  source: "departements",
  paint: {
    "line-color": "#198EC8",
  },
};
const adminLayerDepartmentsFill: LineLayerSpecification = {
  id: "departements-fill",
  type: "fill",
  source: "departements",
  paint: {
    "fill-color": "transparent",
    "fill-opacity": 0.1,
  },
};

const adminLayerDepartmentsFillHighlight: LineLayerSpecification = {
  id: "departements-fill-highlight",
  type: "fill",
  source: "departements",
  paint: {
    "fill-color": "#ff6b6b",
    "fill-opacity": 0.2,
  },
  filter: ["==", ["get", "nom"], ""], // Initially show nothing
};

const adminLayerRegions: LineLayerSpecification = {
  id: "regions",
  type: "line",
  source: "regions",
  paint: {
    "line-color": "#198EC8",
    "line-width": 1,
  },
};

// Optional: Add a fill layer for better click detection
const adminLayerRegionsFill: LineLayerSpecification = {
  id: "regions-fill",
  type: "fill",
  source: "regions",
  paint: {
    "fill-color": "transparent",
    "fill-opacity": 0.1,
  },
};

const adminLayerRegionsFillHighlight: LineLayerSpecification = {
  id: "regions-fill-highlight",
  type: "fill",
  source: "regions",
  paint: {
    "fill-color": "#ff6b6b",
    "fill-opacity": 0.2,
  },
  filter: ["==", ["get", "nom"], ""], // Initially show nothing
};

const MARKER_BLUE = "#000091";

export default function MapContainer({ mapRef, lat, lng }: MapContainerProps) {
  const [showLoader, setShowLoader] = useState(false);
  const [selectedRegion, setSelectedRegion] = useState<any>(null);

  const loaderTimerRef = useRef<number | null>(null);

  // Update highlight layer filters when selectedRegion changes
  useEffect(() => {
    if (mapRef.current) {
      updateHighlightFilters();
    }
  }, [selectedRegion]);
  const layers = [
    "regions",
    "regions-fill",
    "regions-highlight",
    "regions-fill-highlight",
    "departments",
    "departments-fill",
    "departments-highlight",
    "departements-fill-highlight",
  ];
  const updateHighlightFilters = useCallback(() => {
    if (!mapRef.current) return;

    // Access the underlying MapLibre map instance
    const map = mapRef.current.getMap();

    // Check if the map is loaded and layers exist
    if (map && map.isStyleLoaded()) {
      try {
        const filter = selectedRegion.name
          ? ["==", ["get", "nom"], selectedRegion.name]
          : ["==", ["get", "nom"], ""]; // Empty filter to show nothing

        // Check if layers exist before updating filters
        if (map.getLayer("regions-highlight")) {
          map.setFilter("regions-highlight", filter);
        }
        if (map.getLayer("regions-fill-highlight")) {
          map.setFilter("regions-fill-highlight", filter);
        }
      } catch (error) {
        console.error("Error updating filters:", error);
      }
    }
  }, [selectedRegion]);

  const handleMapClick = useCallback(
    (event: MapLayerMouseEvent) => {
      const { features } = event;
      console.log("Map click event:", event);

      if (!features || features.length === 0) {
        setSelectedRegion(null);

        return;
      }

      const feature: MapGeoJSONFeature = features[0];

      // Check if the clicked feature belongs to the regions layer
      if (layers.includes(feature.layer.id)) {
        console.log("Region clicked:", feature);

        // Extract region information from the feature properties
        const regionInfo = {
          name: feature.properties?.nom || feature.properties?.name,
          code: feature.properties?.code || feature.properties?.code_region,
          properties: feature.properties,
          geometry: feature.geometry,
        };

        setSelectedRegion(regionInfo);

        // You can dispatch to your store here if needed
        // dispatch(setPopupData({
        //   type: 'region',
        //   data: regionInfo,
        //   coordinates: event.lngLat
        // }));

        console.log("Selected region info:", regionInfo);
      } else {
        // Handle other layer clicks or clear selection
        setSelectedRegion(null);
      }
    },
    [mapRef],
  );

  // Optional: Handle hover effects
  const handleMapHover = useCallback(
    (event: MapLayerMouseEvent) => {
      if (mapRef.current) {
        const { features } = event;
        if (features && features.length > 0) {
          const feature = features[0];
          if (layers.includes(feature.id)) {
            mapRef.current.getCanvas().style.cursor = "pointer";
          }
        } else {
          mapRef.current.getCanvas().style.cursor = "";
        }
      }
    },
    [mapRef],
  );

  return (
    <>
      <ReactMapGL
        ref={mapRef}
        initialViewState={{
          longitude: lng,
          latitude: lat,
          zoom: 4,
        }}
        dragRotate={false}
        touchZoomRotate={false}
        mapStyle={MAP_STYLE}
        onLoad={(event) => {
          if (mapRef.current) {
            const mapBounds = event.target.getBounds();
            const sw = mapBounds.getSouthWest();
            const ne = mapBounds.getNorthEast();

            // Ensure filters are applied after map loads
            setTimeout(() => {
              updateHighlightFilters();
            }, 100);
          }
        }}
        onMoveEnd={(event) => {
          // dispatch(setZoom(event.target.getZoom()));
        }}
        // IMPORTANT: Add the layer IDs you want to make interactive
        interactiveLayerIds={layers}
        onClick={handleMapClick}
        onMouseMove={handleMapHover}
      >
        <NavigationControl showCompass={false} />
        <ScaleControl />
        Administrative boundaries
        <Source
          id="departements"
          type="geojson"
          data="/static/geo/departements-avec-outre-mer-light.geojson"
        >
          <Layer {...adminLayerDepartmentsFill} />
          <Layer {...adminLayerDepartments} />

          <Layer {...adminLayerDepartmentsFillHighlight} />
        </Source>
        {/*<Source*/}
        {/*  id="regions"*/}
        {/*  type="geojson"*/}
        {/*  data="/static/geo/regions-avec-outre-mer-light.geojson"*/}
        {/*>*/}
        {/*  /!* Base layers *!/*/}
        {/*  <Layer {...adminLayerRegionsFill} />*/}
        {/*  <Layer {...adminLayerRegions} />*/}
        {/*  /!* Highlight layers - render on top *!/*/}
        {/*  <Layer {...adminLayerDepartmentsFillHighlight} />*/}
        {/*</Source>*/}
        {/* Display selected region info */}
        {selectedRegion && (
          <div
            style={{
              position: "absolute",
              top: 10,
              left: 10,
              background: "white",
              padding: "10px",
              borderRadius: "5px",
              boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
              maxWidth: "300px",
              zIndex: 1000,
            }}
          >
            <h4>Selected Region</h4>
            <p>
              <strong>Name:</strong> {selectedRegion.name}
            </p>
            <p>
              <strong>Code:</strong> {selectedRegion.code}
            </p>
            {/* Add more properties as needed */}
            <button
              onClick={() => {
                setSelectedRegion(null);
              }}
            >
              Close
            </button>
          </div>
        )}
      </ReactMapGL>
    </>
  );
}
