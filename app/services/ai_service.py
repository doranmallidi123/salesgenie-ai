"""Internal outreach generation service.

This deterministic implementation provides a usable local draft generator. It
can be replaced by an LLM-backed implementation without changing the API.
"""

from typing import Any


def generate_outreach_email(
    lead_data: dict[str, Any], tone: str
) -> dict[str, str]:
    """Generate an outreach draft using only the lead profile and supplied focus.

    The function avoids inventing company facts. Integrations can replace this
    implementation while preserving the same input and output contract.
    """
    contact_name = str(lead_data.get("contact_name") or "there").strip()
    company_name = str(lead_data.get("company_name") or "your team").strip()
    industry = str(lead_data.get("industry") or "your industry").strip()
    focus_points = str(lead_data.get("focus_points") or "").strip()
    focus_sentence = (
        f"I would be glad to discuss {focus_points}."
        if focus_points
        else f"I would be glad to learn about your priorities at {company_name}."
    )
    tone_label = tone.strip().lower()

    subject = f"A conversation about {company_name}'s priorities"
    content = (
        f"Hi {contact_name},\n\n"
        f"I’m reaching out to connect with {company_name} in the {industry} space. "
        f"{focus_sentence}\n\n"
        "Would you be open to a brief conversation this week?\n\n"
        "Best,\nSalesGenie"
    )
    follow_up = (
        f"If there is no reply, send a brief, {tone_label} follow-up after 3 business days. "
        "If there is still no response, make one final follow-up a week later with a concise "
        "summary of the proposed conversation."
    )
    return {
        "email_subject": subject,
        "email_content": content,
        "follow_up_strategy": follow_up,
    }
