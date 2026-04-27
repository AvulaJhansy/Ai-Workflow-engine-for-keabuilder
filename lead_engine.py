def classify_lead(budget, urgency):
    score = 0

    if budget > 100000:
        score += 50
    elif budget > 50000:
        score += 30
    else:
        score += 10

    if urgency.lower() == "high":
        score += 40
    elif urgency.lower() == "medium":
        score += 20

    if score >= 80:
        lead_type = "hot"
    elif score >= 50:
        lead_type = "warm"
    else:
        lead_type = "cold"

    return score, lead_type


def generate_response(name, lead_type, message):
    return (
        f"Hi {name}, thank you for reaching out regarding "
        f"'{message}'. Based on your requirements, your lead "
        f"has been classified as {lead_type.upper()} and our team "
        f"will connect with you shortly."
    )