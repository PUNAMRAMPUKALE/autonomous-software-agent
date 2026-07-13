from dataclasses import dataclass, field

from models.symbol import Symbol


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

    language: str = ""

    framework: str = ""

    test_framework: str = ""

    entry_point: str = ""

    readme: bool = False

    project_structure: list = field(default_factory=list)

    implementation_plan: list = field(default_factory=list)

    source_files: list = field(default_factory=list)

    context: str = ""

    llm_prompt: str = ""

    symbols: list[Symbol] = field(default_factory=list)