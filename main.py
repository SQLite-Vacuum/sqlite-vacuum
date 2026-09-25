"""SQLite Vacuum — Run VACUUM on a SQLite file and report size before and after."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='sqlite_vacuum',
        description='Run VACUUM on a SQLite file and report size before and after.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('SQLite Vacuum')
    print('Reclaim space from a SQLite file.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
