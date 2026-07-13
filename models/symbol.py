"""
models/symbol.py

Purpose
-------
Represents a symbol discovered while indexing the repository.

A symbol can be:

- Class
- Function
- Async Function
- Method

Later milestones will enrich these symbols with semantic search,
dependency analysis and AI reasoning.

This model is intentionally language-agnostic so it can later support
Python, Java, JavaScript, Go, C#, etc.
"""

from dataclasses import dataclass, field


@dataclass
class Symbol:
    """
    Represents one symbol inside the repository.
    """

    # ---------------------------------------------
    # Basic Information
    # ---------------------------------------------

    name: str

    symbol_type: str

    file_path: str

    start_line: int

    end_line: int

    # ---------------------------------------------
    # Ownership
    # ---------------------------------------------

    # Example:
    # PlannerAgent
    #
    # choose_next_story()
    #
    # parent = PlannerAgent
    #
    parent: str = ""

    # ---------------------------------------------
    # Documentation
    # ---------------------------------------------

    docstring: str = ""
    symbol_id: str = ""

    # ---------------------------------------------
    # Relationships
    # ---------------------------------------------

    imports: list[str] = field(
        default_factory=list
    )

    calls: list[str] = field(
        default_factory=list
    )

    decorators: list[str] = field(
        default_factory=list
    )

    base_classes: list[str] = field(
        default_factory=list
    )

    # ---------------------------------------------
    # Metadata
    # ---------------------------------------------

    language: str = "Python"

    complexity: int = 0

    hash: str = ""

    # ---------------------------------------------
    # Serialization
    # ---------------------------------------------

    def to_dict(self):

        """
        Convert Symbol to JSON.
        """

        return {

            "name": self.name,

            "type": self.symbol_type,

            "file": self.file_path,

            "start_line": self.start_line,

            "end_line": self.end_line,

            "parent": self.parent,

            "docstring": self.docstring,

            "imports": self.imports,

            "calls": self.calls,

            "decorators": self.decorators,

            "base_classes": self.base_classes,

            "language": self.language,

            "complexity": self.complexity,

            "hash": self.hash,
            
            "symbol_id": self.symbol_id,

        }