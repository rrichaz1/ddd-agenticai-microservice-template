.github/COPILOT_INSTRUCTIONS
Instructions for GitHub Copilot
🎯 Goal

This repository uses a Domain-Driven Design (DDD) architecture for building Python microservices using FastAPI, src/ layout, multiple deployable apps, shared utilities, evaluation pipelines, and Streamlit demo apps.
Copilot should generate and update code following these conventions.

📐 General Architectural Rules
1️⃣ Use DDD Layers

Each microservice (app1, app2, etc.) must be structured via:

appX/
  api/           → FastAPI routers, request/response models
  application/   → services coordinating domain logic
  domain/        → domain models, logic, aggregates, value objects
  infrastructure/→ adapters, repositories, clients


Copilot must NOT mix domain, application, and infrastructure concerns.
Domain layer stays pure and framework-free.

2️⃣ Use src/ layout

All packages must live under:

src/
  app1/
  app2/
  shared/


Imports must always be absolute, never relative:

❌ from ..domain import X
✅ from app1.domain.model import X

3️⃣ Multi-App Architecture

Copilot should expect multiple deployables in the same repo:

src/app1/ → microservice 1  
src/app2/ → microservice 2
src/shared/ → utilities / common libs


Shared code (e.g., OpenAI adapter, config loader, logging) goes in:

src/shared/utils/
src/shared/adapters/

4️⃣ Streamlit Demo Apps

Local test UIs must be placed under:

streamlit_apps/
  app1_demo/
  app2_demo/
  shared_components/


Copilot should generate Streamlit apps that import directly from src/ modules.

⚒️ Copilot Coding Conventions
5️⃣ Use uv for dependency management

When generating commands or docs, Copilot should prefer:

uv add fastapi
uv run uvicorn app1.api.main:app

6️⃣ FastAPI Structure

For each microservice, Copilot should create:

api/

Routers organized by domain context

Pydantic models for requests/responses

application/

Handlers, orchestrating domain logic

No external service code inside domain

domain/

Entities, value objects, invariants

Should not import FastAPI or infrastructure

infrastructure/

DB, external APIs, OpenAI adapters

Config & logging utilities

🧪 Testing Standards

Copilot should create tests under:

tests/
  app1/
  app2/
  shared/


Following conventions:

Use pytest

Use async tests when applicable

Use FastAPI TestClient or HTTPX

🧠 Evaluation Pipeline

Copilot should create evaluation pipelines under:

eval/
  scenarios/
  metrics/
  runners/


Where:

scenarios = test prompts, LLM inputs

metrics = correctness, hallucination, latency

runners = scripts callable via CI

Evaluation must run locally and via GitHub Actions.

🔄 CI/CD Expectations

Copilot must generate GitHub Actions workflows with:

uv sync for dependencies

running tests

running evaluation pipeline

building & pushing Docker images for each app (app1, app2)

Artifacts:

app1-image:latest
app2-image:latest

🧱 Directory Layout to Follow

Copilot must follow this structure unless explicitly instructed otherwise:

src/
  app1/
    api/
    application/
    domain/
    infrastructure/
  app2/
    api/
    application/
    domain/
    infrastructure/
  shared/
    utils/
    adapters/
streamlit_apps/
  app1_demo/
  app2_demo/
  shared_components/
eval/
tests/
.github/
  workflows/
  COPILOT_INSTRUCTIONS

🦾 Copilot Must Enforce Clean Code

Prefer type-hinted functions

No business logic inside API routers

Domain logic = pure, framework-free

External systems only via adapters

Config loaded through shared utilities

No deep relative imports

📌 Example Prompts Copilot Should Respond Well To

Copilot should know how to generate:

“Create a FastAPI router in app1/api/items.py and wire it to the app.”

“Add a new domain entity in app2 with invariants.”

“Create an evaluation scenario comparing two LLM responses.”

“Generate a Streamlit UI that tests the app1 /predict endpoint.”

“Add GitHub Actions workflow to run tests and eval using uv.”

✔️ End of Copilot Instructions