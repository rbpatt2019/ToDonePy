# -*- coding: utf-8 -*-
import subprocess

import pytest
from helpers.external_command import external_command


def test_ec_successful() -> None:
    """Test a basic command call with `external_command`

    Checks that a successful call returns an exit code of 0 and the expected output
    """
    results = external_command(["echo", "hello"])
    assert results.returncode == 0
    assert results.stdout == b"hello\n"


def test_ec_OSError() -> None:
    """Test `external_command` raise an `OSError` for `Command Not Found`

    """
    with pytest.raises(OSError):
        external_command(["thisdoesntexistinanyOS"])


def test_ec_ProcessError() -> None:
    """Test `external_command` raise an CalledProcessError when has a non-0 status

    """
    with pytest.raises(subprocess.CalledProcessError):
        external_command(["false"])
