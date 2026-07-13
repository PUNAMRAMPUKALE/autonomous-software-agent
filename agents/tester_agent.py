"""
agents/tester_agent.py

Milestone 10
Tester Agent

Runs project validation after generated patches are applied.
"""

import os
import subprocess


class TesterAgent:

    def __init__(self):

        self.commands = [

            ["pytest"],

            ["python", "-m", "pytest"],

            ["python", "-m", "unittest"],

        ]

    # ---------------------------------------------------------

    def run_tests(
        self,
        state,
    ):

        print()

        print("=" * 70)
        print("TESTER AGENT")
        print("=" * 70)

        repository = getattr(
            state,
            "repository_path",
            None,
        )

        if repository is None:

            repository = getattr(
                state,
                "repo_path",
                None,
            )

        if repository is None:

            print(
                "Repository path not found."
            )

            state.tests_passed = False

            return state

        for command in self.commands:

            try:

                result = subprocess.run(

                    command,

                    cwd=repository,

                    capture_output=True,

                    text=True,

                    timeout=300,

                )

                print()

                print(
                    "Command :",
                    " ".join(command),
                )

                print(
                    "Return Code :",
                    result.returncode,
                )

                if result.stdout:

                    print()

                    print(result.stdout)

                if result.stderr:

                    print()

                    print(result.stderr)

                if result.returncode == 0:

                    print()

                    print(
                        "Tests passed."
                    )

                    state.tests_passed = True

                    state.test_command = " ".join(
                        command
                    )

                    return state

            except FileNotFoundError:

                continue

            except subprocess.TimeoutExpired:

                print()

                print(
                    "Tests timed out."
                )

                break

            except Exception as ex:

                print(ex)

                break

        state.tests_passed = False

        return state

    # ---------------------------------------------------------

    def print_summary(
        self,
        state,
    ):

        print()

        print("=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)

        print(
            "Passed :",
            getattr(
                state,
                "tests_passed",
                False,
            ),
        )

        if hasattr(
            state,
            "test_command",
        ):

            print(
                "Command :",
                state.test_command,
            )

        print("=" * 70)