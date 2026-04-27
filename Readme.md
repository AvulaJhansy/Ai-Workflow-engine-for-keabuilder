# KeaBuilder AI Workflow Engine

An end-to-end AI workflow prototype designed for **Dream Reflection Media – AI Engineer Assessment**.

This project simulates how AI capabilities can be integrated into **KeaBuilder**, a SaaS platform for funnels, lead capture, automation, and content generation.

---

## Project Objective

The goal of this project is to design and implement an intelligent workflow system that can:

- classify incoming leads
- generate personalized responses
- route requests to the best AI provider
- apply brand-level personalization
- perform similarity search
- handle provider fallback
- support high-volume request processing

This workflow demonstrates **system design thinking + practical implementation skills**.

---

## Workflow Architecture

```text
User Form Input
        ↓
Lead Classification
        ↓
Response Generation
        ↓
Provider Routing
        ↓
LoRA Personalization
        ↓
Similarity Search
        ↓
Fallback Handling
        ↓
Queue Processing
        ↓
Final Output
```

---

## Features Implemented

### 1. Lead Classification
Classifies leads into:

- HOT
- WARM
- COLD

Based on:

- budget
- urgency
- business message

Example:

```json
{
  "score": 90,
  "lead_type": "hot"
}
```

---

### 2. Personalized Response Engine
Generates human-like responses using:

- user name
- lead type
- business requirement

Example:

```text
Hi Rahul, thank you for reaching out regarding AI funnel automation.
```

---

### 3. Multi-Provider Routing
Routes requests based on content type.

```text
image → Stability AI
video → Runway ML
voice → ElevenLabs
```

This simulates provider orchestration inside KeaBuilder.

---

### 4. LoRA Personalization
Supports brand-consistent image generation.

Example:

```text
brand_001 → apply style profile
```

This ensures:

- consistent branding
- reusable visual identity
- personalized outputs

---

### 5. Similarity Search
Finds similar assets/templates using similarity logic.

Example use cases:

- similar banner templates
- prompt matching
- reusable assets

---

### 6. Fallback Handling
Implements reliability layer for:

- provider failure
- timeout
- retry

Example:

```text
Primary provider fails → backup provider executes
```

---

### 7. Queue Management
Supports scalable request processing.

Used for:

- high traffic
- batch requests
- optimization

---

## Tech Stack

- Python
- FastAPI
- Streamlit
- Pydantic
- Uvicorn

---

## Project Structure

```text
keabuilder-ai-workflow/
│
├── main.py
├── models.py
├── lead_engine.py
├── provider_router.py
├── lora_pipeline.py
├── similarity_search.py
├── fallback_service.py
├── queue_manager.py
├── app.py
├── requirements.txt
└── README.md
```

---

## How to Run

### Backend

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

### Streamlit UI

```bash
streamlit run app.py
```

---

## Sample Input

```json
{
  "name": "Rahul",
  "email": "rahul@gmail.com",
  "budget": 120000,
  "urgency": "high",
  "message": "Need AI funnel automation",
  "content_type": "image",
  "prompt": "Generate brand campaign banner",
  "user_brand_id": "brand_001"
}
```

---

## Sample Output

```json
{
  "lead_classification": {
    "score": 90,
    "lead_type": "hot"
  },
  "personalized_response": "Hi Rahul, thank you for reaching out regarding AI funnel automation.",
  "content_provider": "Stability AI",
  "lora_output": "Applied LoRA model",
  "similar_asset": "template_1",
  "similarity_score": 0.99,
  "fallback_status": "success",
  "queue_processed_requests": 1
}
```

---

## Engineering Decisions

- Modular architecture
- service-based workflow
- scalable request handling
- provider abstraction
- easy API extensibility

---

## Future Scope

- vector database integration
- async workers (Celery / Redis)
- real provider APIs
- analytics dashboard
- user asset memory