# GitHub Copilot Project Instructions

## 🧱 Overall Architectural Style
Use **Domain-Driven Design (DDD)** and organize code according to:
- `api/` for controllers (FastAPI routers)
- `application/` for application services and use-cases
- `domain/` for entities, value objects, domain events, and repository interfaces
- `infrastructure/` for adapters and external integrations (DB, LLMs, queues, cloud)
- `shared/` for utilities, cross-cutting concerns, exceptions, logging, configuration

This project contains multiple deployable applications (e.g., app1, app2) inside `src/`.

## 📂 Required Python Project Structure

When generating new modules/components, follow this layout:

.
├── copilotinstructions.md  # Instructions for GitHub Copilot
├── pyproject.toml          # Project configuration (dependencies, build)
└── src/
    └── clinical_app/       # Renamed from app_name for clarity
        ├── main.py         # FastAPI application entry point
        │
        ├── api/            # Presentation/API Layer
        │   ├── dependencies.py     # Dependency Injection setup (Factories)
        │   └── v1/
        │       └── clinical/
        │           └── endpoints.py  # Routes for clinical summarization
        │
        ├── application/    # Application Layer
        │   ├── dtos/               # Data Transfer Objects (Pydantic models)
        │   │   └── clinical_dtos.py
        │   └── use_cases/          # Use Cases (Orchestration/Agentic flow)
        │       └── summarize_account.py # The asyncio.gather logic
        │
        ├── domain/         # Domain Layer (The Core)
        │   ├── models/             # Domain Entities/Value Objects
        │   │   ├── note.py
        │   │   └── summary.py
        │   └── ports/              # Interfaces/Ports (ABCs)
        │       ├── llm_port.py     # NoteProcessorAgent (The LLM Contract)
        │       └── repository_port.py # Persistence Contract
        │
        ├── infrastructure/ # Infrastructure Layer (The Adapters/Implementation)
        │   ├── llm/                # LLM Implementations
        │   │   ├── openai_adapter.py  # Contains the asyncio.Semaphore
        │   │   └── azure_adapter.py
        │   └── repositories/       # Persistence Implementations
        │       └── postgres_repo.py  # Mock/Real DB access
        │
        └── shared/         # Shared Utilities
            └── utils/
                └── text_cleaning.py

## 📦 Key Conventions
# Project Instructions for GitHub Copilot

## 1. Project Goal and Architecture
This is a FastAPI project built on **Domain-Driven Design (DDD)** principles, specifically using the **Ports and Adapters** (Hexagonal) pattern.

The core business logic is **Clinical Note Summarization**. The process is "Agentic":
1.  Receive a batch of notes for a single patient account.
2.  Process each note **in parallel** via a rate-limited external LLM API.
3.  Save the intermediate summary of each note.
4.  Aggregate all intermediate summaries into a final report.
5.  Save the final report.

The system must handle external **rate limits** and allow easy **swapping of LLM providers** (e.g., OpenAI, Azure).

## 2. Core Domain Contracts (Ports)

### A. File: `src/clinical_app/domain/models/note.py`
Create Python dataclasses for the core data structures:
* `ClinicalNote`: Must contain `id: str`, `content: str`, `account_id: str`.
* `NoteSummary`: Must contain `note_id: str`, `key_findings: List[str]`, `diagnoses: List[str]`.

### B. File: `src/clinical_app/domain/ports/llm_port.py`
Define the **Agent Contract** using `abc.ABC`. This is the Domain Service interface.
* Class: `NoteProcessorAgent(ABC)`
* Method: `summarize_note(self, note: ClinicalNote) -> NoteSummary`.

### C. File: `src/clinical_app/domain/ports/repository_port.py`
Define the **Persistence Contract** using `abc.ABC`.
* Class: `ArtifactRepository(ABC)`
* Method 1: `save_note_summary(self, summary: NoteSummary) -> None` (for intermediate results).
* Method 2: `save_account_summary(self, account_id: str, final_report: dict) -> None` (for final report).

## 3. Infrastructure Adapters (Implementations)

### A. File: `src/clinical_app/infrastructure/llm/openai_adapter.py`
Implement the `NoteProcessorAgent` interface. **Crucially**, use `asyncio.Semaphore` to manage rate limits for concurrent LLM calls.
* Class: `OpenAINoteProcessor(NoteProcessorAgent)`
* `__init__` must accept `concurrency_limit: int` and initialize `self.semaphore = asyncio.Semaphore(concurrency_limit)`.
* `summarize_note` must use `async with self.semaphore:` to wrap the simulated LLM call. Simulate LLM latency with `await asyncio.sleep(1)`.

### B. File: `src/clinical_app/infrastructure/repositories/postgres_repo.py`
Implement the `ArtifactRepository` interface with placeholder logic for database saving.
* Class: `PostgresArtifactRepository(ArtifactRepository)`
* Methods: `save_note_summary` and `save_account_summary` should print a debug message instead of connecting to a real DB.

## 4. Application Logic (Use Case)

### A. File: `src/clinical_app/application/use_cases/summarize_account.py`
Create the orchestration logic. This is the **main service** for the workflow.
* Class: `AccountSummarizationUseCase`
* `__init__` must inject the two Ports: `agent: NoteProcessorAgent` and `repo: ArtifactRepository`.
* Method: `execute(self, account_id: str, notes: List[ClinicalNote]) -> dict`.
* The `execute` method must:
    1.  Define an inner async function `process_and_save_single_note(note)`.
    2.  Use a list comprehension to create tasks: `tasks = [process_and_save_single_note(note) for note in notes]`.
    3.  Execute tasks with `individual_summaries = await asyncio.gather(*tasks)`.
    4.  Call the repository to save the final aggregated summary.

## 5. API and Dependencies

### A. File: `src/clinical_app/api/dependencies.py`
Write the Dependency Injection setup to wire concrete implementations to interfaces.
* Function `get_repository()`: Returns a `PostgresArtifactRepository` instance.
* Function `get_agent()`: Returns an `OpenAINoteProcessor` instance with a default concurrency limit of `5`.
* Function `get_summarization_use_case()`: Uses `FastAPI.Depends` to inject the repository and agent into `AccountSummarizationUseCase`.

### B. File: `src/clinical_app/application/dtos/clinical_dtos.py`
Create Pydantic models for API input.
* Class: `NoteInput(BaseModel)` (must match `ClinicalNote` fields).
* Class: `AccountSummaryRequest(BaseModel)`: Contains `account_id: str` and `notes: List[NoteInput]`.

### C. File: `src/clinical_app/api/v1/clinical/endpoints.py`
Create the FastAPI router and endpoint.
* Define a POST endpoint `/api/v1/clinical/summaries/accounts`.
* The endpoint function must accept the `AccountSummaryRequest` DTO and the injected `AccountSummarizationUseCase`.
* It should transform the DTO input into Domain Models (`ClinicalNote`) before passing to the use case.
