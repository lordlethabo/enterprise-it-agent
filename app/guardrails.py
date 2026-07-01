from app.config import settings


def contains_prompt_injection(text: str) -> bool:
    """
    Detect common prompt injection attempts.
    """

    if not text:
        return False

    text = text.lower()

    for phrase in settings.BLOCKED_PHRASES:
        if phrase.lower() in text:
            return True

    return False


def validate_ticket(issue_title: str, issue_description: str):
    """
    Validate the incoming support ticket.
    Returns:
        (is_valid, message)
    """

    if not issue_title.strip():
        return False, "Issue title cannot be empty."

    if not issue_description.strip():
        return False, "Issue description cannot be empty."

    if len(issue_description) > settings.MAX_TICKET_LENGTH:
        return (
            False,
            f"Issue description exceeds the maximum length of {settings.MAX_TICKET_LENGTH} characters."
        )

    if contains_prompt_injection(issue_title):
        return (
            False,
            "Potential prompt injection detected in the issue title."
        )

    if contains_prompt_injection(issue_description):
        return (
            False,
            "Potential prompt injection detected in the issue description."
        )

    return True, "Validation successful."


def sanitize_text(text: str) -> str:
    """
    Remove unnecessary whitespace from user input.
    """

    if not text:
        return ""

    return " ".join(text.split())