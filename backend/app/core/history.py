from datetime import datetime

_history = []

def add_history(text, model, intent, confidence):
    _history.append({
        "timestamp": datetime.utcnow().isoformat(),
        "input": text,
        "model": model,
        "intent": intent,
        "confidence": confidence
    })

def get_history():
    return _history

def clear_history():
    _history.clear()
