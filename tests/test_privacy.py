"""Verify the report's privacy boundary and explicit startup behavior."""
import json
import subprocess
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

from app import collect_report


class PrivacyTests(unittest.TestCase):
    def test_report_contains_only_allowlisted_fields(self):
        report = collect_report()
        self.assertEqual(set(report), {
            "schema_version", "created_at", "system", "release", "machine", "python_version"})
        json.dumps(report)

    def test_device_name_is_never_collected(self):
        with patch("platform.node", side_effect=AssertionError("Private identifier accessed")):
            collect_report()

    def test_import_does_not_start_gui(self):
        result = subprocess.run(
            [sys.executable, "-c", "from unittest.mock import patch; "
             "guard = patch('tkinter.Tk', side_effect=AssertionError('Unexpected GUI')); "
             "guard.start(); import app"],
            cwd=Path(__file__).resolve().parents[1], capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
