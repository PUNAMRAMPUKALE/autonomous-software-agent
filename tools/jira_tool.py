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
            basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN),
        )

    def get_todo_issues(self):

        jql = f'project={PROJECT_KEY} AND status="To Do" ORDER BY created ASC'

        return self.client.search_issues(jql)

    def get_issue(self, issue_key):

        return self.client.issue(issue_key)

    def print_issue(self, issue):

        print("=" * 60)

        print("Issue :", issue.key)
        print("Summary :", issue.fields.summary)

        print()

        print("Description")

        print()

        print(issue.fields.description)

        print("=" * 60)