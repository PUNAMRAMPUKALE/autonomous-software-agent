"""
agents/slack_notification_agent.py

Milestone 10

Slack Notification Agent

Responsibilities
----------------
- Notify workflow started
- Notify tests completed
- Notify Pull Request created
- Notify Jira completed
- Notify workflow completed
"""

from tools.slack_tool import SlackTool


class SlackNotificationAgent:

    def __init__(self):

        self.slack = SlackTool()

    # ---------------------------------------------------------
    # Send Message
    # ---------------------------------------------------------

    def send(
        self,
        message,
    ):

        try:

            self.slack.send_message(
                message
            )

        except Exception as ex:

            print()

            print(
                f"Slack notification failed: {ex}"
            )

    # ---------------------------------------------------------
    # Workflow Started
    # ---------------------------------------------------------

    def workflow_started(
        self,
        state,
    ):

        message = f"""
🚀 Autonomous Software Engineering Agent Started

Issue      : {state.issue_key}
Summary    : {state.summary}
Repository : {state.repository}
Branch     : {state.feature_branch}
"""

        self.send(message)

    # ---------------------------------------------------------
    # Tests Finished
    # ---------------------------------------------------------

    def tests_completed(
        self,
        state,
    ):

        passed = getattr(
            state,
            "tests_passed",
            False,
        )

        emoji = "✅" if passed else "❌"

        message = f"""
{emoji} Test Execution Completed

Issue : {state.issue_key}

Passed : {passed}

Output

{getattr(state, "test_output", "No Output")}
"""

        self.send(message)

    # ---------------------------------------------------------
    # Pull Request Created
    # ---------------------------------------------------------

    def pull_request_created(
        self,
        state,
    ):

        if not getattr(
            state,
            "pull_request_url",
            None,
        ):

            return

        message = f"""
🔀 Pull Request Created

Issue : {state.issue_key}

PR

{state.pull_request_url}
"""

        self.send(message)

    # ---------------------------------------------------------
    # Jira Updated
    # ---------------------------------------------------------

    def jira_completed(
        self,
        state,
    ):

        message = f"""
📋 Jira Story Completed

Issue : {state.issue_key}

Status : Done
"""

        self.send(message)

    # ---------------------------------------------------------
    # Workflow Completed
    # ---------------------------------------------------------

    def workflow_completed(
        self,
        state,
    ):

        message = f"""
🎉 Autonomous Workflow Completed

Issue : {state.issue_key}

Summary : {state.summary}

Repository : {state.repository}

Branch : {state.feature_branch}

Pull Request

{getattr(state, "pull_request_url", "Not Created")}

Tests Passed

{getattr(state, "tests_passed", False)}
"""

        self.send(message)

    # ---------------------------------------------------------
    # Workflow Failed
    # ---------------------------------------------------------

    def workflow_failed(
        self,
        state,
        reason,
    ):

        message = f"""
❌ Autonomous Workflow Failed

Issue : {state.issue_key}

Reason

{reason}
"""

        self.send(message)

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    def print_summary(
        self,
    ):

        print()

        print("=" * 70)
        print("SLACK NOTIFICATION AGENT")
        print("=" * 70)

        print(
            "Slack notifications dispatched."
        )

        print("=" * 70)