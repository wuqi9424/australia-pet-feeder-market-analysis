"""CSV typing shared by the public, offline summary modules."""
import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_table(filename):
    with (ROOT / 'data' / 'processed' / filename).open(encoding='utf-8-sig', newline='') as handle:
        return [{key: None if value == '' else value for key, value in row.items()}
                for row in csv.DictReader(handle)]


def number(value):
    if value is None:
        return None
    result = float(value)
    if not math.isfinite(result):
        raise ValueError('Non-finite number')
    return result


def boolean(value):
    if value is None:
        return None
    value = str(value).lower()
    if value not in ('true', 'false'):
        raise ValueError('Invalid Boolean; do not interpret arbitrary text as false')
    return value == 'true'


def unique(rows, fields):
    keys = [tuple(row[field] for field in fields) for row in rows]
    if any(any(value is None for value in key) for key in keys) or len(keys) != len(set(keys)):
        raise ValueError('Missing or duplicate identity key')


def emit(value):
    print(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False))
