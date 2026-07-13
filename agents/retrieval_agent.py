"""
agents/retrieval_agent.py

Purpose
-------
Retrieve the most relevant repository symbols for a Jira story.

Responsibilities
----------------
1. Rank repository symbols.
2. Expand related dependencies.
3. Remove duplicate symbols.
4. Perform impact analysis.

This agent does not use an LLM.
"""

from collections import deque
import os

from tools.impact_analyzer import ImpactAnalyzer


class RetrievalAgent:
    """
    Retrieves repository context using the Repository Graph.
    """

    def __init__(self):

        self.impact = ImpactAnalyzer()

    # ---------------------------------------------------------
    # Main Entry
    # ---------------------------------------------------------

    def retrieve(self, state):
        """
        Retrieve repository context for downstream agents.
        """

        print()
        print("=" * 70)
        print("RETRIEVAL AGENT")
        print("=" * 70)

        summary = state.summary.lower()
        description = state.description.lower()

        ranked = []

        # -------------------------------------------------
        # Rank symbols
        # -------------------------------------------------

        for symbol in state.symbols:

            score = self.score_symbol(
                symbol,
                summary,
                description,
            )

            if score > 0:

                ranked.append(
                    (
                        score,
                        symbol,
                    )
                )

        ranked.sort(
            reverse=True,
            key=lambda item: item[0],
        )

        # -------------------------------------------------
        # Initial Retrieval
        # -------------------------------------------------

        initial = []

        for _, symbol in ranked[:10]:

            initial.append(symbol)

        # -------------------------------------------------
        # Graph Expansion
        # -------------------------------------------------

        expanded = self.expand(
            initial,
            state.repository_graph,
        )

        state.relevant_symbols = expanded

        self.print_symbols(expanded)

        # -------------------------------------------------
        # Impact Analysis
        # -------------------------------------------------

        self.impact.initialize(
            state.repository_graph
        )

        report = self.impact.analyze_symbols(
            expanded
        )

        state.impact_report = report

        self.impact.print_report(report)

        return state

    # ---------------------------------------------------------
    # Graph Expansion
    # ---------------------------------------------------------

    def expand(
        self,
        symbols,
        graph,
    ):
        """
        Expand retrieval results using the Repository Graph.
        """

        queue = deque(symbols)

        visited = set()

        expanded = []

        while queue:

            symbol = queue.popleft()

            if symbol.symbol_id in visited:
                continue

            visited.add(
                symbol.symbol_id
            )

            expanded.append(symbol)

            neighbours = graph.expand(
                symbol.symbol_id
            )

            for symbol_id in neighbours:

                neighbour = graph.get_symbol(
                    symbol_id
                )

                if neighbour:

                    queue.append(
                        neighbour
                    )

        return expanded

    # ---------------------------------------------------------
    # Ranking
    # ---------------------------------------------------------

    def score_symbol(
        self,
        symbol,
        summary,
        description,
    ):

        score = 0

        name = symbol.name.lower()

        parent = symbol.parent.lower()

        doc = symbol.docstring.lower()

        if name in summary:
            score += 25

        if name in description:
            score += 20

        if parent:

            if parent in summary:
                score += 15

            if parent in description:
                score += 10

        if doc:

            if doc in description:
                score += 5

        score += len(symbol.calls)

        score += len(symbol.imports)

        return score

    # ---------------------------------------------------------
    # Console Output
    # ---------------------------------------------------------

    def print_symbols(
        self,
        symbols,
    ):
        """
        Display retrieved repository symbols.
        """

        print()

        print("Relevant Repository Symbols")

        print("-" * 70)

        for symbol in symbols:

            print(
                f"{symbol.symbol_type:<15}"
                f"{symbol.name:<35}"
                f"{os.path.basename(symbol.file_path)}"
            )

        print("-" * 70)

        print(
            f"Retrieved {len(symbols)} symbols"
        )

        print("-" * 70)