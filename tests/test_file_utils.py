from file_utils import count_lines, list_python_files, read_file_safe
import tempfile
import os
from pathlib import Path


class TestFileUtils:
    def test_count_lines(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            f.write("a\nb\nc\n")
            tmp = f.name
        try:
            assert count_lines(tmp) == 3
        finally:
            os.unlink(tmp)

    def test_count_lines_empty(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            tmp = f.name
        try:
            assert count_lines(tmp) == 0
        finally:
            os.unlink(tmp)

    def test_list_python_files(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d, "a.py").touch()
            Path(d, "sub").mkdir()
            Path(d, "sub", "b.py").touch()
            Path(d, "__init__.py").touch()
            result = list_python_files(d)
            assert "a.py" in [os.path.basename(p) for p in result]
            assert "sub/b.py" in [os.path.relpath(p, d) for p in result]
            assert "__init__.py" not in [os.path.basename(p) for p in result]

    def test_read_file_safe_exists(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            f.write("hello")
            tmp = f.name
        try:
            assert read_file_safe(tmp) == "hello"
        finally:
            os.unlink(tmp)

    def test_read_file_safe_missing(self):
        assert read_file_safe("/tmp/nonexistent_file_xyz") == ""
