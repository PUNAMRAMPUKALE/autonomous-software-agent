from dataclasses import dataclass


@dataclass
class AgentState:

    issue_key: str = ""

    summary: str = ""

    description: str = ""

    status: str = ""