import { User, Bot, Sparkles } from "lucide-react";

interface Props {
  type: "user" | "bot";
  content: string;
  intent?: string;
  confidence?: number;
}

const ChatMessage = ({ type, content, intent, confidence }: Props) => {
  const isUser = type === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"} mb-6 animate-fade-in group`}>
      <div className={`flex gap-4 max-w-[85%] lg:max-w-[75%] ${isUser ? "flex-row-reverse" : "flex-row"}`}>
        {/* Avatar */}
        <div className={`
          w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 transition-transform duration-300 group-hover:scale-110
          ${isUser
            ? "bg-gradient-to-br from-cyan-400 to-blue-500 shadow-lg shadow-cyan-500/20"
            : "bg-gradient-to-br from-purple-500 to-pink-500 shadow-lg shadow-purple-500/20"
          }
        `}>
          {isUser ? (
            <User className="w-5 h-5 text-white" />
          ) : (
            <Bot className="w-5 h-5 text-white" />
          )}
        </div>

        {/* Message Content */}
        <div className={`
          px-6 py-4 rounded-2xl backdrop-blur-md transition-all duration-300
          ${isUser
            ? "glass-message-user text-cyan-50 rounded-tr-sm"
            : "glass-message-bot text-gray-100 rounded-tl-sm"
          }
        `}>
          <p className="text-[15px] leading-relaxed tracking-wide font-light">{content}</p>

          {/* Intent & Confidence Display */}
          {!isUser && intent && (
            <div className="mt-4 pt-4 border-t border-white/5 space-y-3">
              <div className="flex items-center gap-2">
                <Sparkles className="w-3.5 h-3.5 text-purple-300" />
                <span className="text-[10px] font-bold text-white/40 uppercase tracking-widest">Analysis Result</span>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className="space-y-1">
                   <span className="text-[10px] text-white/40 font-medium">DETECTED INTENT</span>
                   <div className="text-sm font-semibold text-purple-200 bg-purple-500/10 px-2 py-1 rounded border border-purple-500/20 inline-block">
                     {intent}
                   </div>
                </div>

                <div className="space-y-1">
                  <div className="flex items-center justify-between">
                    <span className="text-[10px] text-white/40 font-medium">CONFIDENCE SCORE</span>
                    <span className="text-xs font-bold text-white">{(confidence! * 100).toFixed(0)}%</span>
                  </div>
                  <div className="h-1.5 bg-white/5 rounded-full overflow-hidden w-full">
                    <div
                      className="h-full bg-gradient-to-r from-purple-400 to-pink-400 rounded-full glow-accent"
                      style={{ width: `${confidence! * 100}%` }}
                    />
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ChatMessage;
