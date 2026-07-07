import {
  Trees,
  Leaf,
  MapPinned,
  Calendar,
} from "lucide-react";

export default function MapInfoCards({
  district,
  analysis,
}) {
  const carbon =
    analysis?.carbon_estimate?.estimated_carbon_stock || "--";

  const forest =
    analysis?.carbon_estimate?.forest_area_pct || "--";

  return (
    <div className="absolute top-6 left-6 z-[1000] flex gap-4">

      <div className="bg-white/90 backdrop-blur-lg rounded-2xl shadow-xl p-4 w-48">

        <div className="flex items-center gap-3">

          <Leaf className="text-emerald-600" />

          <div>
            <p className="text-xs uppercase text-gray-500">
              Carbon Stock
            </p>

            <h2 className="font-black text-lg">
              {carbon === "--"
                ? "--"
                : Number(carbon).toLocaleString()}
            </h2>

          </div>

        </div>

      </div>

      <div className="bg-white/90 backdrop-blur-lg rounded-2xl shadow-xl p-4 w-40">

        <div className="flex items-center gap-3">

          <Trees className="text-green-700" />

          <div>

            <p className="text-xs uppercase text-gray-500">
              Forest
            </p>

            <h2 className="font-black text-lg">
              {forest}%
            </h2>

          </div>

        </div>

      </div>

      <div className="bg-white/90 backdrop-blur-lg rounded-2xl shadow-xl p-4 w-44">

        <div className="flex items-center gap-3">

          <MapPinned className="text-red-500" />

          <div>

            <p className="text-xs uppercase text-gray-500">
              District
            </p>

            <h2 className="font-black">
              {district?.name || "--"}
            </h2>

          </div>

        </div>

      </div>

      <div className="bg-white/90 backdrop-blur-lg rounded-2xl shadow-xl p-4 w-28">

        <div className="flex items-center gap-3">

          <Calendar className="text-blue-600" />

          <div>

            <p className="text-xs uppercase text-gray-500">
              Years
            </p>

            <h2 className="font-black">
              2020-21
            </h2>

          </div>

        </div>

      </div>

    </div>
  );
}