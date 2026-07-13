"""
agents/patch_agent.py

Purpose
-------
Convert the LLM response into a CodePatch.
"""

from tools.response_parser import ResponseParser


class PatchAgent:

    def __init__(self):

        self.parser = ResponseParser()

    # ---------------------------------------------------------
    # Generate Patch
    # ---------------------------------------------------------

    def generate_patch(
        self,
        state,
    ):

        print()

        print("=" * 70)
        print("PATCH AGENT")
        print("=" * 70)

        #
        # CodingAgent stores the LLM output here.
        #
        response = getattr(
            state,
            "generated_code",
            "",
        )

        if not response:

            print("No LLM response found.")

            state.patch = None

            return state

        if not self.parser.validate(
            response
        ):

            print(
                "Invalid LLM response format."
            )

            state.patch = None

            return state

        patch = self.parser.parse(
            response
        )

        self.parser.print_summary(
            patch
        )

        state.patch = patch

        return state

    # ---------------------------------------------------------
    # Print Summary
    # ---------------------------------------------------------

    def print_summary(
        self,
        patch,
    ):

        print()

        print("=" * 70)
        print("PATCH SUMMARY")
        print("=" * 70)

        if patch is None:

            print("Operations : 0")

            print("=" * 70)

            return

        print(
            f"Operations : {patch.total_operations()}"
        )

        print("=" * 70)