repo-root/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── v1/
│   │   │       ├── __init__.py
│   │   │       └── routes/
│   │   │           ├── __init__.py
│   │   │           ├── patients.py
│   │   │           ├── encounters.py
│   │   │           └── clinical_notes.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   │   ├── auth.py
│   │   │   └── security.py
│   │   ├── domain/
│   │   │   ├── __init__.py
│   │   │   ├── common/
│   │   │   │   ├── __init__.py
│   │   │   │   └── note_type.py
│   │   │   ├── patient/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── models.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── service.py
│   │   │   │   └── repository.py
│   │   │   ├── encounter/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── models.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── service.py
│   │   │   │   └── repository.py
│   │   │   ├── clinical_note/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── models.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── service.py
│   │   │   │   ├── repository.py
│   │   │   │   ├── llm_interface.py
│   │   │   │   └── agent_tools.py
│   │   │   └── agents/
│   │   │       ├── __init__.py
│   │   │       ├── base_agent.py
│   │   │       ├── extract_soap_agent.py
│   │   │       └── summarization_agent.py
│   │   ├── application/
│   │   │   ├── __init__.py
│   │   │   ├── services/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── clinical_note_extraction_service.py
│   │   │   │   └── note_summarization_service.py
│   │   │   └── orchestrators/
│   │   │       ├── __init__.py
│   │   │       └── agent_controller.py
│   │   ├── infrastructure/
│   │   │   ├── __init__.py
│   │   │   ├── azure_openai_client.py
│   │   │   ├── azure_openai_extractor.py
│   │   │   ├── database.py
│   │   │   ├── key_vault.py
│   │   │   ├── storage_client.py
│   │   │   ├── prompt_loader.py
│   │   │   ├── preprocessing.py
│   │   │   └── prompts/
│   │   │       ├── v1/
│   │   │       │   ├── handp.txt
│   │   │       │   ├── ed.txt
│   │   │       │   └── progress.txt
│   │   │       ├── v2/
│   │   │       │   ├── handp.txt
│   │   │       │   ├── ed.txt
│   │   │       │   └── progress.txt
│   │   │       └── prompt_manifest.yaml
│   │   ├── adapters/
│   │   │   ├── __init__.py
│   │   │   └── fhir_parser.py
│   │   ├── tools/
│   │   │   ├── __init__.py
│   │   │   ├── fhir_extraction_tool.py
│   │   │   └── llm_extraction_tool.py
│   │   ├── evaluation/
│   │   │   ├── __init__.py
│   │   │   ├── eval_runner.py
│   │   │   ├── eval_dataset_loader.py
│   │   │   └── metrics/
│   │   │       ├── __init__.py
│   │   │       ├── accuracy.py
│   │   │       ├── cost.py
│   │   │       └── token_usage.py
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── unit/
│   │   │   │   ├── __init__.py
│   │   │   │   └── domain/
│   │   │   │       └── test_clinical_note_service.py
│   │   │   └── integration/
│   │   │       ├── __init__.py
│   │   │       └── api/
│   │   │           └── test_clinical_notes.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
├── frontend/
│   ├── react-ui/
│   └── streamlit-app/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── eval_config.yaml
└── README.md
