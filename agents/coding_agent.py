"""
agents/coding_agent.py

Purpose
-------
Send the prepared developer prompt to an LLM and store the generated
response inside AgentState.
"""

from tools.llm_provider import LLMFactory


class CodingAgent:
    """
    Generates code using the configured LLM provider.
    """

    def __init__(
        self,
        provider="mock",
    ):
        """
        Initialize the coding agent.
        """

        self.provider = LLMFactory.create(
            provider
        )

    # ---------------------------------------------------------
    # Generate Code
    # ---------------------------------------------------------

    def generate(
        self,
        state,
    ):
        """
        Generate code from the LLM.

        Parameters
        ----------
        state : AgentState

        Returns
        -------
        AgentState
        """

        print()

        print("=" * 70)
        print("CODING AGENT")
        print("=" * 70)

        #
        # Force the model to return machine-readable output.
        #

        output_format = """

======================================================================
OUTPUT FORMAT (MANDATORY)
======================================================================

Return ONLY repository files.

DO NOT explain anything.

DO NOT summarize.

DO NOT say "Here is the implementation".

DO NOT use Markdown except the required code fences.

DO NOT use unified diff.

DO NOT use:

*** Begin Patch

*** End Patch

For EVERY modified file return EXACTLY:

FILE: relative/path/to/file.py

```python
<complete file contents>
```

Example

FILE: app.py

```python
print("hello")
```

FILE: tools/test_runner.py

```python
def run():
    pass
```

Rules

1. Return ONLY FILE blocks.

2. Do NOT output any text before the first FILE block.

3. Do NOT output any text after the last FILE block.

4. Every FILE block must contain the COMPLETE file.

5. Never return partial snippets.

======================================================================
"""

        prompt = (

            state.llm_prompt

            + "\n"

            + output_format

        )

        response = self.provider.generate(
            prompt
        )

        state.generated_code = response

        print()

        print("Generation Complete")

        print(
            f"Response Size : {len(response)} characters"
        )

        return state

    # ---------------------------------------------------------
    # Preview Response
    # ---------------------------------------------------------

    def preview_response(
        self,
        state,
        limit=4000,
    ):
        """
        Print the first part of the LLM response.
        """

        print()

        print("=" * 70)
        print("LLM RESPONSE")
        print("=" * 70)

        response = state.generated_code

        if len(response) > limit:

            print(
                response[:limit]
            )

            print()

            print("...TRUNCATED...")

        else:

            print(response)

        print("=" * 70)