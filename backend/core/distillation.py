def distill_story(raw_text: str) -> dict:
    """
    Distills a raw film idea or script into core story components
    from a producer's perspective.
    """

    text = raw_text.strip()

    if len(text) < 50:
        return {
            "error": "Input too short for meaningful story analysis"
        }

    # Basic heuristics (producer-style thinking)
    genre = "Drama"
    tone = "Grounded"

    if any(word in text.lower() for word in ["crime", "murder", "police", "gang"]):
        genre = "Crime / Drama"
        tone = "Serious"

    logline = text.split(".")[0].strip()

    return {
        "logline": logline,
        "genre": genre,
        "tone": tone,
        "core_conflict": "Personal values vs external pressure",
        "protagonist_goal": "Protect family while facing moral dilemma",
        "emotional_driver": "Fear of loss and desire for truth"
    }
