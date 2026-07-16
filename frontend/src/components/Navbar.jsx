import { Leaf, Satellite, Trees, MapPinned } from "lucide-react";

export default function Navbar() {
  return (
    <header className="sticky top-0 z-50 h-16 bg-[#0D2B1E]/95 backdrop-blur-md border-b border-emerald-900/50 shadow-lg">
      <div className="h-full max-w-screen-2xl mx-auto px-6 flex items-center justify-between">

        {/* Logo */}
        <div className="flex items-center gap-3">
          <div className="h-9 w-9 rounded-full bg-emerald-500 flex items-center justify-center shadow-md">
            <Leaf size={18} className="text-white" />
          </div>
          <div>
            <span className="text-white font-bold text-lg tracking-tight">
              Carbon Watch
            </span>
            <span className="hidden sm:inline text-emerald-400 text-xs tracking-widest uppercase ml-3">
              Nepal
            </span>
          </div>
        </div>

        {/* Pills - hidden on small screens */}
        <div className="hidden md:flex items-center gap-3">
          <div className="flex items-center gap-2 rounded-full bg-emerald-900/60 border border-emerald-700/40 px-4 py-1.5 text-emerald-300 text-xs">
            <Satellite size={13} />
            Earth Engine
          </div>
          <div className="flex items-center gap-2 rounded-full bg-emerald-900/60 border border-emerald-700/40 px-4 py-1.5 text-emerald-300 text-xs">
            <Trees size={13} />
            ESA WorldCover
          </div>
          <div className="flex items-center gap-2 rounded-full bg-emerald-900/60 border border-emerald-700/40 px-4 py-1.5 text-emerald-300 text-xs">
            <MapPinned size={13} />
            77 Districts
          </div>
        </div>

        {/* Status indicator */}
        <div className="flex items-center gap-2 text-xs text-emerald-400">
          <div className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></div>
          <span className="hidden sm:inline">Live Satellite Data</span>
        </div>

      </div>
    </header>
  )
}
