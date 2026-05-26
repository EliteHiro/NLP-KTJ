import { useState } from "react";
import { analyze } from "@/lib/api";
import MainLayout from "@/components/layout/MainLayout";
import ChatMessage from "@/components/chat/ChatMessage";
import ChatInput from "@/components/chat/ChatInput";
import { Sparkles } from "lucide-react";

const Index = () => {
  const [messages, setMessages] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async (text: string) => {
    if (!text.trim()) return;

    setMessages((m) => [...m, { type: "user", content: text }]);
    setLoading(true);

    const res = await analyze({
      message: text,
      model_type: "gemma",
      model_name: "gemma3",
    });

    setMessages((m) => [
      ...m,
      { type: "bot", content: res.intent },
    ]);

    setLoading(false);
  };

  return (
    <MainLayout>
      <div className="flex h-full flex-col">

        {/* Hero */}
        {messages.length === 0 && (
          <div className="flex-1 flex flex-col items-center justify-center text-center">

            <div className="mb-6 flex h-12 w-12 items-center justify-center
              rounded-2xl bg-gradient-to-br from-cyan-500 to-blue-600">
              <Sparkles className="h-6 w-6 text-black" />
            </div>

            <h2 className="text-3xl font-semibold mb-3">
              NLP Intent Analysis
            </h2>

            <p className="text-white/60 max-w-md mb-8">
              Analyze intent and extract insights from natural language
            </p>

            <div className="grid grid-cols-2 gap-4 max-w-lg w-full">
              {[
                "Analyze customer feedback",
                "Classify user queries",
                "Extract intent patterns",
                "Process natural language",
              ].map((item) => (
                <div key={item} className="glass-card rounded-xl px-4 py-3 text-sm">
                  {item}
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Messages */}
        <div className="flex-1 overflow-y-auto">
          {messages.map((m, i) => (
            <ChatMessage key={i} {...m} />
          ))}
          {loading && <p className="text-white/40">Thinking…</p>}
        </div>

        <ChatInput onSend={sendMessage} />
      </div>
    </MainLayout>
  );
};

export default Index;
