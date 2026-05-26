import { useState, useRef, useEffect } from "react";
import { analyze } from "@/lib/api";
import ChatInput from "@/components/chat/ChatInput";
import ChatMessage from "@/components/chat/ChatMessage";
import TypingIndicator from "@/components/chat/TypingIndicator";
import { Sparkles, MessageSquare, Zap } from "lucide-react";

interface Message {
  type: "user" | "bot";
  content: string;
  intent?: string;
  confidence?: number;
}

const Chat = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    scrollRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const handleSend = async (text: string) => {
    const userMsg: Message = { type: "user", content: text };
    setMessages((m) => [...m, userMsg]);
    setLoading(true);

    try {
      const res = await analyze({
        message: text,
        model_type: "gemma",
        model_name: "gemma3",
      });

      const botMsg: Message = {
        type: "bot",
        content: res.answer || `Analysis Complete`,
        intent: res.intent,
        confidence: res.confidence || 0.95 // Fallback if api doesn't return confidence
      };
      setMessages((m) => [...m, botMsg]);
    } catch (error) {
      console.error(error);
      setMessages((m) => [
        ...m,
        { type: "bot", content: "⚠️ Error analyzing intent. Please try again." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-full w-full max-w-5xl mx-auto px-4 lg:px-0">
      
      {/* Messages Area */}
      <div className="flex-1 overflow-y-auto py-6 space-y-6 scrollbar-hide">
        {messages.length === 0 && (
          <div className="h-full flex flex-col items-center justify-center space-y-8 animate-fade-in py-10">
            {/* Hero Icon */}
            <div className="relative group">
              <div className="absolute inset-0 bg-gradient-accent opacity-30 blur-3xl rounded-full group-hover:opacity-50 transition-opacity duration-500"></div>
              <div className="relative w-24 h-24 bg-gradient-to-br from-cyan-500/20 to-blue-600/20 rounded-3xl flex items-center justify-center border border-white/10 backdrop-blur-xl shadow-2xl transition-transform duration-500 group-hover:scale-105">
                <Sparkles className="w-10 h-10 text-cyan-300" />
              </div>
            </div>

            {/* Hero Text */}
            <div className="text-center space-y-3 max-w-lg">
              <h3 className="text-3xl font-bold text-white tracking-tight">
                How can I help you today?
              </h3>
              <p className="text-white/50 text-lg leading-relaxed">
                I can analyze intents, extract entities, and process natural language queries.
              </p>
            </div>

            {/* Suggestions Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 w-full max-w-2xl px-2">
              {[
                { icon: MessageSquare, text: "Analyze customer feedback", color: "text-cyan-400" },
                { icon: Zap, text: "Classify support tickets", color: "text-purple-400" },
                { icon: Sparkles, text: "Extract user intent", color: "text-pink-400" },
                { icon: MessageSquare, text: "Summarize conversation", color: "text-blue-400" },
              ].map((suggestion, i) => (
                <button
                  key={i}
                  onClick={() => handleSend(suggestion.text)}
                  className="glass-hover p-4 rounded-xl text-left flex items-center gap-4 group transition-all duration-300 hover:border-cyan-500/30"
                >
                  <div className={`p-2 rounded-lg bg-white/5 ${suggestion.color} group-hover:bg-white/10 transition-colors`}>
                    <suggestion.icon className="w-5 h-5" />
                  </div>
                  <span className="text-sm font-medium text-white/70 group-hover:text-white transition-colors">
                    {suggestion.text}
                  </span>
                </button>
              ))}
            </div>
          </div>
        )}

        {messages.map((m, i) => (
          <ChatMessage key={i} {...m} />
        ))}

        {loading && (
          <div className="flex justify-start animate-fade-in pl-2">
            <TypingIndicator />
          </div>
        )}
        <div ref={scrollRef} />
      </div>

      {/* Input Area - Fixed at bottom of container */}
      <div className="pb-6 pt-2">
        <ChatInput onSend={handleSend} />
      </div>
    </div>
  );
};

export default Chat;
