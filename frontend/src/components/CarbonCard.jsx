import {
  Trees,
  TrendingUp,
  TrendingDown,
  Leaf,
  Building2,
  Wheat,
  Waves,
} from "lucide-react";

export default function CarbonCard({ analysis }) {
  if (!analysis) return null;

  const carbon = analysis.carbon_estimate;

  const stats = [
    {
      title: "Forest",
      value: carbon.forest_area_pct,
      icon: <Trees size={18} />,
      color: "bg-emerald-500",
    },
    {
      title: "Cropland",
      value: carbon.cropland_area_pct,
      icon: <Wheat size={18} />,
      color: "bg-yellow-500",
    },
    {
      title: "Built-up",
      value: carbon.built_up_area_pct,
      icon: <Building2 size={18} />,
      color: "bg-red-500",
    },
    {
      title: "Other",
      value: carbon.other_area_pct,
      icon: <Waves size={18} />,
      color: "bg-blue-500",
    },
  ];

  return (
    <div className="bg-white rounded-3xl shadow-xl border border-gray-200 overflow-hidden">

      {/* Header */}
      <div className="bg-gradient-to-r from-green-700 to-emerald-500 text-white p-6">

        <div className="flex items-center gap-3">

          <div className="bg-white/20 p-3 rounded-xl">
            <Leaf size={22} />
          </div>

          <div>
            <p className="text-sm uppercase tracking-widest opacity-80">
              Estimated Carbon Stock
            </p>

            <h1 className="text-4xl font-black mt-2">
              {carbon.estimated_carbon_stock.toLocaleString()}
            </h1>

            <p className="text-emerald-100">
              tonnes of Carbon (tC)
            </p>
          </div>

        </div>

      </div>

      {/* Body */}
      <div className="p-6">

        <div
          className={`inline-flex items-center gap-2 px-4 py-2 rounded-full font-semibold mb-6 ${
            carbon.estimated_change >= 0
              ? "bg-emerald-100 text-emerald-700"
              : "bg-red-100 text-red-700"
          }`}
        >
          {carbon.estimated_change >= 0 ? (
            <TrendingUp size={18} />
          ) : (
            <TrendingDown size={18} />
          )}

          {Math.abs(carbon.estimated_change).toLocaleString()} tC
        </div>

        <div className="space-y-5">

          {stats.map((item) => (
            <div key={item.title}>

              <div className="flex justify-between mb-2">

                <div className="flex items-center gap-2 font-semibold">
                  {item.icon}
                  {item.title}
                </div>

                <span className="font-bold">
                  {item.value}%
                </span>

              </div>

              <div className="w-full h-3 rounded-full bg-gray-200 overflow-hidden">

                <div
                  className={`${item.color} h-3 rounded-full transition-all duration-700`}
                  style={{
                    width: `${item.value}%`,
                  }}
                />

              </div>

            </div>
          ))}

        </div>

      </div>

    </div>
  );
}