import { useState } from "react";

const tabs = [
  "Single Query",
  "Batch Testing",
  "Evaluation",
  "Intent Schema",
  "Performance",
  "History",
];

const Header = () => {
  const [activeTab, setActiveTab] = useState("Single Query");

  return (
    <header className="px-8 py-6 z-10 relative">
      <div className="flex items-center justify-between mb-6">
         <h2 className="text-2xl font-bold text-white tracking-tight">
          Intent Analysis
          <span className="text-cyan-400 text-3xl leading-none">.</span>
        </h2>
      </div>

      <div className="flex gap-2 overflow-x-auto pb-2 scrollbar-hide mask-fade-right">
        {tabs.map((tab) => {
          const isActive = activeTab === tab;
          return (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`
                relative px-4 py-2 rounded-full text-sm font-medium whitespace-nowrap
                transition-all duration-300 ease-out border border-transparent
                ${isActive
                  ? 'bg-white/10 text-white border-white/10 shadow-sm'
                  : 'text-white/50 hover:text-white hover:bg-white/5'
                }
              `}
            >
              {tab}
            </button>
          );
        })}
      </div>
    </header>
  );
};

export default Header;
