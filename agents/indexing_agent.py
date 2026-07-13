"""
agents/indexing_agent.py

Purpose
-------
Indexes the repository and builds the Repository Graph.

Workflow

Repository
    │
    ▼
Find Python Files
    │
    ▼
Parse Source Code
    │
    ▼
Extract Symbols
    │
    ▼
Build Repository Graph
    │
    ▼
Save repository_index.json
"""

import json
import os

from tools.file_tool import FileTool
from tools.parser_tool import ParserTool
from tools.graph_tool import GraphTool


class IndexingAgent:

    def __init__(self):

        self.files = FileTool()

        self.parser = ParserTool()

        self.graph = GraphTool()

    # --------------------------------------------------
    # Main
    # --------------------------------------------------

    def build_index(self, state):

        print()

        print("=" * 60)
        print("INDEXING AGENT")
        print("=" * 60)

        source_files = self.files.find_source_files(
            state.local_path
        )

        state.source_files = source_files

        repository_symbols = []

        statistics = {
            "files": 0,
            "classes": 0,
            "functions": 0,
            "async_functions": 0,
        }

        for file in source_files:

            print(f"Indexing : {os.path.basename(file)}")

            statistics["files"] += 1

            symbols = self.parser.parse(file)

            for symbol in symbols:

                repository_symbols.append(symbol)

                if symbol.symbol_type == "class":
                    statistics["classes"] += 1

                elif symbol.symbol_type == "function":
                    statistics["functions"] += 1

                elif symbol.symbol_type == "async_function":
                    statistics["async_functions"] += 1

        state.symbols = repository_symbols

        # ------------------------------------------
        # Build Repository Graph
        # ------------------------------------------

        graph = self.graph.build(
            repository_symbols
        )

        state.repository_graph = graph

        # ------------------------------------------
        # Save JSON
        # ------------------------------------------

        self.save_index(
            repository_symbols
        )

        self.print_summary(
            statistics
        )

        graph.print_summary()

        return state

    # --------------------------------------------------
    # Save repository_index.json
    # --------------------------------------------------

    def save_index(self, symbols):

        os.makedirs(
            "index",
            exist_ok=True,
        )

        data = []

        for symbol in symbols:

            data.append(
                symbol.to_dict()
            )

        with open(

            "index/repository_index.json",

            "w",

            encoding="utf-8",

        ) as file:

            json.dump(

                data,

                file,

                indent=4,

            )

    # --------------------------------------------------
    # Console Summary
    # --------------------------------------------------

    def print_summary(self, stats):

        print()

        print("-" * 60)

        print("Repository Index Summary")

        print("-" * 60)

        print(
            f"Python Files      : {stats['files']}"
        )

        print(
            f"Classes           : {stats['classes']}"
        )

        print(
            f"Functions         : {stats['functions']}"
        )

        print(
            f"Async Functions   : {stats['async_functions']}"
        )

        print("-" * 60)