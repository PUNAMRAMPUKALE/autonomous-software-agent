import os


class FileTool:

    def find_source_files(self, repo):

        source_files = []

        ignore = {
            ".git",
            ".venv",
            "__pycache__",
            "workspace",
            "node_modules",
        }

        for root, dirs, files in os.walk(repo):

            dirs[:] = [
                d for d in dirs
                if d not in ignore
            ]

            for file in files:

                if file.endswith(
                    (
                        ".py",
                        ".js",
                        ".ts",
                        ".java",
                        ".go",
                        ".cs",
                    )
                ):

                    source_files.append(
                        os.path.join(root, file)
                    )

        return sorted(source_files)

    def read_file(self, path):

        try:

            with open(
                path,
                "r",
                encoding="utf-8",
            ) as f:

                return f.read()

        except Exception:

            return ""

    def build_context(
        self,
        files,
    ):

        context = ""

        for file in files:

            context += "\n"

            context += "=" * 70

            context += "\n"

            context += file

            context += "\n"

            context += "=" * 70

            context += "\n\n"

            context += self.read_file(file)

            context += "\n"

        return context