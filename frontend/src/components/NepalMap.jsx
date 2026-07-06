import { useEffect, useRef, useState } from 'react'
import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet'
import 'leaflet/dist/leaflet.css'
import { getDistricts } from '../services/api'

const NEPAL_CENTER = [28.3949, 84.1240]
const NEPAL_ZOOM = 7

export default function NepalMap({ onDistrictSelect, selectedId }) {
  const [geoData, setGeoData] = useState(null)
  const districtMapRef = useRef({})

  useEffect(() => {
    fetch('/nepal_districts.geojson')
      .then(r => r.json())
      .then(setGeoData)
      .catch(console.error)

    getDistricts().then(res => {
      const map = {}
      res.data.forEach(d => {
        map[d.name.toLowerCase()] = d
      })
      districtMapRef.current = map
      console.log('Districts loaded:', Object.keys(map).length)
    }).catch(console.error)
  }, [])

  const style = () => ({
    fillColor: '#1A6B4A',
    weight: 1,
    opacity: 1,
    color: '#2ECC8A',
    fillOpacity: 0.2,
  })

  const onEachFeature = (feature, layer) => {
    const name = feature.properties.DISTRICT?.toLowerCase()

    layer.on({
     click: () => {
  console.log("========== DISTRICT CLICK ==========");
  console.log("GeoJSON district name:", name);

  const district = districtMapRef.current[name];

  console.log("Matched district object:", district);
  console.log("District ID:", district?.id);

  if (district) {
    onDistrictSelect(district);
  } else {
    console.log("❌ No matching district found!");
  }
},
      mouseover: (e) => e.target.setStyle({ fillOpacity: 0.5 }),
      mouseout: (e) => e.target.setStyle({ fillOpacity: 0.2 })
    })

    layer.bindTooltip(feature.properties.DISTRICT, {
      permanent: false,
      direction: 'center',
    })
  }

  return (
    <MapContainer
      center={NEPAL_CENTER}
      zoom={NEPAL_ZOOM}
      style={{ height: '100%', width: '100%' }}
    >
      <TileLayer
        url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
        attribution='CartoDB'
      />
      {geoData && (
        <GeoJSON
          data={geoData}
          style={style}
          onEachFeature={onEachFeature}
        />
      )}
    </MapContainer>
  )
}
