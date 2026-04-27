from fastapi import FastAPI
from models import LeadInput
from lead_engine import classify_lead, generate_response
from provider_router import route_provider
from lora_pipeline import apply_lora_model
from similarity_search import find_similar_asset
from fallback_service import execute_with_fallback
from queue_manager import add_request, process_requests

app = FastAPI()


@app.post("/keabuilder-ai-workflow")
def process_workflow(data: LeadInput):

    # Feature A: Handle incomplete or unclear input
    if not data.message.strip():
        return {
            "error": "Lead message is incomplete. Please provide business requirements."
        }

    # Lead classification
    score, lead_type = classify_lead(
        data.budget,
        data.urgency
    )

    # Feature B: Decision explainability
    decision_reason = (
        f"Lead classified as {lead_type.upper()} because "
        f"budget is {data.budget} and urgency is '{data.urgency}'."
    )

    # Personalized response generation
    response = generate_response(
        data.name,
        lead_type,
        data.message
    )

    # Multi-provider routing
    provider = route_provider(data.content_type)

    # LoRA personalization
    lora_output = apply_lora_model(
        data.user_brand_id,
        data.prompt
    )

    # Similarity search
    similar_asset, similarity_score = find_similar_asset()

    # Fallback handling
    fallback_status = execute_with_fallback()

    # Queue management / scalability simulation
    add_request(data.dict())
    queue_status = process_requests()

    return {
        "lead_classification": {
            "score": score,
            "lead_type": lead_type,
            "decision_reason": decision_reason
        },
        "personalized_response": response,
        "content_provider": provider,
        "lora_output": lora_output,
        "similar_asset": similar_asset,
        "similarity_score": similarity_score,
        "fallback_status": fallback_status,
        "queue_processed_requests": len(queue_status)
    }