def call_primary_service():
    raise TimeoutError("Primary provider timeout")


def call_fallback_service():
    return "Fallback provider response success"


def execute_with_fallback():
    try:
        return call_primary_service()
    except Exception:
        return call_fallback_service()