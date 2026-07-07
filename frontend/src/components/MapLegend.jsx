import {
  Trees,
  Wheat,
  Building2,
  Waves,
} from "lucide-react";

export default function MapLegend() {
  const items = [
    {
      icon: <Trees size={18} className="text-emerald-700" />,
      label: "Forest",
      color: "bg-emerald-500",
    },
    {
      icon: <Wheat size={18} className="text-yellow-600" />,
      label: "Cropland",
      color: "bg-yellow-500",
    },
    {
      icon: <Building2 size={18} className="text-red-600" />,
      label: "Built-up",
      color: "bg-red-500",
    },
    {
      icon: <Waves size={18} className="text-blue-600" />,
      label: "Other",
      color: "bg-blue-500",
    },
  ];

  return (
    <div className="absolute bottom-6 left-6 z-[1000] bg-white/95 backdrop-blur-lg rounded-2xl shadow-xl border border-gray-200 p-5 w-56">

      <h3 className="font-bold text-gray-800 mb-4">
        Land Cover Legend
      </h3>

      <div className="space-y-3">

        {items.map((item) => (
          <div
            key={item.label}
            className="flex items-center justify-between"
          >
            <div className="flex items-center gap-3">
              {item.icon}

              <span className="text-gray-700">
                {item.label}
              </span>
            </div>

            <div
              className={`w-5 h-5 rounded ${item.color}`}
            />
          </div>
        ))}

      </div>

    </div>
  );
}