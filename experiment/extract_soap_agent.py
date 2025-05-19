from domain.agents.base_agent import BaseAgent

class SummarizationAgent(BaseAgent):
    def __init__(self, llm_tool):
        super().__init__(prompt_type="summarization", llm_tool=llm_tool)

    def describe(self) -> str:
        return "Agent to summarize extracted clinical note data."
