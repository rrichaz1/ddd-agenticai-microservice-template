repo-root/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── api_router.py
│   │   │       └── routes/
│   │   │           └── clinical_notes.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── auth.py
│   │   │   └── security.py
│   │   ├── domain/
│   │   │   ├── clinical_note/
│   │   │   │   ├── models.py
│   │   │   │   ├── schemas.py
│   │   │   │   └── value_objects.py
│   │   │   └── services/
│   │   │       └── clinical_note_service.py
│   │   ├── application/
│   │   │   ├── orchestrators/
│   │   │   │   └── clinical_note_orchestrator.py
│   │   │   ├── agents/
│   │   │   │   ├── base_agent.py
│   │   │   │   ├── extract_soap_agent.py
│   │   │   │   └── summarization_agent.py
│   │   │   └── dtos/
│   │   │       └── note_result_dto.py
│   │   ├── infrastructure/
│   │   │   ├── llm/
│   │   │   │   ├── openai_client.py
│   │   │   │   └── prompt_loader.py
│   │   │   ├── storage/
│   │   │   │   └── blob_uploader.py
│   │   │   ├── secrets/
│   │   │   │   └── keyvault_client.py
│   │   │   └── prompts/
│   │   │       ├── v1/
│   │   │       │   ├── handp.txt
│   │   │       │   ├── ed.txt
│   │   │       │   └── progress.txt
│   │   │       └── prompt_manifest.yaml
│   │   ├── adapters/
│   │   │   └── fhir_parser.py
│   │   ├── tools/
│   │   │   └── text_preprocessor.py
│   │   ├── tests/
│   │   │   ├── unit/
│   │   │   └── integration/
│   │   ├── requirements.txt
│   │   └── Dockerfile
├── frontend/
│   ├── react-ui/
│   └── streamlit-app/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
└── README.md
