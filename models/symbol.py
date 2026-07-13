from dataclasses import dataclass, field


@dataclass
class Symbol:

    name: str

    symbol_type: str

    file_path: str

    line: int

    end_line: int

    parent: str = ""

    imports: list = field(default_factory=list)

    calls: list = field(default_factory=list)