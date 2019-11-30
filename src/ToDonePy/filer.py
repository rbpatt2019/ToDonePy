import csv
import os
import shutil
from operator import itemgetter
from pathlib import Path
from typing import List

from ToDonePy.file_len import file_len as file_len
from ToDonePy.itemsetter import itemsetter as itemsetter


class Filer(object):

    """A class for gracefully handling file interactions with delimited data

    Designed particularly for passing context in a Click program. 

    :path: A Unix filepath to the desired file
    :create: If the file does not already exist, create it.
    :delimiter: The delimiter to be used for the file

    """

    def __init__(self, path: Path, create: bool = True, delimiter: str = "\t") -> None:
        """Initialise the Filer

        :path: A Unix filepath to the desired file
        :create: If the file does not already exist, create it.
        :delimiter: The delimiter to be used for the file

        :returns: None

        """
        self.path = Path(path)
        self.delimiter = delimiter
        if not os.path.isfile(self.path):
            if create:
                self.path.touch()
                # Specifically for initiating todos
                self.append([["ID", "Rank", "Date", "Task"]])
            else:
                raise OSError("File does not exist")

    def read(self) -> List[List[str]]:
        """Read the lines of self.path

        :Note: Reads in all lines, so will suffer on large files

        :returns: A list of lines where each line is a list 
        of column values

        """
        with open(self.path, "r", newline="") as file:
            reader = csv.reader(file, delimiter=self.delimiter)
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
            writer = csv.writer(file, delimiter=self.delimiter)
            writer.writerows(rows)

    def write_col(self, col: List[str], index: int = 0) -> None:
        """Writes contents of col to column given by index

        :col: A list of strings to write to self.path
        :index: To which column to write. Defaults to first (index = 0)

        :returns: None

        """
        lines = self.read()
        write_col = itemsetter(index)
        for line, val in zip(lines, col):
            write_col(line, val)
        self.write(lines)

    def append(self, rows: List[List[str]]) -> None:
        """Appends contents of rows to self.path.

        Contents of self.path will not be overwritten, if it exists.

        rows is a list of lists. rows[0] is line 1, rows[0][0] is 
        is line 1, column 1

        :rows: An list of strings to write to self.path

        :returns: None

        """
        with open(self.path, "a", newline="") as file:
            writer = csv.writer(file, delimiter=self.delimiter)
            writer.writerows(rows)

    def delete(self, contains: str) -> bool:
        """Deletes all lines from self where ``contains in line``

        :contains: string to use for line deletion

        :returns: True, if successful, false otherwise

        """
        with open(self.path, "r") as r_file:
            reader = csv.reader(r_file, delimiter=self.delimiter)
            with open("tmp", "a") as w_file:
                writer = csv.writer(w_file, delimiter=self.delimiter)
                for line in reader:
                    if contains not in line:
                        writer.writerow(line)
        if file_len(self.path) == file_len(Path("tmp")):
            os.remove(Path("tmp"))
            return False
        else:
            shutil.move("tmp", self.path)
            return True

    def sort(self, cols: List[int], header: bool = False) -> None:
        """Sort the contents of self by columns

        :cols: List of columns, 0-indexed, to sort by
        :header: Whether or not row 0 is a header. If True, row 0 is skipped for sorting.

        :returns: None

        """
        lines = self.read()
        if header:
            # Slice off header
            head = lines[0]
            entries = lines[1:]
            # Sort and re-add
            entries.sort(key=itemgetter(*cols))
            entries.insert(0, head)
            # Write
            self.write(entries)
        else:
            lines.sort(key=itemgetter(*cols))
            self.write(lines)
