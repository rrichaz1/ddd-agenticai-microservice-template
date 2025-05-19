repo-root/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── api_router.py
│   │   │       └── routes/
│   │   │           ├── patients.py
│   │   │           ├── encounters.py
│   │   │           └── clinical_notes.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── auth.py
│   │   │   └── security.py
│   │   ├── domain/
│   │   │   ├── common/
│   │   │   │   └── note_type.py
│   │   │   ├── patient/
│   │   │   │   ├── models.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── service.py
│   │   │   │   └── repository.py
│   │   │   ├── encounter/
│   │   │   │   ├── models.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── service.py
│   │   │   │   └── repository.py
│   │   │   └── clinical_note/
│   │   │       ├── models.py
│   │   │       ├── schemas.py
│   │   │       ├── service.py
│   │   │       ├── repository.py
│   │   │       ├── llm_interface.py
│   │   │       └── application_service.py
│   │   ├── infrastructure/
│   │   │   ├── azure_openai_client.py
│   │   │   ├── azure_openai_extractor.py
│   │   │   ├── database.py
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
│   │   │   └── fhir_parser.py
│   │   ├── tests/
│   │   │   ├── unit/
│   │   │   │   ├── domain/
│   │   │   │   │   └── test_clinical_note_service.py
│   │   │   └── integration/
│   │   │       └── api/
│   │   │           └── test_clinical_notes.py
│   │   ├── requirements.txt
│   │   └── Dockerfile
├── frontend/
│   ├── react-ui/   # optional frontend in React
│   └── streamlit-app/  # optional frontend in Streamlit
├── .github/
│   └── workflows/
│       └── ci-cd.yml  # GitHub Actions for build/deploy
└── README.md
