"""
Intent Classifier Module
Classifies user queries as 'question' or 'action'
based on enterprise workflow intent.
"""

from typing import Literal, Dict
import logging

logger = logging.getLogger(__name__)


class IntentClassifier:
    """
    Classifies user intent into:
    - 'question' → RAG retrieval
    - 'action' → structured enterprise action (JSON)
    """

    def __init__(self):
        # STRICT enterprise action keywords
        self.action_phrases = [
            "create ticket",
            "raise ticket",
            "open ticket",
            "schedule meeting",
            "book meeting",
            "set up meeting",
            "apply leave",
            "request leave",
            "request access",
            "notify hr",
            "escalate issue",
            "assign task",
        ]

    def classify(self, query: str) -> Literal["question", "action"]:
        query_lower = query.lower().strip()

        for phrase in self.action_phrases:
            if phrase in query_lower:
                logger.info(f"Intent classified as ACTION: {phrase}")
                return "action"

        logger.info("Intent classified as QUESTION")
        return "question"

    def classify_with_confidence(self, query: str) -> Dict[str, float]:
        intent = self.classify(query)

        confidence = 0.85 if intent == "action" else 0.9

        return {
            "intent": intent,
            "confidence": confidence
        }
