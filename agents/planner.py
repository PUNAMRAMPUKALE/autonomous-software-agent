from state import AgentState
from tools.jira_tool import JiraTool


class PlannerAgent:

    def __init__(self):

        self.jira = JiraTool()

    def choose_next_story(self):

        issues = self.jira.get_todo_issues()

        if len(issues) == 0:
            print("No To Do stories found.")
            return None

        issue = issues[0]

        state = AgentState()

        state.issue_key = issue.key
        state.summary = issue.fields.summary
        state.description = issue.fields.description
        state.status = issue.fields.status.name

        return state

    def print_selected_story(self, state):

        issue = self.jira.get_issue(state.issue_key)

        self.jira.print_issue(issue)