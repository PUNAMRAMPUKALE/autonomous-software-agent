import json
import os

from tools.file_tool import FileTool
from tools.parser_tool import ParserTool


class IndexingAgent:

    def __init__(self):

        self.files = FileTool()

        self.parser = ParserTool()

    def build_index(self, state):

        print()

        print("=" * 60)

        print("INDEXING AGENT")

        print("=" * 60)

        source_files = self.files.find_source_files(
            state.local_path
        )

        symbols = []

        for file in source_files:

            parsed = self.parser.parse(file)

            symbols.extend(parsed)

        state.symbols = symbols

        output = []

        for symbol in symbols:

            output.append({

                "name": symbol.name,

                "type": symbol.symbol_type,

                "file": symbol.file_path,

                "line": symbol.line,

                "end_line": symbol.end_line,

            })

        os.makedirs(
            "index",
            exist_ok=True,
        )

        with open(

            "index/repository_index.json",

            "w",

            encoding="utf-8",

        ) as f:

            json.dump(

                output,

                f,

                indent=4,

            )

        print()

        print(f"Indexed {len(symbols)} symbols")

        return state