"""
tools/graph_tool.py

Purpose
-------
Repository Knowledge Graph.

This component stores relationships between repository symbols.

Relationships

1. Class -> Methods
2. Function -> Calls
3. Function <- Callers
4. Symbol -> Imports

Every node is identified using a globally unique symbol_id.

Example

agents/planner.py::PlannerAgent.choose_next_story
"""

from collections import defaultdict


class GraphTool:
    """
    Repository dependency graph.
    """

    def __init__(self):

        # symbol_id -> Symbol
        self.symbol_lookup = {}

        # symbol_id -> set(symbol_id)
        self.call_graph = defaultdict(set)

        # symbol_id -> set(symbol_id)
        self.reverse_call_graph = defaultdict(set)

        # class symbol_id -> method symbol_id
        self.class_graph = defaultdict(set)

        # symbol_id -> imports
        self.import_graph = defaultdict(set)

    # ---------------------------------------------------------
    # Build Graph
    # ---------------------------------------------------------

    def build(self, symbols):
        """
        Build the repository graph.
        """

        self.symbol_lookup.clear()
        self.call_graph.clear()
        self.reverse_call_graph.clear()
        self.class_graph.clear()
        self.import_graph.clear()

        # --------------------------------------------
        # Register symbols
        # --------------------------------------------

        for symbol in symbols:

            self.symbol_lookup[
                symbol.symbol_id
            ] = symbol

        # --------------------------------------------
        # Build relationships
        # --------------------------------------------

        name_lookup = {}

        for symbol in symbols:

            name_lookup[
                symbol.name
            ] = symbol.symbol_id

        for symbol in symbols:

            self._build_class_graph(symbol)

            self._build_call_graph(
                symbol,
                name_lookup,
            )

            self._build_import_graph(symbol)

        return self

    # ---------------------------------------------------------
    # Class Graph
    # ---------------------------------------------------------

    def _build_class_graph(self, symbol):

        if not symbol.parent:
            return

        class_symbol = None

        for item in self.symbol_lookup.values():

            if item.name == symbol.parent:

                class_symbol = item

                break

        if class_symbol:

            self.class_graph[
                class_symbol.symbol_id
            ].add(
                symbol.symbol_id
            )

    # ---------------------------------------------------------
    # Call Graph
    # ---------------------------------------------------------

    def _build_call_graph(
        self,
        symbol,
        lookup,
    ):

        for call in symbol.calls:

            if call not in lookup:
                continue

            target = lookup[call]

            self.call_graph[
                symbol.symbol_id
            ].add(target)

            self.reverse_call_graph[
                target
            ].add(
                symbol.symbol_id
            )

    # ---------------------------------------------------------
    # Import Graph
    # ---------------------------------------------------------

    def _build_import_graph(self, symbol):

        for module in symbol.imports:

            self.import_graph[
                symbol.symbol_id
            ].add(module)

    # ---------------------------------------------------------
    # Queries
    # ---------------------------------------------------------

    def get_symbol(self, symbol_id):

        return self.symbol_lookup.get(symbol_id)

    def get_methods(self, symbol_id):

        return list(

            self.class_graph.get(
                symbol_id,
                [],
            )

        )

    def get_calls(self, symbol_id):

        return list(

            self.call_graph.get(
                symbol_id,
                [],
            )

        )

    def get_callers(self, symbol_id):

        return list(

            self.reverse_call_graph.get(
                symbol_id,
                [],
            )

        )

    def get_imports(self, symbol_id):

        return list(

            self.import_graph.get(
                symbol_id,
                [],
            )

        )

    # ---------------------------------------------------------
    # Graph Expansion
    # ---------------------------------------------------------

    def expand(self, symbol_id):
        """
        Return directly connected symbols.
        """

        related = set()

        related.update(
            self.get_methods(symbol_id)
        )

        related.update(
            self.get_calls(symbol_id)
        )

        related.update(
            self.get_callers(symbol_id)
        )

        return sorted(related)

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def statistics(self):

        return {

            "symbols": len(
                self.symbol_lookup
            ),

            "classes": len(
                self.class_graph
            ),

            "calls": len(
                self.call_graph
            ),

            "reverse_calls": len(
                self.reverse_call_graph
            ),

            "imports": len(
                self.import_graph
            ),

        }

    # ---------------------------------------------------------
    # Console
    # ---------------------------------------------------------

    def print_summary(self):

        stats = self.statistics()

        print()

        print("=" * 70)

        print("REPOSITORY GRAPH")

        print("=" * 70)

        print(
            f"Symbols         : {stats['symbols']}"
        )

        print(
            f"Classes         : {stats['classes']}"
        )

        print(
            f"Call Graph      : {stats['calls']}"
        )

        print(
            f"Reverse Calls   : {stats['reverse_calls']}"
        )

        print(
            f"Import Graph    : {stats['imports']}"
        )

        print("=" * 70)