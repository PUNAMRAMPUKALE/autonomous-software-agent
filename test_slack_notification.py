from state import AgentState
from agents.slack_notification_agent import SlackNotificationAgent

state = AgentState()

state.issue_key = "KAN-999"

state.summary = "Slack Test"

state.repository = "https://github.com/PUNAMRAMPUKALE/autonomous-software-agent"

state.feature_branch = "feature/kan-999"

state.tests_passed = True

state.pull_request_url = "https://github.com/PUNAMRAMPUKALE/autonomous-software-agent/pull/1"

agent = SlackNotificationAgent()

agent.workflow_started(state)

agent.tests_completed(state)

agent.pull_request_created(state)

agent.jira_completed(state)

agent.workflow_completed(state)

agent.print_summary()