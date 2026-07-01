from typing import List, Optional
from pydantic import BaseModel, Field


class TicketRequest(BaseModel):
    employee_name: str = Field(..., example="Lethabo Phasha")
    department: str = Field(..., example="Finance")
    issue_title: str = Field(..., example="Cannot access Outlook")
    issue_description: str = Field(
        ...,
        example="My Outlook keeps asking for my password and I cannot access my emails."
    )
    affected_system: Optional[str] = Field(default=None, example="Outlook")
    urgency: Optional[str] = Field(default="medium", example="high")


class TroubleshootingStep(BaseModel):
    step_number: int
    instruction: str


class TicketResponse(BaseModel):
    ticket_id: str
    category: str
    priority: str
    severity: str
    assigned_team: str
    escalation_required: bool
    summary: str
    recommended_steps: List[TroubleshootingStep]
    business_impact: str
    estimated_resolution_time: str
    confidence_score: float
    guardrail_status: str
    ai_used: bool