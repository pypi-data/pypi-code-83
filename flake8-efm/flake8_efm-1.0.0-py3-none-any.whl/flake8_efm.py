from flake8.formatting import base

# Map of flake8 codes to errorformat codes:
error_mappings = {
    "B": "W",  # flake8-bugbear
    "E": "E",
    "F": "W",  # formatting
    "I": "W",  # flake8-import-order
    "W": "W",
}


class Errorformat(base.BaseFormatter):
    """Formatter compatible with Vim's errorformat."""

    def format(self, error):
        file = error.filename
        line = error.line_number  # or physical_line ??
        col = error.column_number
        type = error_mappings.get(error.code[0], "E")
        message = f"{error.code}: {error.text}"

        return f"{file}:{line}:{col}:{type}:{message}"
