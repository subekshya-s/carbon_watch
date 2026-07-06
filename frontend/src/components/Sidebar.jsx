export default function Sidebar({ district, analysis, loading, onAnalyze }) {
  return (
    <div className="sidebar">
      <div className="sidebar-header">
        <h2>Carbon Watch</h2>
        <p>Select a district to analyze</p>
      </div>

      <div className="sidebar-content">
        {!district && (
          <div className="empty-state">
            <p>Click on any district on the map to select it and trigger a carbon analysis.</p>
          </div>
        )}

        {district && (
          <>
            <div className="district-info">
              <div className="district-name">{district.name}</div>
              <div className="district-province">{district.province}</div>
            </div>

            <button
              className="btn-analyze"
              onClick={onAnalyze}
              disabled={loading}
            >
              {loading ? 'Analyzing...' : '⚡ Analyze Carbon'}
            </button>

            {loading && (
              <div className="loading">
                <div className="spinner"></div>
                Fetching satellite data...
              </div>
            )}

            {analysis && !loading && (
              <div className="results-section">
                <div className="results-title">Analysis Results · 2020 → 2021</div>

                <div className="carbon-stock">
                  <div className="carbon-label">Estimated Carbon Stock</div>
                  <div className="carbon-value">
                    {analysis.carbon_estimate.estimated_carbon_stock.toLocaleString()}
                    <span className="carbon-unit"> tC</span>
                  </div>
                  <div className={`carbon-change ${analysis.carbon_estimate.estimated_change < 0 ? 'loss' : 'gain'}`}>
                    {analysis.carbon_estimate.estimated_change < 0 ? '▼' : '▲'} {Math.abs(analysis.carbon_estimate.estimated_change).toLocaleString()} tC change
                  </div>
                </div>

                <div className="landcover-grid">
                  {[
                    { label: 'Forest', value: analysis.carbon_estimate.forest_area_pct, color: '#2ECC8A' },
                    { label: 'Cropland', value: analysis.carbon_estimate.cropland_area_pct, color: '#E8A020' },
                    { label: 'Built-up', value: analysis.carbon_estimate.built_up_area_pct, color: '#E05252' },
                    { label: 'Other', value: analysis.carbon_estimate.other_area_pct, color: '#B8B0A4' },
                  ].map(item => (
                    <div className="landcover-item" key={item.label}>
                      <div className="landcover-header">
                        <span>{item.label}</span>
                        <span className="landcover-pct">{item.value}%</span>
                      </div>
                      <div className="landcover-bar">
                        <div
                          className="landcover-fill"
                          style={{ width: `${item.value}%`, background: item.color }}
                        />
                      </div>
                    </div>
                  ))}
                </div>

                {analysis.carbon_estimate.ai_summary && (
                  <div className="ai-summary">
                    <div className="ai-label">🤖 AI Summary</div>
                    <div className="ai-text">{analysis.carbon_estimate.ai_summary}</div>
                  </div>
                )}
              </div>
            )}
          </>
        )}
      </div>
    </div>
  )
}
