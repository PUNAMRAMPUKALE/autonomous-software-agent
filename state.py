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

    # --------------------------------------------------
    # Repository
    # --------------------------------------------------

    repository: str = ""

    repository_path: str = ""

    local_path: str = ""

    branch: str = ""

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
    # Source Files
    # --------------------------------------------------

    source_files: list = field(
        default_factory=list
    )

    # --------------------------------------------------
    # Prompt / Context
    # --------------------------------------------------

    context: str = ""

    llm_prompt: str = ""

    generated_code: str = ""

    review: str = ""

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

    # --------------------------------------------------
    # Patch
    # --------------------------------------------------

    patch: CodePatch | None = None

    # --------------------------------------------------
    # Review
    # --------------------------------------------------

    review_passed: bool = False

    # --------------------------------------------------
    # Testing
    # --------------------------------------------------

    tests_passed: bool = False

    test_command: str = ""

    test_output: str = ""

    # --------------------------------------------------
    # Git
    # --------------------------------------------------

    commit_hash: str = ""

    commit_message: str = ""

    # --------------------------------------------------
    # Workflow
    # --------------------------------------------------

    workflow_status: str = "Pending"

    workflow_error: str = ""

    completed: bool = False