from pathlib import Path

from ToDonePy.sort_csv_pd import sort_csv_pd as sort_csv_pd
from tests.make_temp import make_file

def test_sort_csv_pd(tmp_path):
    """Call sprt_csv_pd with an existing file"""
    csv = make_file(tmp_path, "3,Old task,2019-09-20 20:56:00\n1,New task,2019-09-24 11:33:00\n")
    result = sort_csv_pd(csv, ['rank'])
    assert result
    assert Path(csv).read_text() == f"1,New task,2019-09-24 11:33:00\n3,Old task,2019-09-20 20:56:00\n"
