"""
agents/reviewer_agent.py

Milestone 10
Reviewer Agent
"""

from tools.llm_provider import LLMFactory


class ReviewerAgent:
    """
    Reviews generated code using an LLM.
    """

    def __init__(self, provider="openai"):

        self.provider = LLMFactory.create(
            provider
        )

    # ---------------------------------------------------------

    def review(self, state):

        print()

        print("=" * 70)
        print("REVIEWER AGENT")
        print("=" * 70)

        generated_code = getattr(
            state,
            "generated_code",
            "",
        )

        if not generated_code:

            print(
                "No generated code available."
            )

            state.review_passed = False

            return state

        prompt = f"""
You are a Senior Software Engineer.

Review the following generated implementation.

Evaluate:

1. Correctness
2. Code Quality
3. Maintainability
4. Security
5. Performance

Reply ONLY with either:

APPROVED

or

REJECTED

followed by a short explanation.

Generated Code

{generated_code}
"""

        review = self.provider.generate(
            prompt
        )

        state.review = review

        state.review_passed = (
            "APPROVED"
            in review.upper()
        )

        print()

        print(review)

        return state

    # ---------------------------------------------------------

    def print_summary(self, state):

        print()

        print("=" * 70)
        print("REVIEW SUMMARY")
        print("=" * 70)

        print(
            "Approved :",
            getattr(
                state,
                "review_passed",
                False,
            ),
        )

        print("=" * 70)