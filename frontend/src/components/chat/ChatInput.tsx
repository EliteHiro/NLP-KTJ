import { useState } from "react";
import { Send, Sparkles } from "lucide-react";

interface Props {
  onSend: (text: string) => void;
}

const ChatInput = ({ onSend }: Props) => {
  const [value, setValue] = useState("");
  const [isFocused, setIsFocused] = useState(false);

  const submit = () => {
    if (!value.trim()) return;
    onSend(value);
    setValue("");
  };

  return (
    <div className="p-6">
      <div className={`
        flex gap-3 p-2 rounded-2xl transition-all duration-300 glass-input
        ${isFocused
          ? 'ring-1 ring-cyan-500/40 shadow-lg shadow-cyan-900/20'
          : 'hover:bg-white/5'
        }
      `}>
        <div className="flex items-center pl-3">
          <Sparkles className={`w-5 h-5 transition-colors duration-300 ${isFocused ? 'text-cyan-400' : 'text-white/30'}`} />
        </div>

        <input
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && submit()}
          onFocus={() => setIsFocused(true)}
          onBlur={() => setIsFocused(false)}
          placeholder="Ask me anything..."
          className="flex-1 bg-transparent border-none outline-none text-white placeholder:text-white/30 py-3 text-[15px]"
        />

        <button
          onClick={submit}
          disabled={!value.trim()}
          className={`
            px-5 py-2.5 rounded-xl font-semibold flex items-center gap-2
            transition-all duration-300 ease-out
            ${value.trim()
              ? 'bg-gradient-primary text-white shadow-lg hover:shadow-cyan-500/25 hover:-translate-y-0.5'
              : 'bg-white/5 text-white/20 cursor-not-allowed'
            }
          `}
        >
          <span className="text-sm">Send</span>
          <Send className="w-3.5 h-3.5" />
        </button>
      </div>

      {/* Helper Text */}
      <div className="flex items-center justify-between mt-3 px-4 opacity-0 transition-opacity duration-300 group-hover:opacity-100 hover:opacity-100">
        <p className="text-[10px] text-white/30 tracking-wide uppercase font-medium">
          Powered by RAG
        </p>
        <p className="text-[10px] text-white/30 font-mono">
          {value.length} chars
        </p>
      </div>
    </div>
  );
};

export default ChatInput;
