"""
tools/ollama_provider.py

Purpose
-------
Ollama implementation of the LLM Provider interface.

Requirements
------------
- Ollama installed
- Ollama server running
- Example:
    ollama run llama3
"""

import requests


class OllamaProvider:
    """
    Ollama LLM Provider.
    """

    def __init__(
        self,
        model="llama3",
        host="http://localhost:11434",
        temperature=0,
    ):
        """
        Initialize Ollama provider.
        """

        self.model = model

        self.host = host.rstrip("/")

        self.temperature = temperature

    # ---------------------------------------------------------
    # Generate Response
    # ---------------------------------------------------------

    def generate(
        self,
        prompt,
    ):
        """
        Generate a response using Ollama.
        """

        print()

        print("=" * 70)
        print("OLLAMA PROVIDER")
        print("=" * 70)

        url = f"{self.host}/api/generate"

        response = requests.post(

            url,

            json={

                "model": self.model,

                "prompt": prompt,

                "stream": False,

                "options": {

                    "temperature": self.temperature,

                },

            },

            timeout=300,

        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            "",
        )

    # ---------------------------------------------------------
    # Provider Information
    # ---------------------------------------------------------

    def info(
        self,
    ):
        """
        Return provider configuration.
        """

        return {

            "provider": "Ollama",

            "model": self.model,

            "host": self.host,

            "temperature": self.temperature,

        }