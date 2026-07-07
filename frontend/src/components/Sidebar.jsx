import CarbonCard from "./CarbonCard";
import {
  MapPinned,
  Sparkles,
  ArrowRight,
  LoaderCircle,
} from "lucide-react";

export default function Sidebar({
  district,
  analysis,
  loading,
  onAnalyze,
}) {
  return (
    <div className="space-y-6">

      {/* District Card */}
      <div className="bg-white rounded-3xl shadow-xl border border-gray-200 overflow-hidden">

        <div className="bg-gradient-to-r from-emerald-700 to-green-500 p-6 text-white">

          <div className="flex items-center gap-3">
            <MapPinned size={26} />
            <div>
              <p className="uppercase tracking-widest text-xs opacity-80">
                Selected District
              </p>

              <h2 className="text-3xl font-black mt-1">
                {district ? district.name : "None Selected"}
              </h2>

              {district && (
                <p className="text-emerald-100 mt-1">
                  {district.province}
                </p>
              )}
            </div>
          </div>

        </div>

        <div className="p-6">

          {!district ? (

            <div className="text-center py-10">

              <img
                src="https://cdn-icons-png.flaticon.com/512/684/684908.png"
                alt="Location"
                className="w-16 mx-auto opacity-40"
              />

              <p className="mt-5 text-gray-500 leading-7">
                Click any district on the map to start
                analyzing forest carbon.
              </p>

            </div>

          ) : (

            <button
              onClick={onAnalyze}
              disabled={loading}
              className="w-full bg-emerald-600 hover:bg-emerald-700 transition-all duration-300 rounded-2xl py-4 text-white font-bold text-lg flex justify-center items-center gap-3 shadow-lg hover:shadow-xl"
            >

              {loading ? (
                <>
                  <LoaderCircle className="animate-spin" size={22} />
                  Running Analysis...
                </>
              ) : (
                <>
                  Run Carbon Analysis
                  <ArrowRight size={20} />
                </>
              )}

            </button>

          )}

        </div>

      </div>

      {/* Carbon Card */}
      {analysis && <CarbonCard analysis={analysis} />}

      {/* AI Insights */}
      {analysis?.carbon_estimate?.ai_summary && (

        <div className="bg-white rounded-3xl shadow-xl border border-gray-200 p-6">

          <div className="flex items-center gap-3 mb-5">

            <div className="bg-yellow-100 p-3 rounded-xl">
              <Sparkles className="text-yellow-500" />
            </div>

            <div>
              <h2 className="text-xl font-bold">
                AI Insights
              </h2>

              <p className="text-gray-500 text-sm">
                Automatically generated summary
              </p>
            </div>

          </div>

          <div className="bg-gray-50 rounded-2xl p-5 border border-gray-100">

            <p className="text-gray-700 leading-8">
              {analysis.carbon_estimate.ai_summary}
            </p>

          </div>

        </div>

      )}

    </div>
  );
}