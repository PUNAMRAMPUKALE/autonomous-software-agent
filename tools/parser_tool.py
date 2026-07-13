import ast

from models.symbol import Symbol


class ParserTool:

    def parse(self, file_path):

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8",
            ) as f:

                source = f.read()

        except Exception:

            return []

        try:

            tree = ast.parse(source)

        except Exception:

            return []

        symbols = []

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):

                symbols.append(

                    Symbol(

                        name=node.name,

                        symbol_type="class",

                        file_path=file_path,

                        line=node.lineno,

                        end_line=node.end_lineno,

                    )

                )

            elif isinstance(node, ast.FunctionDef):

                symbols.append(

                    Symbol(

                        name=node.name,

                        symbol_type="function",

                        file_path=file_path,

                        line=node.lineno,

                        end_line=node.end_lineno,

                    )

                )

        return symbols