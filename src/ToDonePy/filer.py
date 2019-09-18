from os.path import isfile
from pathlib import Path
from typing import Iterator, List


class Filer(object):

    """A class for gracefully handling file interactions

    Designed particularly for passing context in a Click program. 

    :PARAMS:
    :path: A Unix filepath to the desired file
    :create: If the file does not already exist, create it.

    :METHODS:
    :read: Can check to see if the file exists, then returns an iterator of lines
    :write: Writes to the file, overwriting existing contents
    :append: Writes to the end of the file, preserving existing contents
    
    """

    def __init__(self, path: str, create: bool = True) -> None:
        """Initialise the Filer

        :path: A Unix filepath to the desired file
        :create: If the file does not already exist, create it.

        """
        self.path = path
        if not isfile(Path(self.path)):
            if create:
                Path(self.path).touch()
            else:
                raise OSError("File does not exist")

    def read(self) -> Iterator[str]:
        """Read the lines of self.path

        :returns: A generator containing the individual lines of self.path

        """
        with open(self.path, "r") as file:
            for line in file:
                yield line.rstrip("\n")

    def write(self, ins: List[str]) -> None:
        """Writes contents of ins to self.path.

        If the file exists, it overwrites.
        Multiple entries are concatenated by new lines - "\n"

        :ins: An iterable of strings to write to self.path
        :returns: None

        """
        with open(self.path, "w") as file:
            file.write("\n".join(ins))

    def append(self, ins: List[str]) -> None:
        """Appends contents of ins to self.path.

        Contents of self.path will not be overwritten, if it exists.
        Multiple entries are concatenated by new lines - "\n"

        :ins: An iterable of strings to write to self.path
        :returns: None

        """
        with open(self.path, "a") as file:
            file.write("\n")  # Open on new line
            file.write("\n".join(ins))
