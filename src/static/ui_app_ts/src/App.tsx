import { useEffect, useRef } from "react";
import { Sidebar } from "./components/Sidebar";
import { fetchPlots } from "./store/mapDataSlice";
import { useFetchPlots } from "./store/hooks";
import { Filters } from "./components/filtering/Filter";
import { useAppDispatch } from "./store/root";
import { MapRef } from "./types.ts";

import { lazy, Suspense } from "react";

const MapContainer = lazy(() => import("./components/Map.tsx"));

function App() {
  const dispatch = useAppDispatch();
  const mapRef = useRef<MapRef | null>(null);

  // Use the custom hook to fetch plots when filters change
  useFetchPlots();

  useEffect(() => {
    // Initial fetch of plots
    dispatch(fetchPlots());
  }, [dispatch]);

  // default coords for France
  const lng = 2.209667;
  const lat = 46.232193;

  return (
    <div className="map-app">
      <Filters />
      <Sidebar mapRef={mapRef} />

      <Suspense fallback={<div>Loading...</div>}>
        <MapContainer lat={lat} lng={lng} mapRef={mapRef} />
      </Suspense>
    </div>
  );
}

export default App;
