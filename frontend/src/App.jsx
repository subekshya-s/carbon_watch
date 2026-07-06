import { useState } from 'react'
import NepalMap from './components/NepalMap'
import Sidebar from './components/Sidebar'
import { triggerAnalysis } from './services/api'
import './index.css'

export default function App() {
  const [selectedDistrict, setSelectedDistrict] = useState(null)
  const [analysis, setAnalysis] = useState(null)
  const [loading, setLoading] = useState(false)

 const handleDistrictSelect = (district) => {
  console.log("========== APP ==========");
  console.log("Selected district:", district);
  console.log("Selected district ID:", district?.id);

  setSelectedDistrict(district);
  setAnalysis(null);
}

  const handleAnalyze = async () => {
    if (!selectedDistrict) return
    setLoading(true)
    setAnalysis(null)
    try {
      const response = await triggerAnalysis(selectedDistrict.id)
      setAnalysis(response.data)
    } catch (error) {
      console.error('Analysis failed:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <nav className="navbar">
        <div className="nav-logo">
          <div className="nav-dot"></div>
          Carbon Watch
        </div>
        <div className="nav-subtitle">Nepal Forest Carbon Monitor · 77 Districts</div>
      </nav>

      <div className="main-layout">
        <div className="map-container">
          <NepalMap
            onDistrictSelect={handleDistrictSelect}
            selectedId={selectedDistrict?.id}
          />
        </div>
        <Sidebar
          district={selectedDistrict}
          analysis={analysis}
          loading={loading}
          onAnalyze={handleAnalyze}
        />
      </div>
    </div>
  )
}
