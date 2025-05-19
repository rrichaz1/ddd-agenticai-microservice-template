# domain/agents/base_agent.py
from abc import ABC, abstractmethod
from infrastructure.prompt_loader import load_prompt
from tools.llm_extraction_tool import LLMExtractionTool
from typing import Any, Dict


class BaseAgent(ABC):
    def __init__(self, prompt_type: str, llm_tool: LLMExtractionTool):
        self.prompt_type = prompt_type
        self.llm_tool = llm_tool

    def load_prompt(self, version: str = "v1") -> str:
        return load_prompt(self.prompt_type, version)

    def call_llm(self, prompt: str, input_text: str) -> Dict[str, Any]:
        result = self.llm_tool.query(prompt=prompt, input=input_text)
        return {
            "text": result.text,
            "usage": result.usage,
            "cost": result.cost
        }

    def run(self, input_text: str, version: str = "v1") -> Dict[str, Any]:
        prompt = self.load_prompt(version)
        return self.call_llm(prompt, input_text)

    @abstractmethod
    def describe(self) -> str:
        """Optional: provide metadata or agent description."""
        pass
