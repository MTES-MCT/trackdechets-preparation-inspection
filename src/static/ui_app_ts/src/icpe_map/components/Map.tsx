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

import { RootState, useAppSelector } from "../../map/store/root.ts";

const MAP_STYLE =
  "https://openmaptiles.geo.data.gouv.fr/styles/osm-bright/style.json";

// Component props types
export interface MapContainerProps {
  mapRef: React.RefObject<MapRef>;
  lat: number;
  lng: number;
}

// Department layers
const adminLayerDepartments: LineLayerSpecification = {
  id: "departements",
  type: "line",
  source: "departements",
  paint: {
    "line-color": "#198EC8",
    "line-width": 1,
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

// Department highlight layers
const adminLayerDepartmentsHighlight: LineLayerSpecification = {
  id: "departements-highlight",
  type: "line",
  source: "departements",
  paint: {
    "line-color": "#ff6b6b",
    "line-width": 1,
  },
  filter: ["==", ["get", "nom"], ""], // Initially show nothing
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

// Region layers
const adminLayerRegions: LineLayerSpecification = {
  id: "regions",
  type: "line",
  source: "regions",
  paint: {
    "line-color": "#198EC8",
    "line-width": 2,
  },
};

const adminLayerRegionsFill: LineLayerSpecification = {
  id: "regions-fill",
  type: "fill",
  source: "regions",
  paint: {
    "fill-color": "transparent",
    "fill-opacity": 0.1,
  },
};

// Region highlight layers
const adminLayerRegionsHighlight: LineLayerSpecification = {
  id: "regions-highlight",
  type: "line",
  source: "regions",
  paint: {
    "line-color": "#ff6b6b",
    "line-width": 2,
  },
  filter: ["==", ["get", "nom"], ""], // Initially show nothing
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
  const [selectedDepartment, setSelectedDepartment] = useState<any>(null);

  const { adminDivision } = useAppSelector((state: RootState) => state.ui);

  // Update highlight layer filters when selections change
  useEffect(() => {
    if (mapRef.current) {
      updateHighlightFilters();
    }
  }, [selectedRegion, selectedDepartment]);

  const regionLayers = [
    "regions",
    "regions-fill",
    "regions-highlight",
    "regions-fill-highlight",
  ];

  const departmentLayers = [
    "departements",
    "departements-fill",
    "departements-highlight",
    "departements-fill-highlight",
  ];

  const allInteractiveLayers = [...regionLayers, ...departmentLayers];

  const updateHighlightFilters = useCallback(() => {
    if (!mapRef.current) return;

    // Access the underlying MapLibre map instance
    const map = mapRef.current.getMap();

    // Check if the map is loaded and layers exist
    if (map && map.isStyleLoaded()) {
      try {
        // Update region highlight filters
        const regionFilter = selectedRegion?.name
          ? ["==", ["get", "name"], selectedRegion.name]
          : ["==", ["get", "name"], ""]; // Empty filter to show nothing

        if (map.getLayer("regions-highlight")) {
          map.setFilter("regions-highlight", regionFilter);
        }
        if (map.getLayer("regions-fill-highlight")) {
          map.setFilter("regions-fill-highlight", regionFilter);
        }

        // Update department highlight filters
        const departmentFilter = selectedDepartment?.name
          ? ["==", ["get", "name"], selectedDepartment.name]
          : ["==", ["get", "name"], ""]; // Empty filter to show nothing

        if (map.getLayer("departements-highlight")) {
          map.setFilter("departements-highlight", departmentFilter);
        }
        if (map.getLayer("departements-fill-highlight")) {
          map.setFilter("departements-fill-highlight", departmentFilter);
        }
      } catch (error) {
        console.error("Error updating filters:", error);
      }
    }
  }, [selectedRegion, selectedDepartment]);

  const handleMapClick = useCallback((event: MapLayerMouseEvent) => {
    const { features } = event;
    console.log("Map click event:", event);

    if (!features || features.length === 0) {
      setSelectedRegion(null);
      setSelectedDepartment(null);
      return;
    }

    const feature: MapGeoJSONFeature = features[0];

    // Check if the clicked feature belongs to region layers
    if (regionLayers.includes(feature.layer.id)) {
      console.log("Region clicked:", feature);

      const regionInfo = {
        name: feature.properties?.nom || feature.properties?.name,
        code: feature.properties?.code || feature.properties?.code_region,
        properties: feature.properties,
        geometry: feature.geometry,
      };

      setSelectedRegion(regionInfo);
      setSelectedDepartment(null); // Clear department selection

      console.log("Selected region info:", regionInfo);
    }
    // Check if the clicked feature belongs to department layers
    else if (departmentLayers.includes(feature.layer.id)) {
      console.log("Department clicked:", feature);

      const departmentInfo = {
        name: feature.properties?.nom || feature.properties?.name,
        code: feature.properties?.code || feature.properties?.code_departement,
        properties: feature.properties,
        geometry: feature.geometry,
      };

      setSelectedDepartment(departmentInfo);
      setSelectedRegion(null); // Clear region selection

      console.log("Selected department info:", departmentInfo);
    } else {
      // Handle other layer clicks or clear selection
      setSelectedRegion(null);
      setSelectedDepartment(null);
    }
  }, []);

  // Optional: Handle hover effects
  const handleMapHover = useCallback((event: MapLayerMouseEvent) => {
    if (mapRef.current) {
      const { features } = event;
      if (features && features.length > 0) {
        const feature = features[0];
        if (allInteractiveLayers.includes(feature.layer.id)) {
          mapRef.current.getCanvas().style.cursor = "pointer";
        }
      } else {
        mapRef.current.getCanvas().style.cursor = "";
      }
    }
  }, []);

  const selectedItem = selectedRegion || selectedDepartment;
  const selectedType = selectedRegion
    ? "Region"
    : selectedDepartment
      ? "Department"
      : "";

  return (
    <>
      <ReactMapGL
        ref={mapRef}
        initialViewState={{
          longitude: lng,
          latitude: lat,
          zoom: 5,
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
        interactiveLayerIds={allInteractiveLayers}
        onClick={handleMapClick}
        onMouseMove={handleMapHover}
      >
        <NavigationControl showCompass={false} />
        <ScaleControl />

        {/* Administrative boundaries */}
        {adminDivision === "departments" && (
          <Source
            id="departements"
            type="geojson"
            data="/static/geo/departements-avec-outre-mer-light.geojson"
          >
            {/* Base department layers */}
            <Layer {...adminLayerDepartmentsFill} />
            <Layer {...adminLayerDepartments} />

            {/* Department highlight layers - render on top */}
            <Layer {...adminLayerDepartmentsFillHighlight} />
            <Layer {...adminLayerDepartmentsHighlight} />
          </Source>
        )}

        {adminDivision === "regions" && (
          <Source
            id="regions"
            type="geojson"
            data="/static/geo/regions-avec-outre-mer-light.geojson"
          >
            {/* Base region layers */}
            <Layer {...adminLayerRegionsFill} />
            <Layer {...adminLayerRegions} />

            {/* Region highlight layers - render on top */}
            <Layer {...adminLayerRegionsFillHighlight} />
            <Layer {...adminLayerRegionsHighlight} />
          </Source>
        )}

        {/* Display selected region/department info */}
        {selectedItem && (
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
            <h4>Selected {selectedType}</h4>
            <p>
              <strong>Name:</strong> {selectedItem.name}
            </p>
            <p>
              <strong>Code:</strong> {selectedItem.code}
            </p>
            {/* Add more properties as needed */}
            <button
              onClick={() => {
                setSelectedRegion(null);
                setSelectedDepartment(null);
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
