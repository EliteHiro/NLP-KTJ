import { MessageSquare, FileText, Clock, Settings, Sparkles } from "lucide-react";
import { useState } from "react";

const Sidebar = () => {
  const [activeItem, setActiveItem] = useState("Chat");
  
  const items = [
    { icon: MessageSquare, label: "Chat", badge: null },
    { icon: FileText, label: "Documents", badge: "3" },
    { icon: Clock, label: "History", badge: null },
    { icon: Settings, label: "Settings", badge: null },
  ];

  return (
    <aside className="w-80 flex flex-col gap-8 p-6 z-20 relative">
      {/* Subtle Background for Sidebar */}
      <div className="absolute inset-0 bg-gradient-to-b from-white/5 to-transparent pointer-events-none border-r border-white/5 backdrop-blur-sm" />

      {/* Branding */}
      <div className="relative z-10 px-2">
        <div className="flex items-center gap-3 mb-2">
          <div className="w-10 h-10 bg-gradient-to-tr from-cyan-400 to-blue-500 rounded-xl flex items-center justify-center shadow-lg shadow-cyan-500/20">
            <Sparkles className="w-5 h-5 text-white" />
          </div>
          <h1 className="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-white to-white/70 tracking-tight">
            NLP Model
          </h1>
        </div>
        <p className="text-white/40 text-xs font-medium pl-14 tracking-wider uppercase">
          Intelligence v2.0
        </p>
      </div>

      {/* Navigation */}
      <nav className="flex flex-col gap-1 z-10">
        <p className="text-[10px] font-bold text-white/30 uppercase tracking-widest mb-4 px-4">Menu</p>
        {items.map((item) => {
          const isActive = activeItem === item.label;
          return (
            <button
              key={item.label}
              onClick={() => setActiveItem(item.label)}
              className={`
                group relative flex items-center justify-between px-4 py-3 rounded-xl 
                transition-all duration-300 ease-out
                ${isActive 
                  ? 'bg-white/10 text-white shadow-sm ring-1 ring-white/10' 
                  : 'text-white/60 hover:text-white hover:bg-white/5'
                }
              `}
            >
              <div className="flex items-center gap-3">
                <item.icon 
                  size={18} 
                  className={`transition-colors duration-300 ${isActive ? 'text-cyan-400' : 'group-hover:text-white'}`}
                />
                <span className="font-medium text-sm">{item.label}</span>
              </div>
              
              {item.badge && (
                <span className="px-2 py-0.5 text-[10px] font-bold bg-cyan-500/20 text-cyan-300 rounded-full border border-cyan-500/20">
                  {item.badge}
                </span>
              )}
            </button>
          );
        })}
      </nav>

      {/* Bottom Section */}
      <div className="mt-auto z-10">
        <div className="glass-panel rounded-2xl p-5 relative overflow-hidden group">
          <div className="absolute top-0 right-0 p-4 opacity-50 group-hover:opacity-100 transition-opacity">
            <Sparkles className="w-12 h-12 text-white/5" />
          </div>
          
          <div className="relative z-10">
            <h3 className="text-sm font-bold text-white mb-1">Upgrade Plan</h3>
            <p className="text-xs text-white/50 mb-4 leading-relaxed">
              Get access to advanced models and faster processing.
            </p>
            <button className="w-full py-2.5 px-4 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-400 hover:to-blue-400 text-white text-xs font-bold rounded-lg transition-all duration-300 shadow-lg shadow-cyan-900/20">
              View Options
            </button>
          </div>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
