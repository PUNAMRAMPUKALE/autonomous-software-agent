"""
agents/tester_agent.py

Milestone 10

Tester Agent

Responsibilities
----------------
1. Detect project type.
2. Execute project test suite.
3. Capture test output.
4. Store results in AgentState.
5. Return updated state.
"""

import os
import subprocess


class TesterAgent:

    def __init__(self):

        self.timeout = 600

    # ---------------------------------------------------------
    # Main
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
            "local_path",
            "",
        )

        if not repository:

            repository = getattr(
                state,
                "repository_path",
                "",
            )

        if not repository:

            print(
                "Repository path not available."
            )

            state.tests_passed = False

            state.test_output = (
                "Repository path missing."
            )

            return state

        commands = self.detect_test_commands(
            repository
        )

        if not commands:

            print(
                "No supported test framework detected."
            )

            state.tests_passed = True

            state.test_output = (
                "No tests detected."
            )

            return state

        for command in commands:

            print()

            print(
                "Running:",
                " ".join(command),
            )

            try:

                result = subprocess.run(

                    command,

                    cwd=repository,

                    capture_output=True,

                    text=True,

                    timeout=self.timeout,

                )

                output = (
                    result.stdout
                    + "\n"
                    + result.stderr
                )

                state.test_command = (
                    " ".join(command)
                )

                state.test_output = output

                print(output)

                if result.returncode == 0:

                    print()

                    print(
                        "Tests passed."
                    )

                    state.tests_passed = True

                    return state

                print()

                print(
                    "Tests failed."
                )

            except FileNotFoundError:

                print()

                print(
                    f"Command not found: {' '.join(command)}"
                )

            except subprocess.TimeoutExpired:

                print()

                print(
                    "Test execution timed out."
                )

                state.tests_passed = False

                state.test_output = (
                    "Tests timed out."
                )

                return state

            except Exception as ex:

                print(ex)

                state.tests_passed = False

                state.test_output = str(ex)

                return state

        state.tests_passed = False

        return state

    # ---------------------------------------------------------
    # Detect Test Framework
    # ---------------------------------------------------------

    def detect_test_commands(
        self,
        repository,
    ):

        commands = []

        #
        # Python
        #

        if os.path.exists(

            os.path.join(
                repository,
                "pytest.ini",
            )

        ):

            commands.append(
                [
                    "pytest",
                ]
            )

        if os.path.exists(

            os.path.join(
                repository,
                "requirements.txt",
            )

        ):

            commands.append(
                [
                    "python",
                    "-m",
                    "pytest",
                ]
            )

        #
        # Node
        #

        if os.path.exists(

            os.path.join(
                repository,
                "package.json",
            )

        ):

            commands.append(
                [
                    "npm",
                    "test",
                ]
            )

        #
        # Maven
        #

        if os.path.exists(

            os.path.join(
                repository,
                "pom.xml",
            )

        ):

            commands.append(
                [
                    "mvn",
                    "test",
                ]
            )

        #
        # Gradle
        #

        if os.path.exists(

            os.path.join(
                repository,
                "build.gradle",
            )

        ):

            commands.append(
                [
                    "gradle",
                    "test",
                ]
            )

        return commands
    
    # ---------------------------------------------------------
    # Print Summary
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
            "Tests Passed :",
            getattr(
                state,
                "tests_passed",
                False,
            ),
        )

        print(
            "Command :",
            getattr(
                state,
                "test_command",
                "Not Executed",
            ),
        )

        output = getattr(
            state,
            "test_output",
            "",
        )

        if output:

            print()

            print("Output")

            print("-" * 70)

            #
            # Prevent extremely large console output.
            #

            if len(output) > 5000:

                print(
                    output[:5000]
                )

                print()

                print(
                    "... Output Truncated ..."
                )

            else:

                print(output)

        print("=" * 70)

    # ---------------------------------------------------------
    # Test Report
    # ---------------------------------------------------------

    def generate_report(
        self,
        state,
    ):

        report = {

            "tests_passed": getattr(
                state,
                "tests_passed",
                False,
            ),

            "command": getattr(
                state,
                "test_command",
                "",
            ),

            "output": getattr(
                state,
                "test_output",
                "",
            ),

        }

        return report

    # ---------------------------------------------------------
    # Save Report
    # ---------------------------------------------------------

    def save_report(
        self,
        state,
        filename="test_report.txt",
    ):

        report = self.generate_report(
            state
        )

        repository = getattr(
            state,
            "local_path",
            "",
        )

        if not repository:

            return

        report_path = os.path.join(
            repository,
            filename,
        )

        with open(
            report_path,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(
                "=" * 70 + "\n"
            )

            file.write(
                "AUTONOMOUS TEST REPORT\n"
            )

            file.write(
                "=" * 70 + "\n\n"
            )

            file.write(
                f"Passed : {report['tests_passed']}\n\n"
            )

            file.write(
                f"Command : {report['command']}\n\n"
            )

            file.write(
                "Output\n"
            )

            file.write(
                "-" * 70 + "\n"
            )

            file.write(
                report["output"]
            )

        print()

        print(
            f"Test report saved to {report_path}"
        )    