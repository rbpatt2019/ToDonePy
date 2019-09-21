#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from click.testing import CliRunner
from datetime import datetime as dt

from command_line.ToDoneCLI import to
from tests.make_temp import make_file, make_path


def test_to_do_custom_file(tmp_path):
    """Run to do with existing custom file"""
    runner = CliRunner()
    with runner.isolated_filesystem():
        csv = make_file(tmp_path, "1,Old task,2019-09-20 20:56:00\n")
        result = runner.invoke(to, ["--file", f"{csv}", "do", "New task", "1"])
        date = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        assert result.exit_code == 0
        assert result.output == "Task added\n"
        assert Path(csv).read_text() == f"1,Old task,2019-09-20 20:56:00\n1,New task,{date}\n"

def test_to_doing_custom_file(tmp_path):
    """Run to do with existing custom file"""
    runner = CliRunner()
    with runner.isolated_filesystem():
        csv = make_file(tmp_path, "1,Old task\n2,New task")
        result = runner.invoke(to, ["--file", f"{csv}", "doing"])
        assert result.exit_code == 0
        assert result.output == "1,Old task\n2,New task\n"
        assert Path(csv).read_text() == "1,Old task\n2,New task"

def test_to_done_custom_file(tmp_path):
    """Run to do with existing custom file"""
    runner = CliRunner()
    with runner.isolated_filesystem():
        csv = make_file(tmp_path, "1,Old task\n2,New task")
        result = runner.invoke(to, ["--file", f"{csv}", "done", "New"])
        assert result.exit_code == 0
        assert result.output == "Task removed\n"
        assert Path(csv).read_text() == "1,Old task\n"
