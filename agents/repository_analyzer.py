import os


class RepositoryAnalyzer:

    def analyze(self, state):

        repo = state.local_path

        print("\n========== Repository Analyzer ==========\n")

        state.language = self.detect_language(repo)
        state.framework = self.detect_framework(repo)
        state.entry_point = self.find_entry_point(repo)
        state.test_framework = self.detect_test_framework(repo)
        state.readme = self.find_readme(repo)
        state.project_structure = self.project_structure(repo)
        state.implementation_plan = self.create_plan(state)

        return state

    # -----------------------------------------------------
    # Language Detection
    # -----------------------------------------------------

    def detect_language(self, repo):

        for root, _, files in os.walk(repo):

            if "requirements.txt" in files:
                return "Python"

            if "pyproject.toml" in files:
                return "Python"

            if "package.json" in files:
                return "JavaScript"

            if "pom.xml" in files:
                return "Java"

            if "build.gradle" in files:
                return "Java"

            if "Cargo.toml" in files:
                return "Rust"

            if "go.mod" in files:
                return "Go"

            if any(file.endswith(".py") for file in files):
                return "Python"

            if any(file.endswith(".js") for file in files):
                return "JavaScript"

            if any(file.endswith(".ts") for file in files):
                return "TypeScript"

            if any(file.endswith(".java") for file in files):
                return "Java"

            if any(file.endswith(".cs") for file in files):
                return ".NET"

        return "Unknown"

    # -----------------------------------------------------
    # Framework Detection
    # -----------------------------------------------------

    def detect_framework(self, repo):

        requirements = self.read_file(repo, "requirements.txt")
        package = self.read_file(repo, "package.json")
        pom = self.read_file(repo, "pom.xml")

        if "fastapi" in requirements.lower():
            return "FastAPI"

        if "flask" in requirements.lower():
            return "Flask"

        if "django" in requirements.lower():
            return "Django"

        if "spring-boot" in pom.lower():
            return "Spring Boot"

        if '"react"' in package.lower():
            return "React"

        if '"next"' in package.lower():
            return "Next.js"

        if '"express"' in package.lower():
            return "Express"

        if self.detect_language(repo) == "Python":
            return "Custom Python"

        return "Unknown"

    # -----------------------------------------------------
    # Test Framework Detection
    # -----------------------------------------------------

    def detect_test_framework(self, repo):

        for root, _, files in os.walk(repo):

            if "pytest.ini" in files:
                return "pytest"

            if "tox.ini" in files:
                return "pytest"

            if "jest.config.js" in files:
                return "Jest"

            if "vitest.config.ts" in files:
                return "Vitest"

            if any(file.startswith("test_") for file in files):
                return "pytest"

            if any(file.endswith(".spec.js") for file in files):
                return "Jest"

            if any(file.endswith(".test.js") for file in files):
                return "Jest"

        return "Not Configured"

    # -----------------------------------------------------
    # Entry Point
    # -----------------------------------------------------

    def find_entry_point(self, repo):

        candidates = [
            "main.py",
            "app.py",
            "server.py",
            "manage.py",
            "index.js",
            "server.js",
            "main.go",
            "Program.cs",
        ]

        for candidate in candidates:

            if os.path.exists(os.path.join(repo, candidate)):
                return candidate

        return "Unknown"

    # -----------------------------------------------------
    # README Detection
    # -----------------------------------------------------

    def find_readme(self, repo):

        for filename in [
            "README.md",
            "README.MD",
            "README",
        ]:

            if os.path.exists(os.path.join(repo, filename)):
                return True

        return False

    # -----------------------------------------------------
    # Project Structure
    # -----------------------------------------------------

    def project_structure(self, repo):

        ignore = {
            ".git",
            ".venv",
            "__pycache__",
            ".idea",
            ".vscode",
            "workspace",
            "node_modules",
        }

        folders = []

        for item in sorted(os.listdir(repo)):

            full = os.path.join(repo, item)

            if os.path.isdir(full) and item not in ignore:
                folders.append(item)

        return folders

    # -----------------------------------------------------
    # Helper
    # -----------------------------------------------------

    def read_file(self, repo, filename):

        for root, _, files in os.walk(repo):

            if filename in files:

                path = os.path.join(root, filename)

                try:

                    with open(path, "r", encoding="utf-8") as file:
                        return file.read()

                except Exception:
                    return ""

        return ""

    # -----------------------------------------------------
    # Implementation Plan
    # -----------------------------------------------------

    def create_plan(self, state):

        plan = [
            "Analyze Jira requirements.",
            "Index repository symbols.",
            "Identify affected classes and functions.",
            "Prepare developer context.",
            "Generate implementation.",
        ]

        if state.test_framework != "Not Configured":
            plan.append(
                f"Run {state.test_framework}."
            )

        plan.extend([
            "Review generated code.",
            "Commit changes.",
        ])

        return plan