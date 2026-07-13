"""
tools/patch_validator.py
"""

class PatchValidator:

    def validate(self, patch):

        #
        # Nothing to validate.
        #

        if patch is None:

            return True, []

        errors = []

        for operation in patch.operations:

            if not operation.file_path:

                errors.append(
                    "Missing file path."
                )

            if operation.operation not in (

                "CREATE",

                "UPDATE",

                "DELETE",

            ):

                errors.append(

                    f"Unknown operation: {operation.operation}"

                )

        return (

            len(errors) == 0,

            errors,

        )

    # ---------------------------------------------------------

    def print_report(

        self,

        valid,

        errors,

    ):

        print()

        print("=" * 70)

        print("PATCH VALIDATION")

        print("=" * 70)

        if valid:

            print(

                "Patch validation successful."

            )

        else:

            print(

                "Validation Errors"

            )

            for error in errors:

                print(

                    "-", error

                )

        print("=" * 70)