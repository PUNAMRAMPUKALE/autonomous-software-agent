from jira import JIRA
from config import JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN


class JiraTool:

    def __init__(self):
        self.client = JIRA(
            server=JIRA_URL,
            basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN)
        )

    def read_story(self, issue_key):

        issue = self.client.issue(issue_key)

        print("=" * 50)
        print("Issue :", issue.key)
        print("Summary :", issue.fields.summary)

        print("\nDescription\n")

        print(issue.fields.description)

        print("=" * 50)

        return issue