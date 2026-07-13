"""
tools/file_writer.py

Purpose
-------
Safely apply validated repository patches.

This is the ONLY component allowed to modify repository files.

Workflow

Patch
    ↓
PatchValidator
    ↓
FileWriter
    ↓
Repository

Features
--------
- Backup existing files
- Create files
- Update files
- Delete files
- Rollback support
"""

from pathlib import Path
import shutil


class FileWriter:
    """
    Applies validated patch operations.
    """

    BACKUP_SUFFIX = ".bak"

    def __init__(self):
        """
        Initialize FileWriter.
        """
        pass

    # ---------------------------------------------------------
    # Apply Patch
    # ---------------------------------------------------------

    def apply_patch(self, patch):
        """
        Apply every operation in a CodePatch.

        Parameters
        ----------
        patch : CodePatch

        Returns
        -------
        bool
        """

        print()

        print("=" * 70)
        print("FILE WRITER")
        print("=" * 70)

        applied = 0

        for operation in patch.operations:

            self.apply_operation(operation)

            applied += 1

        print()

        print(f"Applied Operations : {applied}")

        print("=" * 70)

        return True

    # ---------------------------------------------------------
    # Apply One Operation
    # ---------------------------------------------------------

    def apply_operation(self, operation):
        """
        Apply a single repository operation.
        """

        if operation.operation == "CREATE":

            self.create_file(
                operation.file_path,
                operation.new_content,
            )

        elif operation.operation == "UPDATE":

            self.update_file(
                operation.file_path,
                operation.new_content,
            )

        elif operation.operation == "DELETE":

            self.delete_file(
                operation.file_path,
            )

    # ---------------------------------------------------------
    # Create File
    # ---------------------------------------------------------

    def create_file(
        self,
        file_path,
        content,
    ):
        """
        Create a new repository file.
        """

        path = Path(file_path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        path.write_text(
            content,
            encoding="utf-8",
        )

        print(f"CREATE : {file_path}")

    # ---------------------------------------------------------
    # Update File
    # ---------------------------------------------------------

    def update_file(
        self,
        file_path,
        content,
    ):
        """
        Update an existing file.
        """

        path = Path(file_path)

        if path.exists():

            shutil.copy2(
                path,
                str(path) + self.BACKUP_SUFFIX,
            )

        path.write_text(
            content,
            encoding="utf-8",
        )

        print(f"UPDATE : {file_path}")

    # ---------------------------------------------------------
    # Delete File
    # ---------------------------------------------------------

    def delete_file(
        self,
        file_path,
    ):
        """
        Delete an existing file.
        """

        path = Path(file_path)

        if not path.exists():
            return

        shutil.copy2(
            path,
            str(path) + self.BACKUP_SUFFIX,
        )

        path.unlink()

        print(f"DELETE : {file_path}")

    # ---------------------------------------------------------
    # Rollback
    # ---------------------------------------------------------

    def rollback(
        self,
        patch,
    ):
        """
        Restore backup files.
        """

        print()

        print("=" * 70)
        print("ROLLBACK")
        print("=" * 70)

        restored = 0

        for operation in patch.operations:

            backup = Path(
                operation.file_path
                + self.BACKUP_SUFFIX
            )

            if backup.exists():

                shutil.copy2(
                    backup,
                    operation.file_path,
                )

                restored += 1

        print(
            f"Restored Files : {restored}"
        )

        print("=" * 70)