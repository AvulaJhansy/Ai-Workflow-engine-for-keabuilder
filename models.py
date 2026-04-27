from pydantic import BaseModel
from typing import Optional


class LeadInput(BaseModel):
    name: str
    email: str
    budget: int
    urgency: str
    message: str
    content_type: str
    prompt: str
    user_brand_id: Optional[str] = None