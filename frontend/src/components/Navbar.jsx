import { Leaf, Trees, Satellite, MapPinned } from "lucide-react";
import forest from "../assets/forest.jpg";

export default function Navbar() {
  return (
    <header className="relative h-[420px] overflow-hidden">

      {/* Background */}
      <img
        src={forest}
        alt="Forest"
        className="absolute inset-0 h-full w-full object-cover scale-105"
      />

      {/* Overlay */}
      <div className="absolute inset-0 bg-gradient-to-b from-black/60 via-black/45 to-[#F5F7F4]"></div>

      {/* Content */}
      <div className="relative z-10 h-full flex flex-col justify-center items-center text-center px-6">

        {/* Logo */}
        <div className="flex items-center gap-4">

          <div className="h-16 w-16 rounded-full bg-emerald-500 flex items-center justify-center shadow-2xl border-4 border-white/20">
            <Leaf size={34} className="text-white" />
          </div>

          <div className="text-left">
            <h1 className="text-6xl font-black tracking-tight text-white">
              Carbon Watch
            </h1>

            <p className="text-emerald-200 tracking-[4px] uppercase text-sm">
              Nepal Forest Carbon Monitoring
            </p>
          </div>

        </div>

        {/* Description */}
        <p className="mt-8 max-w-3xl text-lg leading-8 text-gray-100">
          Monitor forest cover, estimate carbon stock, and analyze land cover
          changes across Nepal using Google Earth Engine and ESA WorldCover.
        </p>

        {/* Feature Pills */}
        <div className="mt-10 flex flex-wrap justify-center gap-5">

          <div className="flex items-center gap-2 rounded-full bg-white/15 backdrop-blur-md border border-white/20 px-6 py-3 text-white shadow-lg">
            <Satellite size={18} />
            Earth Engine
          </div>

          <div className="flex items-center gap-2 rounded-full bg-white/15 backdrop-blur-md border border-white/20 px-6 py-3 text-white shadow-lg">
            <Trees size={18} />
            ESA WorldCover
          </div>

          <div className="flex items-center gap-2 rounded-full bg-white/15 backdrop-blur-md border border-white/20 px-6 py-3 text-white shadow-lg">
            <MapPinned size={18} />
            77 Districts of Nepal
          </div>

        </div>

      </div>
    </header>
  );
}