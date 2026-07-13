"""
tools/llm_provider.py

Purpose
-------
Provides a common interface for all supported Large Language Model providers.

Supported Providers
-------------------
- Mock
- Claude
- OpenAI
- Gemini
- Ollama
"""

from abc import ABC, abstractmethod

from tools.claude_provider import ClaudeProvider
from tools.openai_provider import OpenAIProvider
from tools.gemini_provider import GeminiProvider
from tools.ollama_provider import OllamaProvider


# ==========================================================
# Base Provider
# ==========================================================

class LLMProvider(ABC):
    """
    Base interface implemented by every LLM provider.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generate a response from the language model.
        """
        pass


# ==========================================================
# Mock Provider
# ==========================================================

class MockLLMProvider(LLMProvider):
    """
    Mock provider used for development and testing.
    """

    def generate(self, prompt: str) -> str:

        print()

        print("=" * 70)
        print("MOCK LLM PROVIDER")
        print("=" * 70)

        print(
            f"Prompt Length : {len(prompt)} characters"
        )

        print()

        return """
FILE: sample.py

```python
def hello():
    print("Hello from Mock LLM")
```
"""


# ==========================================================
# Provider Factory
# ==========================================================

class LLMFactory:
    """
    Factory responsible for creating LLM providers.
    """

    @staticmethod
    def create(provider="mock"):
        """
        Create the requested provider.

        Parameters
        ----------
        provider : str

        Returns
        -------
        LLMProvider
        """

        provider = provider.lower()

        if provider == "mock":
            return MockLLMProvider()

        elif provider == "claude":
            return ClaudeProvider()

        elif provider == "openai":
            return OpenAIProvider()

        elif provider == "gemini":
            return GeminiProvider()

        elif provider == "ollama":
            return OllamaProvider()

        raise ValueError(
            f"Unsupported provider: {provider}"
        )

    @staticmethod
    def supported_providers():
        """
        Return the list of supported providers.
        """

        return [
            "mock",
            "claude",
            "openai",
            "gemini",
            "ollama",
        ]