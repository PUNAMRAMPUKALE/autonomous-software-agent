from config import PROJECT_REPOSITORIES
from tools.github_tool import GitHubTool


class GitHubAgent:

    def __init__(self):

        self.github = GitHubTool()

    def prepare_repository(self, state):

        config = PROJECT_REPOSITORIES.get(
            state.project_key
        )

        if config is None:
            raise Exception(
                f"No repository configured for project {state.project_key}"
            )

        state.repository = config["repository"]
        state.branch = config["branch"]

        repo_path = self.github.clone_repository(
            state.repository
        )

        state.local_path = repo_path

        self.github.checkout_branch(
            repo_path,
            state.branch,
        )

        state.feature_branch = (
            self.github.create_feature_branch(
                repo_path,
                state.issue_key,
            )
        )

        return state