import csv
import os
import shutil
from operator import itemgetter
from pathlib import Path
from typing import List

from helpers.external_command import external_command
from helpers.itemsetter import itemsetter


class Filer:

    """A class for gracefully handling file interactions with delimited data

    Designed particularly for passing context in a CLI, it is a thin wrapper for many
    common file I/O actions, including reading, writing (both lines and columns), and
    deleting.

    """

    def __init__(self, path: Path, create: bool = True, delimiter: str = "\t") -> None:
        """Initialise the Filer object
        
        Note
        ----
            The attribute self.length is created to hold the number of lines in the file.
            This is particularly useful for checking to see if a file has been altered.

        Parameters
        ----------
        path : Path
            A Posix filepath to the desired file/location
        create : bool
            If the file does not exist, should it be created?
        delimiter : str
            What delimited should be used with the file?


        Examples
        --------
        >>> from pathlib import Path
        >>> example = Filer(Path.home() / 'tmp.tsv')

        """
        self.path = Path(path)
        self.delimiter = delimiter
        if not os.path.isfile(self.path):
            if create:
                self.path.touch()
                self.length = 0
                # Specifically for initiating todos
                self.append([["ID", "Rank", "Date", "Task"]])
            else:
                raise OSError("File does not exist")
        self.length = int(
            external_command(["wc", "-l", self.path]).stdout.strip().split()[0]
        )

    def append(self, rows: List[List[str]]) -> None:
        """Appends contents of `rows` to self.path

        Note
        ----
            This will not over-write the contents of the file, mirroring the modes of
            `open()`_

        .. _open(): 
            https://docs.python.org/3.7/library/functions.html#open

        Parameters
        ----------
        rows : List[List[str]]
            A list of strings to write to self.path.

        Returns
        -------
        None

        Examples
        --------
        >>> example.append([['f','g', 'h'], ['i', 'j', 'k']])

        """
        with open(self.path, "a", newline="") as file:
            writer = csv.writer(file, delimiter=self.delimiter)
            writer.writerows(rows)
        self.length += len(rows)

    def delete(self, contains: str) -> bool:
        """Deletes all lines from self where `contains in line`

        Parameters
        ----------
        contains : str
            String to match for line deletion

        Returns
        -------
        bool
            True if successulf, false otherwise

        Example
        -------
        >>> example.delete('j')
        True

        """
        with open(self.path, "r") as r_file:
            reader = csv.reader(r_file, delimiter=self.delimiter)
            with open("tmp", "a") as w_file:
                writer = csv.writer(w_file, delimiter=self.delimiter)
                for line in reader:
                    if contains not in line:
                        writer.writerow(line)

        # If deleted, copy and return true
        tmp_length = int(
            external_command(["wc", "-l", Path("tmp")]).stdout.strip().split()[0]
        )
        if self.length != tmp_length:
            shutil.move("tmp", self.path)
            self.length = tmp_length
            return True

        # Otherwise, clean tmp and return false
        os.remove(Path("tmp"))
        return False

    def read(self) -> List[List[str]]:
        """Read the lines of self.path

        Note
        ----
            Reads in all lines, so will suffer on large files

        Parameters
        ----------
        None
    
        Returns
        -------
        List[List[str]]
            A list of lines where each line is a list of column values

        Examples
        --------
        >>> example.read()
        [['ID', 'Rank', 'Date', 'Task'], ['f', 'g', 'h']]

        """
        with open(self.path, "r", newline="") as file:
            reader = csv.reader(file, delimiter=self.delimiter)
            lines = []
            for line in reader:
                lines.append(line)
        return lines

    def sort(self, cols: List[int], header: bool = False) -> None:
        """Sort the contents of self.path by columns

        Parameters
        ----------
        cols : List[int]
            List of column indices indicating what to sort by.
            Remember, Python is 0-indexed   
        header : bool
            Whether or not row 0 is a header. If True, row 0 is skipped for sorting

        Returns
        -------
        None

        Example
        -------
        >>> example.sort([1, 2], header=False)

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

    def write(self, rows: List[List[str]]) -> None:
        """Writes contents of rows to self.path.

        Warning
        -------
            If the file already has content, that will be overwritten!
            This mirrors the modes used by `open()`_

        .. _open(): 
            https://docs.python.org/3.7/library/functions.html#open

        Parameters
        ----------
        rows : List[List[str]]
            A list of strings to write to self.path. `rows[0]` represents line 1,
            and `rows[0][0]` is line 1, column 1.

        Returns
        -------
        None

        Examples
        --------
        >>> example.write([['a', 'b', 'c']])

        """
        with open(self.path, "w", newline="") as file:
            writer = csv.writer(file, delimiter=self.delimiter)
            writer.writerows(rows)
        self.length = len(rows)

    def write_col(self, col: List[str], index: int = 0) -> None:
        """Writes contents of col to self.path at specified index

        Warning
        -------
            If the column already has content, that will be overwritten!
            This mirrors the modes used by `open()`_

        .. _open(): 
            https://docs.python.org/3.7/library/functions.html#open

        Parameters
        ----------
        col : List[str]
            A list of strings to write to self.path. This should be the same length as
            `self.length`
        index : int
            Which column to write at. Remember, Python is 0-indexed.

        Returns
        -------
        None

        Raises
        ------
        IndexError
            When `col` has more or less items than `self.length`
        
        Examples
        --------
        >>> example.write_col(['d'], index=2)

        """
        if len(col) != self.length:
            raise IndexError(
                f"col does not have the right number of items! n_lines = {self.length}, n_items = {len(col)}."
            )
        lines = self.read()
        write_col = itemsetter(index)
        for line, val in zip(lines, col):
            write_col(line, val)
        self.write(lines)
