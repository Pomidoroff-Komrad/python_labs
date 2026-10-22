import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    ...
    '''
    p = Path(path)
    return p.read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    '''
    ...
    '''
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    '''
    ...
    '''
    p = Path(path)
    rows = list(rows)

    if len(rows) != 0:
        len1 = len(rows[0])
        for i in rows:
            if len(i) != len1:
                raise ValueError('Все строки должны иметь одинаковую длину')

    ensure_parent_dir(path)
    
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)