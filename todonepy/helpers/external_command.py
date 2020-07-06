import shutil
import subprocess
from typing import List


def external_command(args: List[str]) -> None:
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
        Obviously, if you addapt and use this function elsewhere, take care to check
        your inputs!

    Parameters
    ----------
    *args : List[str]
        The parts of the external command

    Returns
    -------
    True
        If successful.

    Raises
    ------
    OSError
        If unsuccessful. This will be thrown if the command found in args[0]
        cannot be found on the OS 
    subprocess.CalledProcessError
        If the called command returns a non-zero exit status
        
    Example
    -------
    >>> external_command('notify-send', 'Message Title', 'This is notification', '-u', 'low', '-t', '10') 
    True

    """
    if shutil.which(args[0]) is None:
        raise OSError(f"Command {args[0]} not found!")
    subprocess.run(list(args), check=True)
