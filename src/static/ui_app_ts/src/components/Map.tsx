import "maplibre-gl/dist/maplibre-gl.css";
import ReactMapGL, {
    NavigationControl,
    ScaleControl,
    Source,
    Layer,
    Marker, MapLayerMouseEvent, LineLayerSpecification, LayerSpecification
} from "react-map-gl/maplibre";
import {useCallback, useMemo, useState, useRef, useEffect} from "react";
import {MapContainerProps} from "../types.ts";
import {selectZoom, setZoom, setBounds} from "../store/mapUiSlice.ts";
import {closePopup, setPopupData} from "../store/mapPopupSlice";
import {RootState, useAppDispatch, useAppSelector} from "../store/root.ts";
import {Popup} from "./Popup";
import {Loader} from "./Loader.tsx";
import {LocMarker} from "./icons/LocMarker";
import {ZOOM_ETABS, ZOOM_CLUSTERS, ZOOM_DEPARTMENTS} from "../constants/constants.ts";
import {Plot, PopupData} from "../types";
import {Cluster} from "./icons/Cluster.tsx";
import {MapGeoJSONFeature} from "maplibre-gl";
import type {Geometry, FeatureCollection} from 'geojson';


const MAP_STYLE =
    "https://openmaptiles.geo.data.gouv.fr/styles/osm-bright/style.json";

const PREPARE_SLUG = "/sheets/sheet-prepare/";

// Layer styles
const adminLayerDepartments: LineLayerSpecification = {
    id: "departements",
    type: "line",
    source: "departements",
    paint: {
        "line-color": "#198EC8",
    },
};

const adminLayerRegions: LineLayerSpecification = {
    id: "regions",
    type: "line",
    source: "regions",
    paint: {
        "line-color": "#198EC8",
    },
};

const BLUE_LIGHT = "#869ECE";
const BLUE_MEDIUM = "#465F9D";
const BLUE_DARK = "#2F4077";

// Layer styles for clusters
const clusterLayer: LayerSpecification = {
    id: "clusters",
    type: "circle",
    source: "plots",
    filter: ["has", "point_count"],
    paint: {
        "circle-color": [
            "step",
            ["get", "point_count"],
            BLUE_LIGHT, // Color for small clusters
            20, // Threshold
            BLUE_MEDIUM, // Color for medium clusters
            100, // Threshold
            BLUE_DARK, // Color for large clusters
        ],
        "circle-radius": [
            "step",
            ["get", "point_count"],
            20, // Radius for small clusters
            20, // Threshold
            30, // Radius for medium clusters
            100, // Threshold
            40, // Radius for large clusters
        ],
    },
};

const clusterCountLayer: LayerSpecification = {
    id: "cluster-count",
    type: "symbol",
    source: "plots",
    filter: ["has", "point_count"],
    layout: {
        "text-field": "{point_count_abbreviated}",
        "text-font": ["Marianne"],
        "text-size": 12,
    },
    paint: {
        "text-color": "#ffffff",
    },
};

//
const mapPlotToPopup = (plot: Plot, zoom: number): PopupData | null => {
    if (zoom >= ZOOM_ETABS) {
        return {
            popupTitle: plot.nom_etablissement || "",
            popupText: plot.adresse_td || "",
            popupRow1: ["Siret", plot.siret || ""],
            popupRow2: ["Profil", plot.profiles || ""],
            popupRow3: ["Déchet", plot.wastes || ""],
            popupLink: `${PREPARE_SLUG}?siret=${plot.siret || ""}`,
        };
    }
    return null;
};


function hasCoordinates(geometry: Geometry): geometry is GeoJSON.Point | GeoJSON.LineString | GeoJSON.Polygon | GeoJSON.MultiPoint | GeoJSON.MultiLineString | GeoJSON.MultiPolygon {
    return geometry.type !== 'GeometryCollection' && 'coordinates' in geometry;
}

const getFeatures = (plots: Plot[], zoom: number) => {

    if (zoom < ZOOM_DEPARTMENTS) return []
    return plots.map((plot, index) => ({
        type: "Feature",
        properties: {
            id: plot.siret || `marker-${index}`,
            ...plot,
        },
        geometry: {
            type: "Point",
            coordinates: [plot.long, plot.lat],
        },
    }))
}

export default function MapContainer({mapRef, lat, lng}: MapContainerProps) {
    const zoom = useAppSelector(selectZoom);
    const plots = useAppSelector((state: RootState) => state.mapData.plots);
    const loadingStatus = useAppSelector(
        (state: RootState) => state.mapData.status,
    );

    const [showLoader, setShowLoader] = useState(false);
    const loaderTimerRef = useRef<number | null>(null);

    const dispatch = useAppDispatch();

    // Extract popup data from Redux
    const {popupTitle, popupText, popupRow1, popupRow2, popupRow3, popupLink} =
        useAppSelector((state: RootState) => state.mapPopup);

    // Convert plots to GeoJSON format for clustering
    const geojsonData = useMemo(() => {
        return {
            type: "FeatureCollection" as const,
            features: getFeatures(plots, zoom),
        } as FeatureCollection;
    }, [plots]);

    console.log(geojsonData.features.length)

    useEffect(() => {
        if (loadingStatus === "loading") {
            if (loaderTimerRef.current !== null) {
                window.clearTimeout(loaderTimerRef.current);
            }

            loaderTimerRef.current = window.setTimeout(() => {
                setShowLoader(true);
            }, 100);
        } else {
            if (loaderTimerRef.current !== null) {
                window.clearTimeout(loaderTimerRef.current);
                loaderTimerRef.current = null;
            }

            setShowLoader(false);
        }

        return () => {
            if (loaderTimerRef.current !== null) {
                window.clearTimeout(loaderTimerRef.current);
            }
        };
    }, [loadingStatus]);

    // Handle clicks on map layers
    const handleMapClick = useCallback(
        (event: MapLayerMouseEvent) => {
            const {features} = event;
            if (!features || features.length === 0) return;

            const feature: MapGeoJSONFeature = features[0];
            if (hasCoordinates(feature.geometry)) {
                // Inside this block, TypeScript knows that geometry has coordinates
                const coordinates = feature.geometry.coordinates; // No error here

                // Check if it's a cluster
                if (feature.layer.id === "clusters") {
                    const clusterId = feature.properties.cluster_id;
                    const mapboxSource = mapRef.current.getSource("plots");

                    mapboxSource.getClusterExpansionZoom(clusterId, (err: Error, newZoom: number) => {
                        if (err) return;

                        mapRef.current.flyTo({
                            center: coordinates,
                            zoom: newZoom,
                        });
                    });
                }
                // Handle click on single point
                else if (feature.layer.id === "unclustered-point") {
                    const properties = feature.properties;

                    // Create a Plot object from the properties
                    const plot: Plot = {
                        long: coordinates[0] as number,
                        lat: coordinates[1] as number,
                        nom_etablissement: properties.nom_etablissement,
                        adresse_td: properties.adresse_td,
                        siret: properties.siret,
                        profiles: properties.profiles,
                        wastes: properties.wastes,
                        count: 1,
                    };

                    dispatch(setPopupData(mapPlotToPopup(plot, zoom)));
                }
            } else {
                return
            }
        },
        [dispatch, mapRef, zoom],
    );

    const color = "#000091";
    // Generate markers for unclustered points
    const unclusteredMarkers = useMemo(() => {
        // Only render LocMarker components for unclustered points
        // This works alongside the clustered points from the GeoJSON source
        return plots.map((plot, index) => (
            <Marker
                key={`marker-${index}`}
                longitude={plot.long}
                latitude={plot.lat}
                anchor="center"
                onClick={(e) => {
                    e.originalEvent.stopPropagation();
                    dispatch(setPopupData(mapPlotToPopup(plot, zoom)));
                }}
            >
                {zoom < ZOOM_ETABS ? (
                    <Cluster txt={`${plot.count}`} fill={color}/>
                ) : (
                    <LocMarker/>
                )}
            </Marker>
        ));
    }, [plots, zoom, dispatch]);

    return (
        <>
            {showLoader && <Loader/>}
            <ReactMapGL
                ref={mapRef}
                initialViewState={{
                    longitude: lng,
                    latitude: lat,
                    zoom: zoom,
                }}
                dragRotate={false}
                touchZoomRotate={false}
                mapStyle={MAP_STYLE}
                onLoad={(event) => {
                    if (mapRef.current) {
                        dispatch(setBounds(event.target.getBounds()));
                    }
                }}
                onMoveEnd={(event) => {
                    dispatch(setZoom(event.target.getZoom()));
                    dispatch(setBounds(event.target.getBounds()));
                }}
                interactiveLayerIds={["clusters", "unclustered-point"]}
                onClick={handleMapClick}
            >
                <NavigationControl showCompass={false}/>
                <ScaleControl/>

                {/* Clustered data source */}
                {(zoom < ZOOM_ETABS && zoom >=ZOOM_DEPARTMENTS) && (
                <Source
                    id="plots"
                    type="geojson"
                    data={geojsonData}
                    cluster={true}

                    clusterMaxZoom={14}
                    clusterRadius={50}
                >
                    <Layer {...clusterLayer} />
                    <Layer {...clusterCountLayer} />
                </Source>)}
                {(zoom >= ZOOM_ETABS || zoom <= ZOOM_CLUSTERS) && unclusteredMarkers}
                {/* Administrative boundaries */}
                <Source
                    id="departements"
                    type="geojson"
                    data="/static/geo/departements.geojson"
                >
                    <Layer {...adminLayerDepartments}   />
                </Source>

                <Source id="regions" type="geojson" data="/static/geo/regions.geojson">
                    <Layer {...adminLayerRegions}   />
                </Source>

                {/* Popup component */}
                {popupTitle && (
                    <Popup
                        title={popupTitle}
                        text={popupText}
                        row1={[popupRow1[0], popupRow1[1]]}
                        row2={[popupRow2[0], popupRow2[1]]}
                        row3={[popupRow3[0], popupRow3[1]]}

                        link={popupLink}
                        onClose={() => dispatch(closePopup())}
                    />
                )}
            </ReactMapGL>
        </>
    );
}
