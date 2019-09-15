#!/usr/bin/env python
# -*- coding: utf-8 -*-

from click.testing import CliRunner
from src.command_line.example import hello

def test_example_hello_prompt():
    """Run hello with default parameters"""
    runner = CliRunner()
    result = runner.invoke(hello, input='Ryan\n')
    assert result.exit_code == 0
    assert result.output == 'Your name: Ryan\nHello Ryan!\n'

def test_example_hello_count():
    """Run hello with --count option"""
    runner = CliRunner()
    result = runner.invoke(hello, ['--count', '3'], input='Ryan\n')
    assert result.exit_code == 0
    assert result.output == 'Your name: Ryan\nHello Ryan!\nHello Ryan!\nHello Ryan!\n'
