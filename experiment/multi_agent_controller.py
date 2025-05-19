# application/orchestration/agent_controller.py

from domain.clinical_note.service import ClinicalNoteService
from adapters.fhir_parser import parse_fhir_payload
from tools.llm_extraction_tool import LLMExtractionTool
from domain.agents.extract_soap_agent import ExtractSOAPAgent
from domain.agents.summarization_agent import SummarizationAgent

class AgentController:
    def __init__(self):
        # Shared services and tools
        self.clinical_note_service = ClinicalNoteService()
        self.llm_tool = LLMExtractionTool()

        # Agents using BaseAgent inheritance
        self.extract_agent = ExtractSOAPAgent(self.llm_tool)
        self.summarization_agent = SummarizationAgent(self.llm_tool)

    def extract_and_summarize_notes(self, fhir_json: dict, prompt_version: str = "v1") -> dict:
        parsed_notes = parse_fhir_payload(fhir_json)
        outputs = []

        for note_type, note_text in parsed_notes.items():
            preprocessed_text = self.clinical_note_service.preprocess(note_text)

            # Step 1: Extract SOAP
            extraction_result = self.extract_agent.run(preprocessed_text, version=prompt_version)

            # Step 2: Summarize
            summary_result = self.summarization_agent.run(extraction_result["text"], version=prompt_version)

            outputs.append({
                "note_type": note_type,
                "summary": summary_result["text"],
                "llm_usage": {
                    "extraction_tokens": extraction_result["usage"],
                    "summarization_tokens": summary_result["usage"],
                    "extraction_cost": extraction_result["cost"],
                    "summarization_cost": summary_result["cost"]
                }
            })

        return {
            "results": outputs,
            "summary_version": prompt_version
        }
