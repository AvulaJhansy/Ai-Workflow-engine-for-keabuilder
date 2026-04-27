def route_provider(content_type):
    providers = {
        "image": "Stability AI",
        "video": "Runway ML",
        "voice": "ElevenLabs"
    }

    return providers.get(content_type.lower(), "Default AI Provider")