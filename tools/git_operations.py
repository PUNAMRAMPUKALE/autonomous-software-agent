"""
tools/git_operations.py

Milestone 10
Git Operations Tool

Responsible for:
- git status
- git add
- git commit
- git push

This tool does NOT clone repositories.
That responsibility remains in GitHubTool.
"""

import subprocess


class GitOperations:

    def __init__(self, repository_path):

        self.repository_path = repository_path

    # ---------------------------------------------------------
    # Execute Git Command
    # ---------------------------------------------------------

    def _run(self, command):

        result = subprocess.run(
            command,
            cwd=self.repository_path,
            capture_output=True,
            text=True,
        )

        return result

    # ---------------------------------------------------------
    # Git Status
    # ---------------------------------------------------------

    def status(self):

        result = self._run(
            [
                "git",
                "status",
                "--short",
            ]
        )

        print(result.stdout)

        return result.returncode == 0

    # ---------------------------------------------------------
    # Stage Changes
    # ---------------------------------------------------------

    def add_all(self):

        print()

        print("Staging files...")

        result = self._run(
            [
                "git",
                "add",
                ".",
            ]
        )

        if result.returncode != 0:

            raise Exception(result.stderr)

        print("Files staged successfully.")

    # ---------------------------------------------------------
    # Commit Changes
    # ---------------------------------------------------------

    def commit(self, message):

        print()

        print("Creating commit...")

        result = self._run(
            [
                "git",
                "commit",
                "-m",
                message,
            ]
        )

        if result.returncode != 0:

            stdout = result.stdout.lower()
            stderr = result.stderr.lower()

            if (
                "nothing to commit" in stdout
                or "nothing to commit" in stderr
            ):

                print("Nothing to commit.")

                return False

            raise Exception(result.stderr)

        print(result.stdout)

        return True

    # ---------------------------------------------------------
    # Push Branch
    # ---------------------------------------------------------

    def push(self, remote="origin", branch=None):

        if branch is None:

            branch_result = self._run(
                [
                    "git",
                    "branch",
                    "--show-current",
                ]
            )

            branch = branch_result.stdout.strip()

        print()

        print(f"Pushing {branch}...")

        result = self._run(
            [
                "git",
                "push",
                remote,
                branch,
            ]
        )

        if result.returncode != 0:

            raise Exception(result.stderr)

        print(result.stdout)

        return True

    # ---------------------------------------------------------
    # Complete Git Workflow
    # ---------------------------------------------------------

    def commit_and_push(
        self,
        commit_message,
    ):

        print()

        print("=" * 70)
        print("GIT OPERATIONS")
        print("=" * 70)

        self.status()

        self.add_all()

        committed = self.commit(
            commit_message
        )

        if committed:

            self.push()

            print()

            print("Repository pushed successfully.")

        print("=" * 70)