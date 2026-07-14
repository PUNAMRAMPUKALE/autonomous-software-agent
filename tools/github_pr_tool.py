"""
tools/github_pr_tool.py

Milestone 10

GitHub Pull Request Tool
"""

import os

from dotenv import load_dotenv
from github import Github

# Load .env
load_dotenv()


class GitHubPRTool:

    def __init__(self):

        token = os.getenv("GITHUB_TOKEN")

        if not token:

            raise ValueError(
                "GITHUB_TOKEN not configured."
            )

        self.github = Github(token)

    # ---------------------------------------------------------
    # Get Repository
    # ---------------------------------------------------------

    def get_repository(
        self,
        repository_url,
    ):

        repository = (
            repository_url
            .replace(
                "https://github.com/",
                "",
            )
            .replace(
                ".git",
                "",
            )
            .strip("/")
        )

        return self.github.get_repo(
            repository
        )

    # ---------------------------------------------------------
    # Create Pull Request
    # ---------------------------------------------------------

    def create_pull_request(
        self,
        repository_url,
        title,
        body,
        head_branch,
        base_branch="main",
    ):

        print()

        print("=" * 70)
        print("CREATE PULL REQUEST")
        print("=" * 70)

        repo = self.get_repository(
            repository_url
        )

        pr = repo.create_pull(
            title=title,
            body=body,
            head=head_branch,
            base=base_branch,
        )

        print()

        print(f"PR Created : #{pr.number}")
        print(pr.html_url)

        print("=" * 70)

        return pr

    # ---------------------------------------------------------
    # Add Comment
    # ---------------------------------------------------------

    def add_comment(
        self,
        repository_url,
        pr_number,
        comment,
    ):

        repo = self.get_repository(
            repository_url
        )

        pr = repo.get_pull(
            pr_number
        )

        pr.create_issue_comment(
            comment
        )

        print("Comment added to Pull Request.")

    # ---------------------------------------------------------
    # Get Pull Request
    # ---------------------------------------------------------

    def get_pull_request(
        self,
        repository_url,
        pr_number,
    ):

        repo = self.get_repository(
            repository_url
        )

        return repo.get_pull(
            pr_number
        )