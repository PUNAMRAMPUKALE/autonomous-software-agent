"""
tools/impact_analyzer.py

Purpose
-------
Performs repository dependency and impact analysis.

Given one or more repository symbols, this component determines
what other parts of the repository may be affected.

The results are later consumed by:

- Retrieval Agent
- Developer Agent
- Reviewer Agent
- Pull Request Generator

No LLM is used in this component.
"""


class ImpactAnalyzer:
    """
    Repository impact analyzer.
    """

    def __init__(self):

        self.graph = None

    # ---------------------------------------------------------
    # Initialize
    # ---------------------------------------------------------

    def initialize(self, graph):
        """
        Store the Repository Graph.

        Parameters
        ----------
        graph : GraphTool
        """

        self.graph = graph

    # ---------------------------------------------------------
    # Analyze Single Symbol
    # ---------------------------------------------------------

    def analyze(self, symbol_name):
        """
        Analyze one repository symbol.

        Returns
        -------
        dict
        """

        methods = self.graph.get_methods(symbol_name)

        outgoing_calls = self.graph.get_calls(symbol_name)

        incoming_calls = self.graph.get_callers(symbol_name)

        imports = self.graph.get_imports(symbol_name)

        fan_out = len(outgoing_calls)

        fan_in = len(incoming_calls)

        risk_score = (

            fan_in * 3 +

            fan_out * 2 +

            len(methods) +

            len(imports)

        )

        return {

            "symbol": symbol_name,

            "methods": methods,

            "incoming_calls": incoming_calls,

            "outgoing_calls": outgoing_calls,

            "imports": imports,

            "fan_in": fan_in,

            "fan_out": fan_out,

            "risk_score": risk_score,

            "change_radius": fan_in + fan_out,

        }

    # ---------------------------------------------------------
    # Analyze Multiple Symbols
    # ---------------------------------------------------------

    def analyze_symbols(self, symbols):
        """
        Analyze a collection of repository symbols.
        """

        report = []

        for symbol in symbols:

            report.append(

                self.analyze(

                    symbol.name

                )

            )

        report.sort(

            key=lambda item: item["risk_score"],

            reverse=True,

        )

        return report

    # ---------------------------------------------------------
    # Print Report
    # ---------------------------------------------------------

    def print_report(self, report):
        """
        Display impact analysis.
        """

        print()

        print("=" * 70)

        print("IMPACT ANALYSIS")

        print("=" * 70)

        for item in report:

            print()

            print(f"Symbol : {item['symbol']}")

            print(

                f"Risk Score      : {item['risk_score']}"

            )

            print(

                f"Fan In          : {item['fan_in']}"

            )

            print(

                f"Fan Out         : {item['fan_out']}"

            )

            print(

                f"Change Radius   : {item['change_radius']}"

            )

            print(

                f"Methods         : {len(item['methods'])}"

            )

            print(

                f"Imports         : {len(item['imports'])}"

            )

        print("=" * 70)