"""
app.py

Autonomous Software Engineering Agent

End-to-End Workflow

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
    ↓
Reviewer Agent
    ↓
Tester Agent
    ↓
GitHub Delivery Agent
    ↓
Pull Request Agent
    ↓
Jira Delivery Agent
    ↓
Slack Notification Agent
"""

from config import LLM_PROVIDER

from agents.planner import PlannerAgent
from agents.github_agent import GitHubAgent
from agents.repository_analyzer import RepositoryAnalyzer
from agents.indexing_agent import IndexingAgent
from agents.retrieval_agent import RetrievalAgent
from agents.developer_agent import DeveloperAgent
from agents.coding_agent import CodingAgent
from agents.patch_agent import PatchAgent
from agents.reviewer_agent import ReviewerAgent
from agents.tester_agent import TesterAgent
from agents.github_delivery_agent import GitHubDeliveryAgent
from agents.pull_request_agent import PullRequestAgent
from agents.jira_delivery_agent import JiraDeliveryAgent
from agents.slack_notification_agent import SlackNotificationAgent

from tools.patch_validator import PatchValidator
from tools.file_writer import FileWriter


def main():

    print("=" * 70)
    print("AUTONOMOUS SOFTWARE ENGINEERING AGENT")
    print("=" * 70)

    planner = PlannerAgent()
    github = GitHubAgent()
    analyzer = RepositoryAnalyzer()
    indexer = IndexingAgent()
    retrieval = RetrievalAgent()
    developer = DeveloperAgent()

    coding = CodingAgent(
        provider=LLM_PROVIDER
    )

    patch_agent = PatchAgent()

    validator = PatchValidator()

    writer = FileWriter()

    reviewer = ReviewerAgent(
        provider=LLM_PROVIDER
    )

    tester = TesterAgent()

    github_delivery = GitHubDeliveryAgent()

    pull_request = PullRequestAgent()

    jira_delivery = JiraDeliveryAgent()

    slack = SlackNotificationAgent()

    try:

        # ======================================================
        # Planner
        # ======================================================

        state = planner.choose_next_story()

        if state is None:

            print()

            print("No Jira stories available.")

            return

        # ======================================================
        # Repository
        # ======================================================

        state = github.prepare_repository(
            state
        )

        slack.workflow_started(
            state
        )

        # ======================================================
        # Repository Analysis
        # ======================================================

        state = analyzer.analyze(
            state
        )

        # ======================================================
        # Repository Index
        # ======================================================

        state = indexer.build_index(
            state
        )

        # ======================================================
        # Retrieval
        # ======================================================

        state = retrieval.retrieve(
            state
        )

        # ======================================================
        # Developer
        # ======================================================

        state = developer.prepare_task(
            state
        )

    

        # ======================================================
        # Coding
        # ======================================================

        state = coding.generate(
            state
        )


    
            # ======================================================
        # Patch Generation
        # ======================================================

        state = patch_agent.generate_patch(
            state
        )

        patch_agent.print_summary(
            state.patch
        )

        # ======================================================
        # Patch Validation
        # ======================================================

        valid, errors = validator.validate(
            state.patch
        )

        validator.print_report(
            valid,
            errors,
        )

        if not valid:

            print()

            print(
                "Patch validation failed."
            )

            print(
                "Repository was not modified."
            )

            slack.workflow_failed(
                state,
                "Patch validation failed.",
            )

            return

        # ======================================================
        # Apply Patch
        # ======================================================

        writer.apply_patch(
            state.patch
        )

        print()

        print(
            "Patch successfully applied."
        )

        # ======================================================
        # Reviewer
        # ======================================================

        state = reviewer.review(
            state
        )

        reviewer.print_summary(
            state
        )

        if not getattr(
            state,
            "review_passed",
            False,
        ):

            print()

            print(
                 "WARNING: Reviewer rejected the implementation."
            )

            print(
                "Continuing workflow for testing purposes..."
           )

        # ======================================================
        # Testing
        # ======================================================

        state = tester.run_tests(
            state
        )

        tester.print_summary(
            state
        )

        slack.tests_completed(
            state
        )

        if not getattr(
            state,
            "tests_passed",
            False,
        ):

            print()

            print(
                "Tests failed."
            )

            slack.workflow_failed(
                state,
                "Automated tests failed.",
            )

            return
        
                # ======================================================
        # GitHub Delivery
        # ======================================================

        state = github_delivery.deliver(
            state
        )

        github_delivery.print_summary(
            state
        )

        # ======================================================
        # Pull Request
        # ======================================================

        state = pull_request.create_pull_request(
            state
        )

        pull_request.print_summary(
            state
        )

        pull_request.add_comment(

            state,

            (
                "🤖 Pull Request automatically generated by "
                "the Autonomous Software Engineering Agent."
            ),

        )

        slack.pull_request_created(
            state
        )

        # ======================================================
        # Jira Delivery
        # ======================================================

        state = jira_delivery.complete_story(
            state
        )

        jira_delivery.print_summary(
            state
        )

        slack.jira_completed(
            state
        )

        # ======================================================
        # Workflow Completed
        # ======================================================

        slack.workflow_completed(
            state
        )

        planner.print_selected_story(
            state
        )

        print()

        print("=" * 70)
        print("WORKFLOW SUMMARY")
        print("=" * 70)

        print(
            f"Issue               : {state.issue_key}"
        )

        print(
            f"Summary             : {state.summary}"
        )

        print(
            f"Repository          : {state.repository}"
        )

        print(
            f"Branch              : {state.feature_branch}"
        )

        print(
            f"Language            : {state.language}"
        )

        print(
            f"Framework           : {state.framework}"
        )

        print(
            f"Entry Point         : {state.entry_point}"
        )

        print(
            f"Source Files        : {len(state.source_files)}"
        )

        print(
            f"Indexed Symbols     : {len(state.symbols)}"
        )

        print(
            f"Relevant Symbols    : {len(state.relevant_symbols)}"
        )

        print(
            f"Review Passed       : {state.review_passed}"
        )

        print(
            f"Tests Passed        : {state.tests_passed}"
        )

        print(
            f"Repository Delivered: {getattr(state, 'delivery_completed', False)}"
        )

        print(
            f"Pull Request        : {getattr(state, 'pull_request_url', 'Not Created')}"
        )

        print(
            f"Jira Completed      : {getattr(state, 'jira_completed', False)}"
        )

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

        print(
            "Autonomous workflow completed successfully."
        )

        print("=" * 70)

    except Exception as ex:

        print()

        print("=" * 70)
        print("WORKFLOW FAILED")
        print("=" * 70)

        print(ex)

        try:

            slack.workflow_failed(

                state,

                str(ex),

            )

        except Exception:

            pass

        raise


if __name__ == "__main__":

    main()