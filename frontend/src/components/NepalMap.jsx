import { useEffect, useRef, useState } from "react";
import {
  MapContainer,
  TileLayer,
  GeoJSON,
  LayersControl,
} from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { getDistricts } from "../services/api";

const { BaseLayer } = LayersControl;
const NEPAL_CENTER = [28.3949, 84.124];
const NEPAL_ZOOM = 7;

export default function NepalMap({ onDistrictSelect, selectedId }) {
  const [geoData, setGeoData] = useState(null);
  const [districtsLoaded, setDistrictsLoaded] = useState(false);
  const districtMapRef = useRef({});

  useEffect(() => {
    fetch("/nepal_districts.geojson")
      .then((r) => r.json())
      .then(setGeoData);

    getDistricts().then((res) => {
      const map = {};
      res.data.forEach((d) => {
        map[d.name.toLowerCase()] = d;
      });
      districtMapRef.current = map;
      setDistrictsLoaded(true); // trigger re-render after districts loaded
    });
  }, []);

  const style = (feature) => {
    const district =
      districtMapRef.current[feature.properties.DISTRICT?.toLowerCase()];
    const selected = district?.id === selectedId;
    return {
      fillColor: selected ? "#16a34a" : "#34d399",
      weight: selected ? 3 : 1,
      opacity: 1,
      color: selected ? "#14532d" : "#ffffff",
      fillOpacity: selected ? 0.7 : 0.25,
    };
  };

  const onEachFeature = (feature, layer) => {
    const name = feature.properties.DISTRICT?.toLowerCase();

    layer.on({
      click: () => {
        const district = districtMapRef.current[name];
        if (district) onDistrictSelect(district);
      },
      mouseover: (e) => {
        e.target.setStyle({ fillOpacity: 0.55 });
      },
      mouseout: (e) => {
        e.target.setStyle({
          fillOpacity:
            districtMapRef.current[name]?.id === selectedId ? 0.7 : 0.25,
        });
      },
    });

    layer.bindTooltip(feature.properties.DISTRICT);
  };

  return (
    <MapContainer
      center={NEPAL_CENTER}
      zoom={NEPAL_ZOOM}
      className="h-full w-full"
      zoomControl={false}
    >
      <LayersControl position="topright">
        <BaseLayer checked name="🌍 OpenStreetMap">
          <TileLayer
            attribution="OpenStreetMap"
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
        </BaseLayer>
        <BaseLayer name="🌑 Dark">
          <TileLayer
            attribution="Carto"
            url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
          />
        </BaseLayer>
        <BaseLayer name="🛰 Satellite">
          <TileLayer
            attribution="Esri"
            url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
          />
        </BaseLayer>
      </LayersControl>

      {/* Only render GeoJSON after both geoData AND districts API are loaded */}
      {geoData && districtsLoaded && (
        <GeoJSON
          key={selectedId}
          data={geoData}
          style={style}
          onEachFeature={onEachFeature}
        />
      )}
    </MapContainer>
  );
}
