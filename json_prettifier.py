#!/usr/bin/env python3
"""
json_prettifier.py
Pretty-print (and optionally sort) JSON from a file or STDIN.

Usage:
  python3 json_prettifier.py data.json
  cat data.json | python3 json_prettifier.py
  python3 json_prettifier.py --sort data.json
"""

import sys
import json
from typing import Any

def prettify_json(src: str | None = None, *, sort_keys: bool = False) -> str:
    """
    Load JSON from a file path (if provided) or from STDIN,
    then return a nicely formatted string.
    """
    try:
        if src:
            with open(src, "r", encoding="utf-8") as f:
                data: Any = json.load(f)
        else:
            data = json.load(sys.stdin)
    except FileNotFoundError:
        raise SystemExit(f"Error: file not found: {src}")
    except json.JSONDecodeError as e:
        raise SystemExit(f"Error: invalid JSON ({e})")

    return json.dumps(data, indent=2, ensure_ascii=False, sort_keys=sort_keys)

if __name__ == "__main__":
    args = sys.argv[1:]
    sort = False
    path = None

    if args and args[0] == "--sort":
        sort = True
        args = args[1:]

    if args:
        path = args[0]

    print(prettify_json(path, sort_keys=sort))
