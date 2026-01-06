class AIEngine:
    """
    AI Engine wrapper.
    All LLM calls will live here.
    This keeps AI isolated from business logic.
    """

    def __init__(self):
        self.enabled = True  # TURN AI ON
        self.mode = "refine"  # refine | rewrite (future)

    def enhance_story(self, distilled_output: dict) -> dict:
        """
        Enhances producer logic using AI-style refinement.
        This is a controlled mock before real LLM integration.
        """

        if not self.enabled:
            return distilled_output

        enhanced = distilled_output.copy()

        # Simulated AI refinement (safe)
        if "logline" in enhanced:
            enhanced["logline"] = enhanced["logline"].rstrip(".") + \
                " — a high-stakes moral drama."

        if "tone" in enhanced:
            enhanced["tone"] = enhanced["tone"] + " and emotionally intense"

        enhanced["ai_notes"] = (
            "Story shows strong emotional conflict suitable for mid-budget cinema."
        )

        return enhanced

