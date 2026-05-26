import sys
import logging
logging.basicConfig(level=logging.INFO)

try:
    from app.nlp.rag_pipeline import analyze_query
    res = analyze_query("What were the key achievements in 2024?")
    print("SUCCESS")
    print(res)
except Exception as e:
    print(f"FAILED: {e}")
    sys.exit(1)
