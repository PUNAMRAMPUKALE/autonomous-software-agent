"""
tools/gemini_provider.py

Purpose
-------
Google Gemini implementation of the LLM Provider interface.
"""

import os

import google.generativeai as genai


class GeminiProvider:
    """
    Google Gemini Provider.
    """

    def __init__(
        self,
        model="gemini-2.5-pro",
        temperature=0,
        max_tokens=4096,
    ):
        """
        Initialize Gemini client.
        """

        api_key = os.getenv(
            "GOOGLE_API_KEY"
        )

        if not api_key:

            raise ValueError(
                "GOOGLE_API_KEY environment variable not found."
            )

        genai.configure(
            api_key=api_key
        )

        self.model = genai.GenerativeModel(
            model
        )

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
        Generate a response using Gemini.
        """

        print()

        print("=" * 70)
        print("GEMINI PROVIDER")
        print("=" * 70)

        response = self.model.generate_content(

            prompt,

            generation_config={

                "temperature": self.temperature,

                "max_output_tokens": self.max_tokens,

            },

        )

        return response.text

    # ---------------------------------------------------------
    # Provider Information
    # ---------------------------------------------------------

    def info(self):
        """
        Return provider configuration.
        """

        return {

            "provider": "Google Gemini",

            "temperature": self.temperature,

            "max_tokens": self.max_tokens,

        }