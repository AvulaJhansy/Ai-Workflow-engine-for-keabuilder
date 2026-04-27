def apply_lora_model(user_brand_id, prompt):
    if user_brand_id:
        return (
            f"Applied LoRA model for branding profile "
            f"{user_brand_id} with prompt: {prompt}"
        )

    return f"Standard image generation: {prompt}"