import os
from pathlib import Path
from typing import Iterator, List


class Filer(object):

    """A class for gracefully handling file interactions

    Designed particularly for passing context in a Click program. 

    :path: A Unix filepath to the desired file
    :create: If the file does not already exist, create it.

    """

    def __init__(self, path: Path, create: bool = True) -> None:
        """Initialise the Filer

        :path: A Unix filepath to the desired file
        :create: If the file does not already exist, create it.

        """
        self.path = path
        if not os.path.isfile(self.path):
            if create:
                self.path.touch()
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

        Multiple entries are concatenated by new lines

        :ins: An list of strings to write to self.path
        :returns: None

        """
        with open(self.path, "w") as file:
            file.write("\n".join(ins))
            file.write("\n")  # File will end in newline

    def append(self, ins: List[str]) -> None:
        """Appends contents of ins to self.path.

        Contents of self.path will not be overwritten, if it exists.

        Multiple entries are concatenated by new lines

        :ins: An list of strings to write to self.path
        :returns: None

        """
        with open(self.path, "a") as file:
            file.write("\n".join(ins))
            file.write("\n")  # File will end on new line

    def delete(self, contains: str) -> None:
        """Deletes all lines from self where ``contains in line``

        :contains: string to use for line deletion
        :returns: None

        """
        with open(self.path, "r") as r_file:
            with open("tmp", "a") as w_file:
                for line in r_file:
                    if contains not in line:
                        w_file.write(line)
        os.replace("tmp", self.path)
