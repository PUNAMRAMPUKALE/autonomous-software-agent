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

            if any(f.endswith(".py") for f in files):
                return "Python"

            if any(f.endswith(".js") for f in files):
                return "JavaScript"

            if any(f.endswith(".ts") for f in files):
                return "TypeScript"

            if any(f.endswith(".java") for f in files):
                return "Java"

            if any(f.endswith(".cs") for f in files):
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

        if "\"react\"" in package.lower():
            return "React"

        if "\"next\"" in package.lower():
            return "Next.js"

        if "\"express\"" in package.lower():
            return "Express"

        if self.detect_language(repo) == "Python":
            return "Custom Python"

        return "Unknown"

    # -----------------------------------------------------
    # Test Framework
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
    # README
    # -----------------------------------------------------

    def find_readme(self, repo):

        return any(

            os.path.exists(os.path.join(repo, file))

            for file in [

                "README.md",

                "README.MD",

                "README",

            ]

        )

    # -----------------------------------------------------
    # Project Structure
    # -----------------------------------------------------

    def project_structure(self, repo):

        ignore = {

            ".git",

            ".venv",

            "__pycache__",

            "workspace",

            ".idea",

            ".vscode",

            "node_modules",

        }

        folders = []

        for item in sorted(os.listdir(repo)):

            full = os.path.join(repo, item)

            if os.path.isdir(full) and item not in ignore:
                folders.append(item)

        return folders

    # -----------------------------------------------------
    # Helpers
    # -----------------------------------------------------

    def read_file(self, repo, filename):

        for root, _, files in os.walk(repo):

            if filename in files:

                path = os.path.join(root, filename)

                try:

                    with open(path, encoding="utf-8") as f:
                        return f.read()

                except Exception:

                    return ""

        return ""

    # -----------------------------------------------------
    # Implementation Plan
    # -----------------------------------------------------

    def create_plan(self, state):

        plan = []

        plan.append(
            "Understand the Jira requirements."
        )

        plan.append(
            "Identify affected modules."
        )

        plan.append(
            "Implement the requested functionality."
        )

        if state.test_framework != "Not Configured":

            plan.append(
                f"Run {state.test_framework} tests."
            )

        plan.append(
            "Review code quality."
        )

        plan.append(
            "Commit changes."
        )

        return plan