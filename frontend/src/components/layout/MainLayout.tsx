import PixelSnow from "@/components/effects/PixelSnow";
import Sidebar from "./Sidebar";
import Header from "./Header";

const MainLayout = ({ children }: { children: React.ReactNode }) => {
  return (
    <div className="relative min-h-screen bg-gradient-dark text-foreground overflow-hidden font-sans selection:bg-cyan-500/30 selection:text-cyan-100">

      {/* Background Effects */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-cyan-900/20 via-transparent to-transparent opacity-40 pointer-events-none" />
      <div className="absolute bottom-0 left-0 right-0 h-1/3 bg-gradient-to-t from-black to-transparent pointer-events-none" />
      
      <PixelSnow color="#4fd1c5" density={0.6} speed={0.3} />

      <div className="relative z-10 flex h-screen overflow-hidden">
        <Sidebar />
        <div className="flex-1 flex flex-col min-w-0">
          <Header />
          <main className="flex-1 relative overflow-hidden flex flex-col">
              {children}
          </main>
        </div>
      </div>
    </div>
  );
};

export default MainLayout;
