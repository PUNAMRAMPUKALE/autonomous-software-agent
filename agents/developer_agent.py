"""
agents/developer_agent.py

Purpose
-------
Prepare the prompt for the LLM.

Responsibilities
----------------
1. Read retrieved repository symbols.
2. Read only the required source code.
3. Build a structured implementation prompt.
4. Reduce token usage.
5. Preserve project architecture.

This component DOES NOT call an LLM.
"""

import os


class DeveloperAgent:
    """
    Prepare implementation context for downstream AI models.
    """

    def __init__(self):
        """
        Initialize Developer Agent.
        """
        pass

    # ---------------------------------------------------------
    # Main Entry
    # ---------------------------------------------------------

    def prepare_task(self, state):
        """
        Build repository context.

        Parameters
        ----------
        state : AgentState

        Returns
        -------
        AgentState
        """

        print()

        print("=" * 70)
        print("DEVELOPER AGENT")
        print("=" * 70)

        context = self.build_context(state)

        state.context = context

        state.llm_prompt = self.build_prompt(
            state,
            context,
        )

        print()

        print(
            f"Relevant Symbols : {len(state.relevant_symbols)}"
        )

        print(
            f"Prompt Length    : {len(state.llm_prompt)}"
        )

        return state

    # ---------------------------------------------------------
    # Build Repository Context
    # ---------------------------------------------------------

    def build_context(self, state):
        """
        Read only retrieved repository symbols.

        This greatly reduces prompt size.
        """

        sections = []

        added = set()

        for symbol in state.relevant_symbols:

            if symbol.symbol_id in added:
                continue

            added.add(symbol.symbol_id)

            code = self.read_symbol(symbol)

            if not code:
                continue

            sections.append("=" * 70)

            sections.append(
                symbol.symbol_id
            )

            sections.append("=" * 70)

            sections.append(code)

            sections.append("")

        return "\n".join(sections)

    # ---------------------------------------------------------
    # Read Symbol
    # ---------------------------------------------------------

    def read_symbol(self, symbol):
        """
        Read only the source code belonging to one symbol.
        """

        try:

            with open(
                symbol.file_path,
                "r",
                encoding="utf-8",
            ) as file:

                lines = file.readlines()

        except Exception:

            return ""

        start = max(
            symbol.start_line - 1,
            0,
        )

        end = symbol.end_line

        return "".join(
            lines[start:end]
        )

    # ---------------------------------------------------------
    # Build Prompt
    # ---------------------------------------------------------

    def build_prompt(
        self,
        state,
        context,
    ):
        """
        Build the implementation prompt.
        """

        prompt = []

        prompt.append(
            "You are a Senior Software Engineer."
        )

        prompt.append("")

        prompt.append(
            "Complete the Jira story."
        )

        prompt.append("")

        prompt.append("Jira Issue")

        prompt.append(state.issue_key)

        prompt.append("")

        prompt.append("Summary")

        prompt.append(state.summary)

        prompt.append("")

        prompt.append("Description")

        prompt.append(state.description)

        prompt.append("")

        prompt.append("Implementation Plan")

        for item in state.implementation_plan:

            prompt.append(
                f"- {item}"
            )

        prompt.append("")

        prompt.append(
            "Repository Context"
        )

        prompt.append("")

        prompt.append(context)

        prompt.append("")

        prompt.append("Requirements")

        prompt.append(
            "- Follow existing architecture."
        )

        prompt.append(
            "- Reuse existing components."
        )

        prompt.append(
            "- Preserve coding conventions."
        )

        prompt.append(
            "- Minimize changes."
        )

        prompt.append(
            "- Update tests if required."
        )

        return "\n".join(prompt)

    # ---------------------------------------------------------
    # Prompt Preview
    # ---------------------------------------------------------

    def preview_prompt(
        self,
        state,
        max_length=4000,
    ):
        """
        Print a preview of the generated prompt.
        """

        print()

        print("=" * 70)
        print("LLM PROMPT PREVIEW")
        print("=" * 70)

        preview = state.llm_prompt

        if len(preview) > max_length:

            preview = (
                preview[:max_length]
                + "\n\n...TRUNCATED..."
            )

        print(preview)

        print()

        print("=" * 70)

        print(
            f"Prompt Length : {len(state.llm_prompt)}"
        )

        print("=" * 70)