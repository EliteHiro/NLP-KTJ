from intent_classifier import IntentClassifier

class AgentController:
    def __init__(self, rag_agent, action_agent):
        self.intent = IntentClassifier()
        self.rag = rag_agent
        self.action = action_agent

    def process_query(self, query):
        intent = self.intent.classify(query)
        if intent == "question":
            out = self.rag.answer(query)
        else:
            out = self.action.execute(query)

        out["intent"] = intent
        return out
