import shutil
import subprocess
from typing import List


def external_command(args: List[str]) -> subprocess.CompletedProcess:
    """Make a generic command line call

    Any command line call can be made. Pass the respective components as individual
    strings. Roughly speaking, anywhere there is a space, break it into a new
    component. See the documentation on `subprocess.run`_ for advanced use cases.

    .. _subprocess.run:
        https://docs.python.org/3.7/library/subprocess.html#subprocess.Popen

    Note
    ----
        If run in a situation where the user was providing a dynamic input, there are
        obvious security risks. In the app, however, the user cannot provide their own
        input, which I believe sufficiently mitigates the risk in this use case. 
        Obviously, if you adopt and use this function elsewhere, take care to check
        your inputs!

    Parameters
    ----------
    *args : List[str]
        The parts of the external command

    Returns
    -------
    subprocess.CompletedProcess
        If successful. This contains a number of useful attributes, including
        returncode and stdout.

    Raises
    ------
    OSError
        If unsuccessful. This will be thrown if the command found in args[0]
        cannot be found on the OS 
    subprocess.CalledProcessError
        If the called command returns a non-zero exit status
        
    Examples
    --------
    The results of a successful command ccan be queried like so:

    >>> results = external_command(['echo', 'hello']) 
    >>> results.returncode
    0

    """

    if shutil.which(args[0]) is None:
        raise OSError(f"Command {args[0]} not found!")
    return subprocess.run(list(args), check=True, capture_output=True)
