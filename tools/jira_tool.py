from jira import JIRA

from config import (
    JIRA_URL,
    JIRA_EMAIL,
    JIRA_API_TOKEN,
    PROJECT_KEY,
)


class JiraTool:

    def __init__(self):

        self.client = JIRA(
            server=JIRA_URL,
            basic_auth=(
                JIRA_EMAIL,
                JIRA_API_TOKEN,
            ),
        )

    # ---------------------------------------------------------
    # Read Issues
    # ---------------------------------------------------------

    def get_todo_issues(self):

        jql = (
            f'project="{PROJECT_KEY}" '
            'AND status="To Do" '
            "ORDER BY created ASC"
        )

        return self.client.search_issues(jql)

    def get_issue(
        self,
        issue_key,
    ):

        return self.client.issue(issue_key)

    # ---------------------------------------------------------
    # Print
    # ---------------------------------------------------------

    def print_issue(
        self,
        issue,
    ):

        print("=" * 60)
        print("Issue :", issue.key)
        print("Summary :", issue.fields.summary)
        print()
        print("Status :", issue.fields.status.name)
        print()
        print("Description")
        print()
        print(issue.fields.description)
        print("=" * 60)

    # ---------------------------------------------------------
    # Workflow Transition
    # ---------------------------------------------------------

    def get_transition_id(
        self,
        issue,
        transition_name,
    ):

        transitions = self.client.transitions(
            issue
        )

        for transition in transitions:

            if (
                transition["name"].lower()
                ==
                transition_name.lower()
            ):

                return transition["id"]

        return None

    def move_issue(
        self,
        issue_key,
        transition_name,
    ):

        issue = self.get_issue(
            issue_key
        )

        transition_id = self.get_transition_id(
            issue,
            transition_name,
        )

        if transition_id is None:

            raise Exception(
                f"Transition '{transition_name}' not found."
            )

        self.client.transition_issue(
            issue,
            transition_id,
        )

        print(
            f"Moved {issue_key} -> {transition_name}"
        )

    # ---------------------------------------------------------
    # Add Comment
    # ---------------------------------------------------------

    def add_comment(
        self,
        issue_key,
        comment,
    ):

        self.client.add_comment(
            issue_key,
            comment,
        )

        print(
            f"Comment added to {issue_key}"
        )

    # ---------------------------------------------------------
    # Attach Pull Request
    # ---------------------------------------------------------

    def add_pr_link(
        self,
        issue_key,
        repository,
        branch,
        pr_number,
    ):

        comment = f"""
Pull Request Created

Repository : {repository}

Branch : {branch}

PR Number : {pr_number}
"""

        self.add_comment(
            issue_key,
            comment,
        )

    # ---------------------------------------------------------
    # Test Results
    # ---------------------------------------------------------

    def record_test_results(
        self,
        issue_key,
        passed,
        output,
    ):

        status = (
            "PASSED"
            if passed
            else
            "FAILED"
        )

        comment = f"""
Test Results

Status : {status}

Output

{output}
"""

        self.add_comment(
            issue_key,
            comment,
        )

    # ---------------------------------------------------------
    # Completion Notes
    # ---------------------------------------------------------

    def update_completion_notes(
        self,
        issue_key,
        notes,
    ):

        comment = f"""
Completion Notes

{notes}
"""

        self.add_comment(
            issue_key,
            comment,
        )