│   │   │       # agent_controller.py
│   │   │       from domain.clinical_note.service import ClinicalNoteService
│   │   │       from adapters.fhir_parser import parse_fhir_payload
│   │   │       from tools.llm_extraction_tool import LLMExtractionTool
│   │   │       from application.services.note_summarization_service import NoteSummarizationService
│   │   │
│   │   │       class AgentController:
│   │   │           def __init__(self):
│   │   │               self.clinical_note_service = ClinicalNoteService()
│   │   │               self.llm_tool = LLMExtractionTool()
│   │   │               self.summarization_service = NoteSummarizationService()
│   │   │
│   │   │           def extract_and_summarize_notes(self, fhir_json: dict, prompt_version: str = "v1") -> str:
│   │   │               parsed_notes = parse_fhir_payload(fhir_json)
│   │   │               final_outputs = []
│   │   │
│   │   │               for note_type, text in parsed_notes.items():
│   │   │                   preprocessed_text = self.clinical_note_service.preprocess(text)
│   │   │                   extracted = self.llm_tool.extract_soap(note_type, preprocessed_text, prompt_version)
│   │   │                   summary = self.summarization_service.summarize(extracted, note_type)
│   │   │                   final_outputs.append(summary)
│   │   │
│   │   │               return "\n\n".join(final_outputs)






