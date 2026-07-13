"""
app.py

Purpose
-------
Main entry point for the Autonomous Software Engineering Agent.

Workflow
--------
Planner
    ↓
GitHub
    ↓
Repository Analyzer
    ↓
Repository Indexer
    ↓
Repository Graph
    ↓
Retrieval Agent
    ↓
Developer Agent
    ↓
Coding Agent
    ↓
Patch Agent
    ↓
Patch Validator
    ↓
File Writer
"""

from agents.planner import PlannerAgent
from agents.github_agent import GitHubAgent
from agents.repository_analyzer import RepositoryAnalyzer
from agents.indexing_agent import IndexingAgent
from agents.retrieval_agent import RetrievalAgent
from agents.developer_agent import DeveloperAgent
from agents.coding_agent import CodingAgent
from agents.patch_agent import PatchAgent

from tools.patch_validator import PatchValidator
from tools.file_writer import FileWriter
from config import LLM_PROVIDER


def main():
    """
    Execute the complete autonomous software engineering workflow.
    """

    print("=" * 70)
    print("AUTONOMOUS SOFTWARE ENGINEERING AGENT")
    print("=" * 70)

    # ==========================================================
    # Planner
    # ==========================================================

    planner = PlannerAgent()

    state = planner.choose_next_story()

    if state is None:
        return

    # ==========================================================
    # Prepare Repository
    # ==========================================================

    github = GitHubAgent()

    state = github.prepare_repository(
        state
    )

    # ==========================================================
    # Analyze Repository
    # ==========================================================

    analyzer = RepositoryAnalyzer()

    state = analyzer.analyze(
        state
    )

    # ==========================================================
    # Build Repository Index
    # ==========================================================

    indexer = IndexingAgent()

    state = indexer.build_index(
        state
    )

    # ==========================================================
    # Retrieve Relevant Context
    # ==========================================================

    retrieval = RetrievalAgent()

    state = retrieval.retrieve(
        state
    )

    # ==========================================================
    # Prepare Developer Context
    # ==========================================================

    developer = DeveloperAgent()

    state = developer.prepare_task(
        state
    )

    developer.preview_prompt(
        state
    )

    # ==========================================================
    # Generate Code
    # ==========================================================

    #
    # Change provider="claude" when you configure
    # ANTHROPIC_API_KEY.
    #

    coding = CodingAgent(
    provider=LLM_PROVIDER
)

    state = coding.generate(
        state
    )

    coding.preview_response(
        state
    )

    # ==========================================================
    # Generate Patch
    # ==========================================================

    patch_agent = PatchAgent()

    state = patch_agent.generate_patch(
        state
    )

    patch_agent.print_summary(
        state.patch
    )

    # ==========================================================
    # Validate Patch
    # ==========================================================

    validator = PatchValidator()

    valid, errors = validator.validate(
        state.patch
    )

    validator.print_report(
        valid,
        errors,
    )

    # ==========================================================
    # Apply Patch
    # ==========================================================

    if valid:

        writer = FileWriter()

        writer.apply_patch(
            state.patch
        )

    else:

        print()

        print("Patch validation failed.")

        print("Repository was not modified.")

    # ==========================================================
    # Jira Story Summary
    # ==========================================================

    planner.print_selected_story(
        state
    )

    # ==========================================================
    # Final Summary
    # ==========================================================

    print()

    print("=" * 70)
    print("WORKFLOW SUMMARY")
    print("=" * 70)

    print(f"Issue               : {state.issue_key}")
    print(f"Summary             : {state.summary}")
    print(f"Language            : {state.language}")
    print(f"Framework           : {state.framework}")
    print(f"Entry Point         : {state.entry_point}")
    print(f"Source Files        : {len(state.source_files)}")
    print(f"Indexed Symbols     : {len(state.symbols)}")
    print(f"Relevant Symbols    : {len(state.relevant_symbols)}")

    if state.patch:

        print(
            f"Patch Operations    : {state.patch.total_operations()}"
        )

    else:

        print(
            "Patch Operations    : 0"
        )

    print("=" * 70)

    print()

    print("Workflow completed successfully.")

    print("=" * 70)


if __name__ == "__main__":
    main()