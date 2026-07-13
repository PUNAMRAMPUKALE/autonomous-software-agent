"""
tools/parser_tool.py

Purpose
-------
Parse Python source files using the built-in AST module.

Responsibilities
----------------
1. Discover classes and functions.
2. Track imports.
3. Track decorators.
4. Track inheritance.
5. Track function calls.
6. Generate a globally unique symbol ID.

Example Symbol ID
-----------------
agents/planner.py::PlannerAgent.choose_next_story

The symbol ID becomes the primary identifier used by the
Repository Graph instead of relying only on symbol names.
"""

import ast
import hashlib
import os

from models.symbol import Symbol


class SymbolVisitor(ast.NodeVisitor):
    """
    Walk a Python AST and extract repository symbols.
    """

    def __init__(self, file_path):

        self.file_path = file_path

        self.symbols = []

        self.current_class = None

        self.imports = []

    # ---------------------------------------------------------
    # Imports
    # ---------------------------------------------------------

    def visit_Import(self, node):

        for alias in node.names:

            self.imports.append(alias.name)

        self.generic_visit(node)

    def visit_ImportFrom(self, node):

        if node.module:

            self.imports.append(node.module)

        self.generic_visit(node)

    # ---------------------------------------------------------
    # Classes
    # ---------------------------------------------------------

    def visit_ClassDef(self, node):

        symbol = Symbol(

            name=node.name,

            symbol_type="class",

            file_path=self.file_path,

            start_line=node.lineno,

            end_line=node.end_lineno,

            parent="",

            docstring=ast.get_docstring(node) or "",

            imports=self.imports.copy(),

            calls=[],

            decorators=[
                ast.unparse(item)
                for item in node.decorator_list
            ],

            base_classes=[
                ast.unparse(item)
                for item in node.bases
            ],

            hash=self.compute_hash(node),

        )

        symbol.symbol_id = self.create_symbol_id(
            symbol
        )

        self.symbols.append(symbol)

        previous = self.current_class

        self.current_class = node.name

        self.generic_visit(node)

        self.current_class = previous

    # ---------------------------------------------------------
    # Functions
    # ---------------------------------------------------------

    def visit_FunctionDef(self, node):

        calls = []

        for child in ast.walk(node):

            if isinstance(child, ast.Call):

                try:

                    calls.append(
                        ast.unparse(child.func)
                    )

                except Exception:

                    pass

        symbol = Symbol(

            name=node.name,

            symbol_type="function",

            file_path=self.file_path,

            start_line=node.lineno,

            end_line=node.end_lineno,

            parent=self.current_class or "",

            docstring=ast.get_docstring(node) or "",

            imports=self.imports.copy(),

            calls=calls,

            decorators=[
                ast.unparse(item)
                for item in node.decorator_list
            ],

            hash=self.compute_hash(node),

        )

        symbol.symbol_id = self.create_symbol_id(
            symbol
        )

        self.symbols.append(symbol)

        self.generic_visit(node)

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def create_symbol_id(self, symbol):
        """
        Create a globally unique repository symbol ID.

        Example

        agents/planner.py::PlannerAgent.choose_next_story
        """

        relative = os.path.relpath(
            symbol.file_path
        )

        if symbol.parent:

            return (
                f"{relative}::"
                f"{symbol.parent}."
                f"{symbol.name}"
            )

        return (
            f"{relative}::"
            f"{symbol.name}"
        )

    def compute_hash(self, node):
        """
        Generate a stable hash for the AST node.
        """

        text = ast.dump(node)

        return hashlib.sha256(
            text.encode()
        ).hexdigest()


class ParserTool:
    """
    Parse a Python source file into repository symbols.
    """

    def parse(self, file_path):

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8",
            ) as file:

                source = file.read()

        except Exception:

            return []

        try:

            tree = ast.parse(source)

        except Exception:

            return []

        visitor = SymbolVisitor(file_path)

        visitor.visit(tree)

        return visitor.symbols