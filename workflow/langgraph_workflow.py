"""
workflow/langgraph_workflow.py

Milestone 10
End-to-End Autonomous Workflow
"""

from langgraph.graph import StateGraph, END

from state import AgentState

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

from tools.patch_validator import PatchValidator
from tools.file_writer import FileWriter
from tools.github_tool import GitHubTool
from tools.jira_tool import JiraTool
from tools.slack_tool import SlackTool
from agents.reviewer_agent import ReviewerAgent


class AutonomousWorkflow:

    def __init__(self, provider="openai"):

        self.provider = provider

        self.planner = PlannerAgent()

        self.github = GitHubAgent()

        self.analyzer = RepositoryAnalyzer()

        self.indexer = IndexingAgent()

        self.retrieval = RetrievalAgent()

        self.developer = DeveloperAgent()

        self.coding = CodingAgent(
            provider=provider,
        )

        self.patch = PatchAgent()

        self.validator = PatchValidator()

        self.writer = FileWriter()

        self.reviewer = ReviewerAgent(
            provider=provider,
        )

        self.tester = TesterAgent()

        graph = StateGraph(AgentState)

        graph.add_node(
            "planner",
            self.run_planner,
        )

        graph.add_node(
            "github",
            self.run_github,
        )

        graph.add_node(
            "analyzer",
            self.run_analyzer,
        )

        graph.add_node(
            "indexer",
            self.run_indexer,
        )

        graph.add_node(
            "retrieval",
            self.run_retrieval,
        )

        graph.add_node(
            "developer",
            self.run_developer,
        )

        graph.add_node(
            "coding",
            self.run_coding,
        )

        graph.add_node(
            "patch",
            self.run_patch,
        )

        graph.add_node(
            "review",
            self.run_review,
        )

        graph.add_node(
            "test",
            self.run_tests,
        )

        graph.add_node(
            "finish",
            self.finish_workflow,
        )

        graph.set_entry_point(
            "planner"
        )

        graph.add_edge(
            "planner",
            "github",
        )

        graph.add_edge(
            "github",
            "analyzer",
        )

        graph.add_edge(
            "analyzer",
            "indexer",
        )

        graph.add_edge(
            "indexer",
            "retrieval",
        )

        graph.add_edge(
            "retrieval",
            "developer",
        )

        graph.add_edge(
            "developer",
            "coding",
        )

        graph.add_edge(
            "coding",
            "patch",
        )

        graph.add_edge(
            "patch",
            "review",
        )

        graph.add_edge(
            "review",
            "test",
        )

        graph.add_edge(
            "test",
            "finish",
        )

        graph.add_edge(
            "finish",
            END,
        )

        self.workflow = graph.compile()

    # -----------------------------------------------------

    def run_planner(self, state):

        return self.planner.choose_next_story()

    def run_github(self, state):

        return self.github.prepare_repository(
            state
        )

    def run_analyzer(self, state):

        return self.analyzer.analyze(
            state
        )

    def run_indexer(self, state):

        return self.indexer.build_index(
            state
        )

    def run_retrieval(self, state):

        return self.retrieval.retrieve(
            state
        )

    def run_developer(self, state):

        return self.developer.prepare_task(
            state
        )

    def run_coding(self, state):

        return self.coding.generate(
            state
        )

    def run_patch(self, state):

        state = self.patch.generate_patch(
            state
        )

        if state.patch:

            valid, errors = self.validator.validate(
                state.patch
            )

            self.validator.print_report(
                valid,
                errors,
            )

            if valid:

                self.writer.apply_patch(
                    state.patch
                )

        return state

    def run_review(self, state):

        return self.reviewer.review(
            state
        )

    def run_tests(self, state):

        return self.tester.run_tests(
            state
        )

    def finish_workflow(self, state):

        print()

        print("=" * 70)
        print("AUTONOMOUS DELIVERY")
        print("=" * 70)

        if not getattr(
            state,
            "tests_passed",
            False,
        ):

            print(
                "Tests failed. Deployment cancelled."
            )

            return state

        github = GitHubTool(
            state.repository_path
        )

        github.commit_and_push(

            f"{state.issue_key}: {state.summary}"

        )

        jira = JiraTool()

        jira.move_issue(

            state.issue_key,

            "Done",

        )

        try:

            slack = SlackTool()

            slack.send_message(

                f"✅ {state.issue_key} completed successfully."

            )

        except Exception:

            print(
                "Slack notification skipped."
            )

        print()

        print(
            "Workflow completed successfully."
        )

        print("=" * 70)

        return state

    def run(self):

        return self.workflow.invoke(
            AgentState()
        )