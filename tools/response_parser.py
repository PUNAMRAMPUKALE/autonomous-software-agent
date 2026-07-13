"""
tools/response_parser.py
"""

import re

from tools.code_patch import CodePatch, PatchOperation


class ResponseParser:

    def __init__(self):
        """
        Initialize parser.
        """

        #
        # Supports:
        #
        # FILE: app.py
        #
        # ```python
        # ...
        # ```
        #

        self.pattern = re.compile(
            r"FILE:\s*(.*?)\s*\n+\s*```[^\n]*\n(.*?)\n```",
            re.DOTALL | re.MULTILINE,
        )

    # ---------------------------------------------------------

    def validate(self, response):

        return bool(
            self.pattern.search(response)
        )

    # ---------------------------------------------------------

    def parse(self, response):

        patch = CodePatch()

        for match in self.pattern.finditer(response):

            file_path = match.group(1).strip()

            code = match.group(2).rstrip()

            patch.add_operation(

                PatchOperation(

                    file_path=file_path,

                    operation="UPDATE",

                    new_content=code,

                )

            )

        return patch

    # ---------------------------------------------------------

    def extract_files(self, response):

        return [

            match.group(1).strip()

            for match in self.pattern.finditer(response)

        ]

    # ---------------------------------------------------------

    def statistics(self, patch):

        create = 0
        update = 0
        delete = 0

        for operation in patch.operations:

            if operation.operation == "CREATE":
                create += 1

            elif operation.operation == "UPDATE":
                update += 1

            elif operation.operation == "DELETE":
                delete += 1

        return {

            "operations": patch.total_operations(),

            "create": create,

            "update": update,

            "delete": delete,

        }

    # ---------------------------------------------------------

    def print_summary(self, patch):

        stats = self.statistics(patch)

        print()
        print("=" * 70)
        print("RESPONSE PARSER")
        print("=" * 70)

        print(f"Total Operations : {stats['operations']}")
        print(f"Create Files     : {stats['create']}")
        print(f"Update Files     : {stats['update']}")
        print(f"Delete Files     : {stats['delete']}")

        if patch.operations:

            print()
            print("Files")

            for operation in patch.operations:

                print(
                    f"- {operation.operation:<7} {operation.file_path}"
                )

        print("=" * 70)