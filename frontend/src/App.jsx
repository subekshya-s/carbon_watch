import { useState } from "react";
import Navbar from "./components/Navbar";
import NepalMap from "./components/NepalMap";
import Sidebar from "./components/Sidebar";
import { triggerAnalysis } from "./services/api";
import MapInfoCards from "./components/MapInfoCards";
import MapLegend from "./components/MapLegend";
import LoadingOverlay from "./components/LoadingOverlay";
export default function App() {
  const [selectedDistrict, setSelectedDistrict] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);

const handleDistrictSelect = (district) => {

  setSelectedDistrict(district);
  setAnalysis(null);
};

  const handleAnalyze = async () => {
    if (!selectedDistrict) return;

    setLoading(true);
    setAnalysis(null);

    try {
      const response = await triggerAnalysis(selectedDistrict.id);
      setAnalysis(response.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

return (
  <div className="min-h-screen bg-[#F5F7F4]">
    <Navbar />

    <main className="max-w-7xl mx-auto px-6 py-8">
      <div className="grid lg:grid-cols-3 gap-8">

        {/* Map */}
        <div className="lg:col-span-2">
          <div className="relative rounded-3xl overflow-hidden shadow-2xl border border-gray-200 h-[700px]">

<MapInfoCards
  district={selectedDistrict}
  analysis={analysis}
/>

<MapLegend />
<LoadingOverlay loading={loading} />

<NepalMap
  onDistrictSelect={handleDistrictSelect}
  selectedId={selectedDistrict?.id}
/>

          </div>
        </div>

        {/* Sidebar */}
        <div>
          <Sidebar
            district={selectedDistrict}
            analysis={analysis}
            loading={loading}
            onAnalyze={handleAnalyze}
          />
        </div>

      </div>
    </main>
  </div>
);
}