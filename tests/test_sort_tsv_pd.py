from pathlib import Path

from ToDonePy.sort_tsv_pd import sort_tsv_pd as sort_tsv_pd
from tests.make_temp import make_file

def test_sort_tsv_pd(tmp_path):
    """Call sprt_tsv_pd with an existing file"""
    tsv = make_file(tmp_path, "3\tOld task\t2019-09-20 20:56:00\n1\tNew task\t2019-09-24 11:33:00\n")
    result = sort_tsv_pd(tsv, ['rank'])
    assert result
    assert Path(tsv).read_text() == f"1\tNew task\t2019-09-24 11:33:00\n3\tOld task\t2019-09-20 20:56:00\n"
