from pydantic import BaseModel, Field
from typing import Literal, Optional

Priority = Literal["low", "medium", "high"]
Status = Literal["open", "in_progress", "resolved"]
Category = Literal["network", "access", "software", "hardware", "cloud", "other"]

class TicketCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=5, max_length=1000)
    category: Category = "other"
    priority: Priority = "medium"

class TicketUpdate(BaseModel):
    status: Optional[Status] = None
    priority: Optional[Priority] = None

class TicketOut(BaseModel):
    id: int
    title: str
    description: str
    category: Category
    priority: Priority
    status: Status
    created_at: str

class AIClassifyRequest(BaseModel):
    title: str
    description: str

class AIClassifyResponse(BaseModel):
    suggested_category: Category
    suggested_priority: Priority
    reason: str
