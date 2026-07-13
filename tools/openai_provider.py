"""
tools/openai_provider.py
"""

import os

from openai import OpenAI


class OpenAIProvider:

    def __init__(
        self,
        model=None,
        max_tokens=4096,
    ):

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY not found."
            )

        self.client = OpenAI(
            api_key=api_key
        )

        self.model = model or os.getenv(
            "LLM_MODEL",
            "gpt-4.1-mini",
        )

        self.max_tokens = max_tokens

    # ---------------------------------------------------------

    def generate(
        self,
        prompt,
    ):

        print()
        print("=" * 70)
        print("OPENAI PROVIDER")
        print("=" * 70)

        response = self.client.responses.create(
            model=self.model,
            input=prompt,
            max_output_tokens=self.max_tokens,
            reasoning={
                "effort": "minimal"
            },
       )

        #
        # First try the SDK helper.
        #

        text = getattr(
            response,
            "output_text",
            "",
        )

        #
        # Fallback for older/newer SDK formats.
        #

        if not text:

            parts = []

            for item in getattr(
                response,
                "output",
                [],
            ):

                for content in getattr(
                    item,
                    "content",
                    [],
                ):

                    if getattr(
                        content,
                        "type",
                        "",
                    ) == "output_text":

                        parts.append(
                            content.text
                        )

                    elif hasattr(
                        content,
                        "text",
                    ):

                        parts.append(
                            content.text
                        )

            text = "\n".join(parts)

        text = text.strip()

        print()
        print("Generation Complete")
        print(
            f"Response Size : {len(text)} characters"
        )

        #
        # Print raw response if nothing was returned.
        #

        if not text:

            print()
            print("RAW RESPONSE")
            print(response)

        return text

    # ---------------------------------------------------------

    def info(self):

        return {

            "provider": "OpenAI",

            "model": self.model,

        }