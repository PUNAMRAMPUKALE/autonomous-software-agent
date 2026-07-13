import os

from git import Repo


class GitHubTool:

    def __init__(self):

        self.workspace = os.path.join(
            os.getcwd(),
            "workspace",
        )

        os.makedirs(
            self.workspace,
            exist_ok=True,
        )

    def clone_repository(self, repository_url):

        repository_name = repository_url.split("/")[-1]

        if repository_name.endswith(".git"):
            repository_name = repository_name[:-4]

        repository_path = os.path.join(
            self.workspace,
            repository_name,
        )

        if os.path.isdir(
            os.path.join(repository_path, ".git")
        ):

            print("Repository already cloned.")

            return repository_path

        print("\nCloning Repository...")

        Repo.clone_from(
            repository_url,
            repository_path,
        )

        print("Clone completed.")

        return repository_path

    def checkout_branch(
        self,
        repository_path,
        branch_name,
    ):

        repo = Repo(repository_path)

        repo.git.checkout(branch_name)

        print(f"Checked out {branch_name}")

    def create_feature_branch(
        self,
        repository_path,
        issue_key,
    ):

        repo = Repo(repository_path)

        feature_branch = (
            f"feature/{issue_key.lower()}"
        )

        branches = [
            h.name
            for h in repo.heads
        ]

        if feature_branch in branches:

            repo.git.checkout(feature_branch)

        else:

            repo.git.checkout(
                "-b",
                feature_branch,
            )

        print(
            f"Working Branch : {feature_branch}"
        )

        return feature_branch