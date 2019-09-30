import subprocess
from pathlib import Path


def file_len(file: Path) -> int:
    """Find the number of lines in a file

    :file: Path to the file

    :returns: Number of lines in a file
    """
    wc = subprocess.Popen(
        ["wc", "-l", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    result, err = wc.communicate()
    if wc.returncode != 0:
        raise IOError(err)
    return int(result.strip().split()[0])
