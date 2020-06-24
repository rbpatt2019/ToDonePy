#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime as dt
from pathlib import Path
from shutil import which

import pytest
from click.testing import CliRunner

from command_line.ToDoneCLI import to

results_txt = "ID\tRank\tDate\tTask\n1\t2\t2019-09-20 20:56:00\tOld task\n2\t1\t2019-09-24 12:57:00\tNew task\n"


def test_to_do_custom_file(tmp_file: Path):
    """Run to do with existing custom file

    :tmp_file: Custom pytest.fixture. Instantiated tsv
    
    :returns: None
    """
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(to, ["--file", f"{tmp_file}", "do", "1", "Newer task"])
        date = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        assert result.exit_code == 0
        assert result.output == "1 task(s) added!\n"
        assert tmp_file.read_text() == results_txt + f"3\t1\t{date}\tNewer task\n"


def test_to_doing_custom_file(tmp_file: Path):
    """Run to doing with existing custom file

    :tmp_file: Custom pytest.fixture. Instantiated tsv
    
    :returns: None
    """
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(to, ["--file", f"{tmp_file}", "doing"])
        assert result.exit_code == 0
        assert result.output == results_txt + "You do not have 5 tasks!\n"
        assert tmp_file.read_text() == results_txt


@pytest.mark.xfail(reason="Vim hangs the test, resulting in non-0 exit code")
def test_to_doing_custom_file_edit_flag(tmp_file: Path):
    """Run to doing with the edit flag

    :tmp_file: Custom pytest.fixture. Instantiated tsv
    
    :returns: None
    """
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(to, ["--file", f"{tmp_file}", "doing", "--edit"])
        assert result.exit_code == 0
        assert result.output == ""


def test_to_doing_custom_file_sort_flag(tmp_file: Path):
    """Run to doing with the --sort flag

    :tmp_file: Custom pytest.fixture. Instantiated tsv
    
    :returns: None
    """
    runner = CliRunner()
    custom_result = "ID\tRank\tDate\tTask\n1\t1\t2019-09-24 12:57:00\tNew task\n2\t2\t2019-09-20 20:56:00\tOld task\n"
    with runner.isolated_filesystem():
        result = runner.invoke(to, ["--file", f"{tmp_file}", "doing", "--sort", "rank"])
        assert result.exit_code == 0
        assert result.output == custom_result + "You do not have 5 tasks!\n"
        assert tmp_file.read_text() == custom_result


@pytest.mark.skipif(which("notify-send") is None, reason="Requires notify-send")
def test_to_doing_custom_file_graphic_flag(tmp_file):
    """Run to doing with the --graphic flag

    :tmp_file: Custom pytest.fixture. Instantiated tsv
    
    :returns: None
    """
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(to, ["--file", f"{tmp_file}", "doing", "--graphic"])
        assert result.exit_code == 0
        assert result.output == ""


def test_to_done_custom_file(tmp_file: Path):
    """Run to doing with the --graphic flag

    :tmp_file: Custom pytest.fixture. Instantiated tsv
    
    :returns: None
    """
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(to, ["--file", f"{tmp_file}", "done", "New task", "Nothing"])
        assert result.exit_code == 0
        assert (
            result.output
            == 'Task "New task" successfully deleted!\nTask "Nothing" not in TODO.tsv...\n'
        )
        assert (
            tmp_file.read_text()
            == "ID\tRank\tDate\tTask\n1\t2\t2019-09-20 20:56:00\tOld task\n"
        )
