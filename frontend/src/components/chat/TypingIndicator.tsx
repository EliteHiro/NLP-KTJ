const TypingIndicator = () => {
  return (
    <div className="flex gap-4 mb-6 animate-fade-in">
       <div className="w-9 h-9 rounded-xl bg-gradient-to-br from-purple-500 to-pink-500 shadow-lg shadow-purple-500/20 flex items-center justify-center flex-shrink-0 animate-pulse">
          <div className="w-2 h-2 bg-white rounded-full"></div>
       </div>
       <div className="flex space-x-1.5 p-4 glass-message-bot rounded-2xl rounded-tl-sm w-fit items-center h-full">
        <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce [animation-delay:-0.3s]"></div>
        <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce [animation-delay:-0.15s]"></div>
        <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce"></div>
      </div>
    </div>
  );
};

export default TypingIndicator;
