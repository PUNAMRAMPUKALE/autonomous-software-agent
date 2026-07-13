"""
tools/provider_registry.py

Purpose
-------
Central registry for all supported Large Language Model providers.

Supported Providers
-------------------
- Mock
- Claude
- OpenAI
- Gemini
- Ollama
"""

from tools.llm_provider import MockLLMProvider
from tools.claude_provider import ClaudeProvider
from tools.openai_provider import OpenAIProvider
from tools.gemini_provider import GeminiProvider
from tools.ollama_provider import OllamaProvider


class ProviderRegistry:
    """
    Factory responsible for creating LLM providers.
    """

    _providers = {

        "mock": MockLLMProvider,

        "claude": ClaudeProvider,

        "openai": OpenAIProvider,

        "gemini": GeminiProvider,

        "ollama": OllamaProvider,

    }

    # ---------------------------------------------------------
    # Create Provider
    # ---------------------------------------------------------

    @classmethod
    def create(
        cls,
        provider="mock",
        **kwargs,
    ):
        """
        Create an LLM provider.

        Parameters
        ----------
        provider : str

        Returns
        -------
        LLM Provider
        """

        provider = provider.lower()

        if provider not in cls._providers:

            raise ValueError(
                f"Unsupported provider: {provider}"
            )

        return cls._providers[
            provider
        ](**kwargs)

    # ---------------------------------------------------------
    # Register Provider
    # ---------------------------------------------------------

    @classmethod
    def register(
        cls,
        name,
        provider,
    ):
        """
        Register a custom provider.
        """

        cls._providers[
            name.lower()
        ] = provider

    # ---------------------------------------------------------
    # Supported Providers
    # ---------------------------------------------------------

    @classmethod
    def supported(
        cls,
    ):
        """
        Return supported provider names.
        """

        return sorted(
            cls._providers.keys()
        )

    # ---------------------------------------------------------
    # Exists
    # ---------------------------------------------------------

    @classmethod
    def exists(
        cls,
        provider,
    ):
        """
        Check whether a provider exists.
        """

        return provider.lower() in cls._providers