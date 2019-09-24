from pathlib import Path
from typing import List

import pandas as pd


def sort_csv_pd(file: Path, cols: List[str]) -> bool:
    """Sort a csv by one of its columns. Uses pandas

    :path: Path to the file
    :col: Which column to sort

    :returns: True, if successful

    """

    hold = pd.read_csv(
        file, header=None, names=["rank", "task", "date"], parse_dates=["date"]
    )
    hold = hold.sort_values(cols)
    hold.to_csv(file, header=False, index=False)
    return True
