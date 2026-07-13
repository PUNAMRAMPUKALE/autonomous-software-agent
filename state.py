from dataclasses import dataclass


@dataclass
class AgentState:

    issue_key: str = ""

    project_key: str = ""

    summary: str = ""

    description: str = ""

    status: str = ""

    repository: str = ""

    branch: str = ""

    local_path: str = ""

    feature_branch: str = ""