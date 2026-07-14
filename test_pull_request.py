from state import AgentState
from agents.pull_request_agent import PullRequestAgent

state = AgentState()

state.delivery_completed = True

state.repository = "https://github.com/PUNAMRAMPUKALE/autonomous-software-agent"

state.issue_key = "KAN-999"

state.summary = "Testing PR"

state.feature_branch = "feature/kan-999"

state.branch = "main"

agent = PullRequestAgent()

state = agent.create_pull_request(state)

agent.print_summary(state)