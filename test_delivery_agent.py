from state import AgentState
from agents.github_delivery_agent import GitHubDeliveryAgent

state = AgentState()

state.local_path = r"C:\Users\punam\autonomous-software-agent"

state.issue_key = "KAN-999"

state.summary = "Delivery Agent Test"

state.tests_passed = True

state.patch = object()

agent = GitHubDeliveryAgent()

agent.deliver(state)

agent.print_summary(state)