from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.models import TicketRequest, TicketResponse
from app.agent import process_ticket


app = FastAPI(
    title="Enterprise IT Agent",
    description="AI-powered IT helpdesk agent for classifying and resolving support tickets.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Enterprise IT Agent API is running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "enterprise-it-agent",
    }


@app.post("/analyze-ticket", response_model=TicketResponse)
def analyze_ticket(ticket: TicketRequest):
    try:
        result = process_ticket(ticket)
        return result
    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to analyze ticket: {str(error)}",
        )