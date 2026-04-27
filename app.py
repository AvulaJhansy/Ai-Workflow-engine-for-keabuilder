import streamlit as st
import requests

st.set_page_config(
    page_title="KeaBuilder AI Workflow Demo",
    layout="centered"
)

st.title("KeaBuilder AI Workflow Demo")
st.write("AI-powered lead processing, routing, personalization, and fallback workflow")

# Input form
name = st.text_input("Name", "Rahul")
email = st.text_input("Email", "rahul@gmail.com")
budget = st.number_input("Budget", min_value=0, value=120000)
urgency = st.selectbox("Urgency", ["high", "medium", "low"])
message = st.text_area("Business Requirement", "Need AI funnel automation")
content_type = st.selectbox("Content Type", ["image", "video", "voice"])
prompt = st.text_input("Prompt", "Generate brand campaign banner")
user_brand_id = st.text_input("Brand ID", "brand_001")

if st.button("Run Workflow"):

    payload = {
        "name": name,
        "email": email,
        "budget": budget,
        "urgency": urgency,
        "message": message,
        "content_type": content_type,
        "prompt": prompt,
        "user_brand_id": user_brand_id
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/keabuilder-ai-workflow",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            st.success("Workflow Executed Successfully")

            st.subheader("Lead Classification")
            st.json(result["lead_classification"])

            st.subheader("Personalized Response")
            st.write(result["personalized_response"])

            st.subheader("AI Provider Routing")
            st.write(result["content_provider"])

            st.subheader("LoRA Personalization")
            st.write(result["lora_output"])

            st.subheader("Similarity Search")
            st.write(f"Similar Asset: {result['similar_asset']}")
            st.write(f"Similarity Score: {result['similarity_score']}")

            st.subheader("Fallback Service")
            st.write(result["fallback_status"])

            st.subheader("Queue Processing")
            st.write(f"Processed Requests: {result['queue_processed_requests']}")

        else:
            st.error(f"Error: {response.status_code}")
            st.json(response.json())

    except Exception as e:
        st.error(f"Backend connection failed: {str(e)}")