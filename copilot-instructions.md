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


src/
app_name/
api/
v1/
endpoints.py
application/
services.py
dto.py
domain/
models.py
events.py
repositories.py
infrastructure/
repositories/
llm/
persistence/
main.py
shared/
core/
llm/
utils/
streamlit/
app1_ui.py
app2_ui.py
tests/
evaluation/

markdown
Copy code

## 📦 Key Conventions

### 1. Use `src/` root imports:
- Generate imports using **absolute imports**, not relative (`from app1.domain.models import Encounter`).

### 2. LLM Integration
- All LLM clients must be created in `infrastructure/llm/`.
- Use a factory pattern (`shared.llm.factory`) to choose models.
- Domain and application layers must never import OpenAI, Azure, or API SDKs.

### 3. FastAPI Layer (Controllers)
- Always create routers under `app_name/api/v1/`.
- Only handle request/response and dependency injection.

### 4. Application Layer
- Contains the use-case logic and orchestrates domain + infrastructure.
- No I/O or vendor SDKs allowed.

### 5. Domain Layer
- Must contain only pure business logic.
- No imports from FastAPI, OpenAI, or cloud SDKs.

### 6. Infrastructure Layer
- All external integration code must live here.
- Repository implementations, LLM clients, database clients.

### 7. Testing
- Use pytest.
- Create mirrors of the folder structure inside `/tests`.

### 8. Evaluation Pipelines
- Store LLM evaluation code in `/evaluation` separate from production code.

## ✔️ Copilot Should:
- Suggest DDD-aligned structure
- Prefer dependency injection patterns
- Generate absolute imports
- Use pydantic models for DTOs
- Keep domain layer free of libs like FastAPI/OpenAI

## ❌ Copilot Should NOT:
- Suggest relative imports (../../)
- Put business logic inside controllers
- Call LLMs directly from domain/application layers
- Mix evaluation code inside src/

