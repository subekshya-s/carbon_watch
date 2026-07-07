import { LoaderCircle, Satellite } from "lucide-react";

export default function LoadingOverlay({ loading }) {
  if (!loading) return null;

  return (
    <div className="absolute inset-0 z-[2000] bg-black/40 backdrop-blur-sm flex items-center justify-center">

      <div className="bg-white rounded-3xl shadow-2xl p-8 w-[340px] text-center">

        <Satellite
          className="mx-auto text-emerald-600 mb-4"
          size={42}
        />

        <LoaderCircle
          className="animate-spin mx-auto text-emerald-600"
          size={40}
        />

        <h2 className="mt-6 text-2xl font-bold text-gray-800">
          Analyzing Satellite Data
        </h2>

        <p className="mt-3 text-gray-500 leading-7">
          Connecting to Google Earth Engine...
        </p>

        <div className="mt-6 h-2 rounded-full bg-gray-200 overflow-hidden">
          <div className="h-full w-full bg-emerald-500 animate-pulse"></div>
        </div>

      </div>

    </div>
  );
}