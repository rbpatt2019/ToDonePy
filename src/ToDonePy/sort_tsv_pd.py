from pathlib import Path
from typing import List

import pandas as pd


def sort_tsv_pd(file: Path, cols: List[str]) -> bool:
    """Sort a tsv by one of its columns. Uses pandas

    :path: Path to the file
    :col: Which column to sort

    :returns: True, if successful

    """

    hold = pd.read_csv(
        file,
        header=None,
        names=["rank", "date", "task"],
        parse_dates=["date"],
        delimiter="\t",
    )
    hold = hold.sort_values(cols)
    hold.to_csv(file, header=False, index=False, sep="\t")
    return True
