#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from click.testing import CliRunner

from command_line.ToDoneCLI import to
from tests.make_temp import make_file, make_path


def test_example_hello_prompt(tmp_path):
    """Run to do with existing custom file"""
    runner = CliRunner()
    with runner.isolated_filesystem():
        csv = make_file(tmp_path, "1,Old task")
        result = runner.invoke(to, ["--file", f"{csv}", "do", "New task", "1"])
        assert result.exit_code == 0
        assert result.output == "Task added\n"
        assert Path(csv).read_text() == "1,Old task\n1,New task"
