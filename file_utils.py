"""File utility functions."""
import os
from pathlib import Path
from typing import List


def count_lines(filepath: str) -> int:
    """Count the number of lines in a file."""
    with open(filepath) as f:
        return sum(1 for _ in f)


def list_python_files(directory: str) -> List[str]:
    """List all .py files in a directory recursively."""
    return sorted(str(p) for p in Path(directory).rglob("*.py") if not p.name.startswith("__"))


def read_file_safe(filepath: str) -> str:
    """Read a file, returning empty string if not found."""
    if not os.path.isfile(filepath):
        return ""
    with open(filepath) as f:
        return f.read()
