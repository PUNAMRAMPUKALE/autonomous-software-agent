"""
tools/claude_provider.py

Purpose
-------
Anthropic Claude implementation of the LLMProvider interface.
"""

import os

from anthropic import Anthropic


class ClaudeProvider:
    """
    Anthropic Claude Provider.
    """

    def __init__(
        self,
        model="claude-sonnet-4-20250514",
        temperature=0,
        max_tokens=4096,
    ):
        """
        Initialize Claude client.
        """

        api_key = os.getenv(
            "ANTHROPIC_API_KEY"
        )

        if not api_key:

            raise ValueError(
                "ANTHROPIC_API_KEY environment variable not found."
            )

        self.client = Anthropic(
            api_key=api_key
        )

        self.model = model

        self.temperature = temperature

        self.max_tokens = max_tokens

    # ---------------------------------------------------------
    # Generate Response
    # ---------------------------------------------------------

    def generate(
        self,
        prompt,
    ):
        """
        Send a prompt to Claude and return the response.
        """

        print()

        print("=" * 70)
        print("CLAUDE PROVIDER")
        print("=" * 70)

        response = self.client.messages.create(

            model=self.model,

            temperature=self.temperature,

            max_tokens=self.max_tokens,

            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        output = []

        for block in response.content:

            if hasattr(
                block,
                "text",
            ):

                output.append(
                    block.text
                )

        return "\n".join(output)

    # ---------------------------------------------------------
    # Provider Information
    # ---------------------------------------------------------

    def info(self):
        """
        Return provider configuration.
        """

        return {

            "provider": "Anthropic Claude",

            "model": self.model,

            "temperature": self.temperature,

            "max_tokens": self.max_tokens,

        }