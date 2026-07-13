from tools.file_tool import FileTool


class DeveloperAgent:

    def __init__(self):

        self.files = FileTool()

    def prepare_task(
        self,
        state,
    ):

        print()

        print("=" * 60)
        print("DEVELOPER AGENT")
        print("=" * 60)

        source_files = self.files.find_source_files(
            state.local_path
        )

        state.source_files = source_files

        print()

        print("Source Files")

        for file in source_files:

            print(file)

        state.context = self.files.build_context(
            source_files
        )

        state.llm_prompt = self.create_prompt(
            state
        )

        return state

    def create_prompt(
        self,
        state,
    ):

        prompt = f"""
You are a Senior Software Engineer.

Jira Issue

{state.issue_key}

Summary

{state.summary}

Description

{state.description}

Implementation Plan

"""

        for step in state.implementation_plan:

            prompt += f"- {step}\n"

        prompt += """

Project Files

"""

        prompt += state.context

        prompt += """

Tasks

1. Understand the project.
2. Identify affected files.
3. Explain required modifications.
4. Do not generate code yet.
"""

        return prompt

    def preview_prompt(
        self,
        state,
    ):

        print()

        print("=" * 60)

        print("LLM PROMPT PREVIEW")

        print("=" * 60)

        preview = state.llm_prompt

        if len(preview) > 1500:

            preview = preview[:1500]

            preview += "\n\n...TRUNCATED..."

        print(preview)