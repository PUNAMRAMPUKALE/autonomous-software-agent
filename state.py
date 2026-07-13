from dataclasses import dataclass, field

from models.symbol import Symbol

from tools.code_patch import CodePatch


@dataclass
class AgentState:

    # --------------------------------------------------
    # Jira
    # --------------------------------------------------

    issue_key: str = ""

    project_key: str = ""

    summary: str = ""

    description: str = ""

    status: str = ""
    
    patch: CodePatch | None = None

    # --------------------------------------------------
    # Repository
    # --------------------------------------------------

    repository: str = ""

    branch: str = ""

    local_path: str = ""

    feature_branch: str = ""

    # --------------------------------------------------
    # Repository Analysis
    # --------------------------------------------------

    language: str = ""

    framework: str = ""

    test_framework: str = ""

    entry_point: str = ""

    readme: bool = False

    project_structure: list = field(
        default_factory=list
    )

    implementation_plan: list = field(
        default_factory=list
    )

    # --------------------------------------------------
    # Files
    # --------------------------------------------------

    source_files: list = field(
        default_factory=list
    )

    context: str = ""

    llm_prompt: str = ""
    
    generated_code: str = ""

    # --------------------------------------------------
    # Repository Index
    # --------------------------------------------------

    symbols: list[Symbol] = field(
        default_factory=list
    )

    repository_graph = None

    relevant_symbols: list[Symbol] = field(
        default_factory=list
    )