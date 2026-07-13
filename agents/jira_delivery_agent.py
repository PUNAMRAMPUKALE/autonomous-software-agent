"""
agents/jira_delivery_agent.py

Milestone 10

Responsible for:

- Move Jira Issue to Done
- Add Development Comment
- Record Test Results
- Attach Pull Request
- Add Completion Notes
"""

from tools.jira_tool import JiraTool


class JiraDeliveryAgent:

    def __init__(self):

        self.jira = JiraTool()

    # ---------------------------------------------------------
    # Complete Jira Story
    # ---------------------------------------------------------

    def complete_story(
        self,
        state,
    ):

        print()

        print("=" * 70)
        print("JIRA DELIVERY AGENT")
        print("=" * 70)

        issue_key = state.issue_key

        #
        # Development Comment
        #

        self.jira.add_comment(

            issue_key,

            (
                "🤖 Autonomous Software Engineering Agent "
                "completed the implementation."
            ),

        )

        #
        # Pull Request
        #

        if getattr(
            state,
            "pull_request_url",
            None,
        ):

            self.jira.add_pr_link(

                issue_key,

                state.repository,

                state.feature_branch,

                str(
                    state.pull_request_number
                ),

            )

        #
        # Test Results
        #

        self.jira.record_test_results(

            issue_key,

            getattr(
                state,
                "tests_passed",
                False,
            ),

            getattr(
                state,
                "test_output",
                "",
            ),

        )

        #
        # Completion Notes
        #

        completion_notes = f"""
Implementation Completed

Issue          : {state.issue_key}
Summary        : {state.summary}
Branch         : {state.feature_branch}
Repository     : {state.repository}

Patch Applied  : {"Yes" if state.patch else "No"}

Tests Passed   : {
    getattr(
        state,
        "tests_passed",
        False,
    )
}

Pull Request

{
    getattr(
        state,
        "pull_request_url",
        "Not Available",
    )
}
"""

        self.jira.update_completion_notes(

            issue_key,

            completion_notes,

        )

        #
        # Transition to Done
        #

        self.jira.move_issue(

            issue_key,

            "Done",

        )

        state.jira_completed = True

        print()

        print(
            f"{issue_key} moved to Done."
        )

        print("=" * 70)

        return state

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    def print_summary(
        self,
        state,
    ):

        print()

        print("=" * 70)
        print("JIRA DELIVERY SUMMARY")
        print("=" * 70)

        print(
            "Completed :",
            getattr(
                state,
                "jira_completed",
                False,
            ),
        )

        print("=" * 70)