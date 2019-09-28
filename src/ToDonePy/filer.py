import csv
import os
import shutil
from operator import itemgetter
from pathlib import Path
from typing import List


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

        :returns: None

        """
        self.path = path
        if not os.path.isfile(self.path):
            if create:
                self.path.touch()
            else:
                raise OSError("File does not exist")

    def read(self) -> List[List[str]]:
        """Read the lines of self.path

        :Note: Reads in all lines, so will suffer on large files

        :returns: A list of lines where each line is a list 
        of column values

        """
        with open(self.path, "r", newline="") as file:
            reader = csv.reader(file, delimiter="\t")
            lines = []
            for line in reader:
                lines.append(line)
        return lines

    def write(self, rows: List[List[str]]) -> None:
        """Writes contents of rows to self.path.

        If the file exists, it overwrites.

        rows is a list of lists. rows[0] is line 1, rows[0][0] is 
        is line 1, column 1

        :rows: An list of strings to write to self.path

        :returns: None

        """
        with open(self.path, "w", newline="") as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerows(rows)

    def append(self, rows: List[List[str]]) -> None:
        """Appends contents of rows to self.path.

        Contents of self.path will not be overwritten, if it exists.

        rows is a list of lists. rows[0] is line 1, rows[0][0] is 
        is line 1, column 1

        :rows: An list of strings to write to self.path

        :returns: None

        """
        with open(self.path, "a", newline="") as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerows(rows)

    def delete(self, contains: str) -> None:
        """Deletes all lines from self where ``contains in line``

        :contains: string to use for line deletion

        :returns: None

        """
        with open(self.path, "r") as r_file:
            reader = csv.reader(r_file, delimiter="\t")
            with open("tmp", "a") as w_file:
                writer = csv.writer(w_file, delimiter="\t")
                for line in reader:
                    if contains not in line:
                        writer.writerow(line)
        shutil.move("tmp", self.path)

    def sort(self, cols: List[int]) -> None:
        """Sort the contents of self by columns

        :cols: List of columns, 0-indexed, to sort by

        :returns: None

        """
        lines = self.read()
        lines.sort(key=itemgetter(*cols))
        self.write(lines)
