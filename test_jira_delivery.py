from state import AgentState
from agents.jira_delivery_agent import JiraDeliveryAgent

state = AgentState()

state.issue_key = "KAN-999"

state.summary = "Jira Delivery Test"

state.repository = "https://github.com/PUNAMRAMPUKALE/autonomous-software-agent"

state.feature_branch = "feature/kan-999"

state.pull_request_number = 1

state.pull_request_url = "https://github.com/PUNAMRAMPUKALE/autonomous-software-agent/pull/1"

state.tests_passed = True

state.test_output = "All tests passed."

state.patch = object()

agent = JiraDeliveryAgent()

state = agent.complete_story(state)

agent.print_summary(state)