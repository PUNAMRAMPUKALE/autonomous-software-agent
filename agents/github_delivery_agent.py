"""
agents/github_delivery_agent.py

Milestone 10

Responsible for:

- Git Add
- Git Commit
- Git Push

This agent executes after tests have passed.
"""

from tools.git_operations import GitOperations


class GitHubDeliveryAgent:

    def __init__(self):
        pass

    # ---------------------------------------------------------
    # Deliver Changes
    # ---------------------------------------------------------

    def deliver(
        self,
        state,
    ):

        print()

        print("=" * 70)
        print("GITHUB DELIVERY AGENT")
        print("=" * 70)

        if state.patch is None:

            print(
                "No patch available."
            )

            return state

        if not getattr(
            state,
            "tests_passed",
            True,
        ):

            print(
                "Tests failed."
            )

            print(
                "Skipping commit."
            )

            return state

        git = GitOperations(
            state.local_path
        )

        commit_message = (
            f"{state.issue_key}: {state.summary}"
        )

        git.commit_and_push(
            commit_message
        )

        state.delivery_completed = True

        print()

        print(
            "Repository delivery completed."
        )

        print("=" * 70)

        return state

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    def print_summary(
        self,
        state,
    ):

        print()

        print("=" * 70)
        print("DELIVERY SUMMARY")
        print("=" * 70)

        print(
            "Delivered :",
            getattr(
                state,
                "delivery_completed",
                False,
            ),
        )

        print("=" * 70)