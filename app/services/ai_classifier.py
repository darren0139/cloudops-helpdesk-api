from app.schemas import AIClassifyResponse

def classify_ticket(title: str, description: str) -> AIClassifyResponse:
    """
    Beginner-safe AI placeholder.

    This is rule-based for now so the project costs $0 to run.
    Later, you can replace this with an LLM call if you want.
    """
    text = f"{title} {description}".lower()

    if any(word in text for word in ["wifi", "network", "vpn", "dns", "latency", "internet"]):
        category = "network"
        priority = "high" if any(word in text for word in ["down", "cannot connect", "outage"]) else "medium"
        reason = "Detected network/connectivity keywords."
    elif any(word in text for word in ["password", "login", "account", "permission", "access"]):
        category = "access"
        priority = "medium"
        reason = "Detected access/account keywords."
    elif any(word in text for word in ["aws", "ec2", "s3", "cloudwatch", "vpc", "rds"]):
        category = "cloud"
        priority = "medium"
        reason = "Detected cloud infrastructure keywords."
    elif any(word in text for word in ["laptop", "keyboard", "mouse", "printer", "monitor"]):
        category = "hardware"
        priority = "low"
        reason = "Detected hardware keywords."
    elif any(word in text for word in ["app", "bug", "crash", "software", "error"]):
        category = "software"
        priority = "medium"
        reason = "Detected software/application keywords."
    else:
        category = "other"
        priority = "low"
        reason = "No strong keyword match; defaulted to other."

    return AIClassifyResponse(
        suggested_category=category,
        suggested_priority=priority,
        reason=reason,
    )
