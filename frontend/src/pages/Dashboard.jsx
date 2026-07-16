import { useState } from "react";
import Navbar from "../components/Navbar";
import NepalMap from "../components/NepalMap";
import Sidebar from "../components/Sidebar";
import { triggerAnalysis } from "../services/api";
import MapInfoCards from "../components/MapInfoCards";
import MapLegend from "../components/MapLegend";
import LoadingOverlay from "../components/LoadingOverlay";

export default function Dashboard() {
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
    <div className="h-screen flex flex-col overflow-hidden bg-[#0D2B1E]">

      {/* Compact sticky navbar */}
      <Navbar />

      {/* Full height map + sidebar layout */}
      <div className="flex flex-1 overflow-hidden">

        {/* Map — takes all remaining space */}
        <div className="relative flex-1 overflow-hidden">
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

        {/* Sidebar — fixed width, scrollable */}
        <div className="w-[360px] shrink-0 overflow-y-auto bg-white border-l border-gray-200 shadow-xl">
          <Sidebar
            district={selectedDistrict}
            analysis={analysis}
            loading={loading}
            onAnalyze={handleAnalyze}
          />
        </div>

      </div>
    </div>
  );
}